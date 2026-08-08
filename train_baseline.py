"""
Baseline CNN Classifier Training & Evaluation Script
Model: ResNet18 (ImageNet Pretrained)
Dataset: Cleaned Rice Leaf Disease (8 classes)
"""

import os
import sys
import json
import time
import copy
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support

# Optimize CPU threads for PyTorch
torch.set_num_threads(max(1, os.cpu_count() // 2))

# Ensure workspace root is in sys.path
workspace_dir = r"c:\Users\HP\Desktop\Rice Leaf Disease Detection Using GAN-Augmented CNN"
if workspace_dir not in sys.path:
    sys.path.insert(0, workspace_dir)

from src.data_loader import create_data_loaders, set_seed
from src.model import get_baseline_cnn, count_parameters

def main():
    # -------------------------------------------------------------
    # 0. CONFIGURATION & REPRODUCIBILITY SETUP
    # -------------------------------------------------------------
    SEED = 42
    BATCH_SIZE = 32
    NUM_CLASSES = 8
    INITIAL_LR = 0.001
    MAX_EPOCHS = 15
    PATIENCE = 4
    TARGET_SIZE = (224, 224)
    DATASET_ROOT = os.path.join(workspace_dir, "Rice leaf disease")
    
    set_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Output directories
    models_dir = os.path.join(workspace_dir, "models")
    results_dir = os.path.join(workspace_dir, "results")
    plots_dir = os.path.join(workspace_dir, "plots")
    
    for d in [models_dir, results_dir, plots_dir]:
        os.makedirs(d, exist_ok=True)

    print("=" * 80, flush=True)
    print("BASELINE CNN CLASSIFIER EXPERIMENT (RESNET18)", flush=True)
    print("=" * 80, flush=True)
    print(f"Device: {device}", flush=True)
    print(f"Random Seed: {SEED}", flush=True)
    print(f"Batch Size: {BATCH_SIZE}", flush=True)
    print(f"Learning Rate: {INITIAL_LR}", flush=True)
    print(f"Max Epochs: {MAX_EPOCHS}", flush=True)
    print(f"Early Stopping Patience: {PATIENCE} epochs", flush=True)

    # -------------------------------------------------------------
    # 1. PRE-TRAINING VERIFICATION & DATA LOADING
    # -------------------------------------------------------------
    print("\n[STEP 1] Pre-Training Verification & Data Loading...", flush=True)
    loaders, datasets = create_data_loaders(
        dataset_root=DATASET_ROOT,
        batch_size=BATCH_SIZE,
        target_size=TARGET_SIZE,
        seed=SEED,
        normalize_imagenet=True,
        return_tensor=True,
        preload=True
    )

    train_ds = datasets['train']
    val_ds = datasets['val']
    test_ds = datasets['test']

    classes = train_ds.classes
    class_to_idx = train_ds.class_to_idx
    idx_to_class = train_ds.idx_to_class

    print("\n--- Verified Class Mapping ---", flush=True)
    for c, i in class_to_idx.items():
        print(f"  Index {i}: {c}", flush=True)

    print("\n--- Verified Split Image Counts ---", flush=True)
    print(f"  Training Set:   {len(train_ds)} images ({len(loaders['train'])} batches)", flush=True)
    print(f"  Validation Set: {len(val_ds)} images ({len(loaders['val'])} batches)", flush=True)
    print(f"  Testing Set:    {len(test_ds)} images ({len(loaders['test'])} batches)", flush=True)

    assert len(train_ds) == 1291, f"Expected 1291 train samples, got {len(train_ds)}"
    assert len(val_ds) == 178, f"Expected 178 val samples, got {len(val_ds)}"
    assert len(test_ds) == 366, f"Expected 366 test samples, got {len(test_ds)}"
    print("[VERIFICATION PASSED] All image counts and class mappings verified.", flush=True)

    # -------------------------------------------------------------
    # 2. CLASS WEIGHTS & LOSS FUNCTION SETUP
    # -------------------------------------------------------------
    print("\n[STEP 2] Calculating Class Weights for Cross-Entropy Loss...", flush=True)
    train_class_counts = [0] * NUM_CLASSES
    for _, label in train_ds.samples:
        train_class_counts[label] += 1
        
    print("Training Class Counts:", flush=True)
    for idx, cnt in enumerate(train_class_counts):
        print(f"  Class {idx} ({idx_to_class[idx]}): {cnt} images", flush=True)

    total_train = len(train_ds)
    class_weights = [total_train / (NUM_CLASSES * cnt) for cnt in train_class_counts]
    weights_tensor = torch.tensor(class_weights, dtype=torch.float32).to(device)
    
    print("\nNormalized Class Weights:", flush=True)
    for idx, w in enumerate(class_weights):
        print(f"  Class {idx} ({idx_to_class[idx]}): {w:.4f}", flush=True)

    criterion = nn.CrossEntropyLoss(weight=weights_tensor)

    # -------------------------------------------------------------
    # 3. MODEL INSTANTIATION
    # -------------------------------------------------------------
    print("\n[STEP 3] Initializing ResNet18 Pretrained Model...", flush=True)
    model = get_baseline_cnn(num_classes=NUM_CLASSES, pretrained=True).to(device)
    total_params, trainable_params = count_parameters(model)
    print(f"Total Parameters:     {total_params:,}", flush=True)
    print(f"Trainable Parameters: {trainable_params:,}", flush=True)

    optimizer = optim.Adam(model.parameters(), lr=INITIAL_LR)

    # -------------------------------------------------------------
    # 4. TRAINING LOOP WITH EARLY STOPPING (VAL LOSS ONLY)
    # -------------------------------------------------------------
    print("\n[STEP 4] Starting Model Training...", flush=True)
    best_val_loss = float('inf')
    best_model_weights = copy.deepcopy(model.state_dict())
    patience_counter = 0
    best_epoch = 0

    history = {
        'train_loss': [],
        'train_acc': [],
        'val_loss': [],
        'val_acc': []
    }

    start_time = time.time()

    for epoch in range(1, MAX_EPOCHS + 1):
        # --- Training Phase ---
        model.train()
        running_loss = 0.0
        running_corrects = 0
        total_train_samples = 0

        for images, labels in loaders['train']:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            _, preds = torch.max(outputs, 1)
            running_loss += loss.item() * images.size(0)
            running_corrects += torch.sum(preds == labels.data).item()
            total_train_samples += images.size(0)

        epoch_train_loss = running_loss / total_train_samples
        epoch_train_acc = running_corrects / total_train_samples

        # --- Validation Phase (Strictly Val Set Only) ---
        model.eval()
        val_running_loss = 0.0
        val_running_corrects = 0
        total_val_samples = 0

        with torch.no_grad():
            for images, labels in loaders['val']:
                images = images.to(device)
                labels = labels.to(device)

                outputs = model(images)
                loss = criterion(outputs, labels)

                _, preds = torch.max(outputs, 1)
                val_running_loss += loss.item() * images.size(0)
                val_running_corrects += torch.sum(preds == labels.data).item()
                total_val_samples += images.size(0)

        epoch_val_loss = val_running_loss / total_val_samples
        epoch_val_acc = val_running_corrects / total_val_samples

        history['train_loss'].append(epoch_train_loss)
        history['train_acc'].append(epoch_train_acc)
        history['val_loss'].append(epoch_val_loss)
        history['val_acc'].append(epoch_val_acc)

        print(f"Epoch {epoch:02d}/{MAX_EPOCHS:02d} | "
              f"Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc*100:.2f}% | "
              f"Val Loss: {epoch_val_loss:.4f} | Val Acc: {epoch_val_acc*100:.2f}%", flush=True)

        if epoch_val_loss < best_val_loss:
            best_val_loss = epoch_val_loss
            best_model_weights = copy.deepcopy(model.state_dict())
            best_epoch = epoch
            patience_counter = 0
            model_save_path = os.path.join(models_dir, "baseline_cnn.pth")
            torch.save(best_model_weights, model_save_path)
            print(f"  [CHECKPOINT SAVED] Best val loss: {best_val_loss:.4f} at epoch {epoch}", flush=True)
        else:
            patience_counter += 1
            print(f"  [EARLY STOPPING MONITOR] No improvement for {patience_counter}/{PATIENCE} epochs", flush=True)
            if patience_counter >= PATIENCE:
                print(f"\n[EARLY STOPPING TRIGGERED] Training stopped at epoch {epoch}.", flush=True)
                break

    training_time = time.time() - start_time
    total_epochs_completed = len(history['train_loss'])
    print(f"\nTraining completed in {training_time:.2f} seconds across {total_epochs_completed} epochs.", flush=True)
    print(f"Best model selected from Epoch {best_epoch} with Val Loss: {best_val_loss:.4f}", flush=True)

    # Load best weights before test evaluation
    model.load_state_dict(best_model_weights)

    # -------------------------------------------------------------
    # 5. GENERATE & SAVE TRAINING CURVES PLOTS
    # -------------------------------------------------------------
    print("\n[STEP 5] Plotting & Saving Training History Curves...", flush=True)
    epochs_range = range(1, total_epochs_completed + 1)
    
    # Loss Curve Plot
    plt.figure(figsize=(8, 5))
    plt.plot(epochs_range, history['train_loss'], 'b-o', label='Training Loss', linewidth=2)
    plt.plot(epochs_range, history['val_loss'], 'r-s', label='Validation Loss', linewidth=2)
    plt.axvline(best_epoch, color='g', linestyle='--', label=f'Best Model (Epoch {best_epoch})')
    plt.title('Baseline CNN (ResNet18): Training vs Validation Loss', fontsize=12, fontweight='bold')
    plt.xlabel('Epoch', fontsize=11)
    plt.ylabel('Weighted Cross-Entropy Loss', fontsize=11)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    loss_plot_path = os.path.join(plots_dir, "baseline_loss_curve.png")
    plt.savefig(loss_plot_path, dpi=150)
    plt.close()
    print(f"  Saved: {loss_plot_path}", flush=True)

    # Accuracy Curve Plot
    plt.figure(figsize=(8, 5))
    plt.plot(epochs_range, [acc * 100 for acc in history['train_acc']], 'b-o', label='Training Accuracy', linewidth=2)
    plt.plot(epochs_range, [acc * 100 for acc in history['val_acc']], 'r-s', label='Validation Accuracy', linewidth=2)
    plt.axvline(best_epoch, color='g', linestyle='--', label=f'Best Model (Epoch {best_epoch})')
    plt.title('Baseline CNN (ResNet18): Training vs Validation Accuracy', fontsize=12, fontweight='bold')
    plt.xlabel('Epoch', fontsize=11)
    plt.ylabel('Accuracy (%)', fontsize=11)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    acc_plot_path = os.path.join(plots_dir, "baseline_accuracy_curve.png")
    plt.savefig(acc_plot_path, dpi=150)
    plt.close()
    print(f"  Saved: {acc_plot_path}", flush=True)

    # -------------------------------------------------------------
    # 6. FINAL EVALUATION ON UNSEEN TEST SET (EXACTLY ONCE)
    # -------------------------------------------------------------
    print("\n[STEP 6] Final Evaluation of Best Model on Unseen Test Set...", flush=True)
    model.eval()
    all_test_preds = []
    all_test_targets = []
    test_running_loss = 0.0
    total_test_samples = 0

    with torch.no_grad():
        for images, labels in loaders['test']:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            loss = criterion(outputs, labels)

            _, preds = torch.max(outputs, 1)
            test_running_loss += loss.item() * images.size(0)
            total_test_samples += images.size(0)

            all_test_preds.extend(preds.cpu().numpy())
            all_test_targets.extend(labels.cpu().numpy())

    test_loss = test_running_loss / total_test_samples
    all_test_preds = np.array(all_test_preds)
    all_test_targets = np.array(all_test_targets)

    test_acc = np.mean(all_test_preds == all_test_targets)

    precision_macro, recall_macro, f1_macro, _ = precision_recall_fscore_support(
        all_test_targets, all_test_preds, average='macro'
    )
    precision_weighted, recall_weighted, f1_weighted, _ = precision_recall_fscore_support(
        all_test_targets, all_test_preds, average='weighted'
    )

    print("\n" + "=" * 60, flush=True)
    print("FINAL TEST SET EVALUATION RESULTS", flush=True)
    print("=" * 60, flush=True)
    print(f"Test Loss:             {test_loss:.4f}", flush=True)
    print(f"Test Accuracy:         {test_acc * 100:.2f}% ({np.sum(all_test_preds == all_test_targets)}/{len(all_test_targets)})", flush=True)
    print(f"Precision (Macro):     {precision_macro:.4f}", flush=True)
    print(f"Recall (Macro):        {recall_macro:.4f}", flush=True)
    print(f"F1 Score (Macro):      {f1_macro:.4f}", flush=True)
    print(f"Precision (Weighted):  {precision_weighted:.4f}", flush=True)
    print(f"Recall (Weighted):     {recall_weighted:.4f}", flush=True)
    print(f"F1 Score (Weighted):   {f1_weighted:.4f}", flush=True)

    clr_str = classification_report(
        all_test_targets,
        all_test_preds,
        target_names=classes,
        digits=4
    )
    print("\n--- Detailed Per-Class Classification Report ---", flush=True)
    print(clr_str, flush=True)

    report_save_path = os.path.join(results_dir, "classification_report.txt")
    with open(report_save_path, "w") as f:
        f.write("BASELINE CNN (RESNET18) CLASSIFICATION REPORT\n")
        f.write("=" * 60 + "\n")
        f.write(clr_str)
    print(f"Saved classification report to: {report_save_path}", flush=True)

    cm = confusion_matrix(all_test_targets, all_test_preds)
    
    plt.figure(figsize=(10, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Baseline CNN (ResNet18): Test Set Confusion Matrix', fontsize=12, fontweight='bold')
    plt.colorbar()
    tick_marks = np.arange(NUM_CLASSES)
    plt.xticks(tick_marks, classes, rotation=45, ha='right', fontsize=9)
    plt.yticks(tick_marks, classes, fontsize=9)

    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True Class', fontsize=11)
    plt.xlabel('Predicted Class', fontsize=11)
    plt.tight_layout()
    cm_plot_path = os.path.join(plots_dir, "baseline_confusion_matrix.png")
    plt.savefig(cm_plot_path, dpi=150)
    plt.close()
    print(f"Saved confusion matrix plot to: {cm_plot_path}", flush=True)

    metrics_data = {
        'model_architecture': 'ResNet18 (ImageNet Pretrained)',
        'total_parameters': total_params,
        'trainable_parameters': trainable_params,
        'random_seed': SEED,
        'batch_size': BATCH_SIZE,
        'initial_learning_rate': INITIAL_LR,
        'optimizer': 'Adam',
        'loss_function': 'Class-Weighted CrossEntropyLoss',
        'class_weights': class_weights,
        'max_epochs': MAX_EPOCHS,
        'epochs_completed': total_epochs_completed,
        'best_epoch': best_epoch,
        'early_stopping_patience': PATIENCE,
        'best_val_loss': best_val_loss,
        'best_val_acc': history['val_acc'][best_epoch - 1],
        'test_loss': test_loss,
        'test_accuracy': float(test_acc),
        'test_precision_macro': float(precision_macro),
        'test_recall_macro': float(recall_macro),
        'test_f1_macro': float(f1_macro),
        'test_precision_weighted': float(precision_weighted),
        'test_recall_weighted': float(recall_weighted),
        'test_f1_weighted': float(f1_weighted),
        'confusion_matrix': cm.tolist(),
        'training_history': history,
        'training_time_seconds': training_time
    }

    metrics_save_path = os.path.join(results_dir, "baseline_cnn_metrics.json")
    with open(metrics_save_path, "w") as f:
        json.dump(metrics_data, f, indent=2)
    print(f"Saved JSON evaluation metrics to: {metrics_save_path}", flush=True)

    print("\n" + "=" * 80, flush=True)
    print("BASELINE CNN TRAINING AND EVALUATION SUCCESSFULLY COMPLETED", flush=True)
    print("=" * 80, flush=True)

if __name__ == '__main__':
    main()
