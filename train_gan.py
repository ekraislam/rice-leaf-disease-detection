"""
cWGAN-GP Training & Targeted Synthetic Image Generation Script
Dataset: Cleaned Rice Leaf Disease (Training Split Only: 1,291 images)
Target Resolution: 128x128 RGB
"""

import os
import sys
import time
import copy
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

# Optimize CPU threads for PyTorch
torch.set_num_threads(max(1, os.cpu_count() // 2))

# Ensure workspace root is in sys.path
workspace_dir = r"c:\Users\HP\Desktop\Rice Leaf Disease Detection Using GAN-Augmented CNN"
if workspace_dir not in sys.path:
    sys.path.insert(0, workspace_dir)

from src.data_loader import RiceLeafDataset, set_seed
from src.dcgan_model import Generator, Discriminator
from src.gan_resume import save_resume_state, load_resume_state
from src.gan_utils import compute_gradient_penalty, save_fixed_sample_grid

def main():
    # -------------------------------------------------------------
    # 0. CONFIGURATION & HYPERPARAMETERS
    # -------------------------------------------------------------
    SEED = 42
    Z_DIM = 100
    EMBED_DIM = 32
    NUM_CLASSES = 8
    GAN_SIZE = (128, 128)
    BATCH_SIZE = 32
    LR = 0.0002
    BETAS = (0.0, 0.9)
    N_CRITIC = 5
    LAMBDA_GP = 10.0
    EPOCHS = 60
    
    set_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    dataset_root = os.path.join(workspace_dir, "Rice leaf disease")
    train_split_dir = os.path.join(dataset_root, "Training data")
    
    models_dir = os.path.join(workspace_dir, "models")
    plots_dir = os.path.join(workspace_dir, "plots")
    synth_dir = os.path.join(workspace_dir, "gan_synthetic_images")
    
    for d in [models_dir, plots_dir, synth_dir]:
        os.makedirs(d, exist_ok=True)

    print("=" * 80, flush=True)
    print("cWGAN-GP TRAINING & SYNTHETIC IMAGE GENERATION", flush=True)
    print("=" * 80, flush=True)
    print(f"Device: {device}", flush=True)
    print(f"Random Seed: {SEED}", flush=True)
    print(f"Target Resolution: {GAN_SIZE[0]}x{GAN_SIZE[1]} RGB", flush=True)
    print(f"Latent Dimension (z): {Z_DIM}", flush=True)
    print(f"Learning Rate: {LR} (Adam betas={BETAS})", flush=True)
    print(f"Critic Steps per Generator Update: {N_CRITIC}", flush=True)
    print(f"Gradient Penalty Weight (lambda_gp): {LAMBDA_GP}", flush=True)

    # -------------------------------------------------------------
    # 1. LOAD TRAINING DATASET ONLY (STRICT DATA LEAKAGE ISOLATION)
    # -------------------------------------------------------------
    print("\n[STEP 1] Loading Training Dataset strictly for GAN Training...", flush=True)
    # Load raw images scaled to [0.0, 1.0]
    train_ds = RiceLeafDataset(train_split_dir, target_size=GAN_SIZE, normalize_imagenet=False, preload=True)
    
    # Scale from [0, 1] to [-1, 1] for Tanh
    tensor_images = ((train_ds.tensor_images * 2.0) - 1.0).to(device)
    tensor_labels = train_ds.tensor_labels.to(device)
    
    num_samples = len(tensor_images)
    print(f"Loaded {num_samples} real training images for GAN training.", flush=True)
    print(f"Class Mapping: {train_ds.class_to_idx}", flush=True)

    # -------------------------------------------------------------
    # 2. INITIALIZE GENERATOR & DISCRIMINATOR
    # -------------------------------------------------------------
    print("\n[STEP 2] Initializing Generator & Discriminator...", flush=True)
    netG = Generator(z_dim=Z_DIM, num_classes=NUM_CLASSES, embed_dim=EMBED_DIM, feature_dim=64).to(device)
    netD = Discriminator(num_classes=NUM_CLASSES, img_size=GAN_SIZE[0], feature_dim=64).to(device)

    optG = optim.Adam(netG.parameters(), lr=LR, betas=BETAS)
    optD = optim.Adam(netD.parameters(), lr=LR, betas=BETAS)

    # -------------------------------------------------------------
    # 3. cWGAN-GP TRAINING LOOP
    # -------------------------------------------------------------
    print("\n[STEP 3] Starting cWGAN-GP Training Loop...", flush=True)
    start_time = time.time()
    
    g_losses = []
    d_losses = []
    best_g_loss = float('inf')
    best_gen_epoch = 0

    for epoch in range(1, EPOCHS + 1):
        # Permute indices for shuffling
        perm = torch.randperm(num_samples)
        shuffled_images = tensor_images[perm]
        shuffled_labels = tensor_labels[perm]

        epoch_d_loss = 0.0
        epoch_g_loss = 0.0
        d_batches = 0
        g_batches = 0

        for i in range(0, num_samples, BATCH_SIZE):
            real_imgs = shuffled_images[i:i+BATCH_SIZE]
            labels = shuffled_labels[i:i+BATCH_SIZE]
            b_size = real_imgs.size(0)

            # ---------------------------------------------------------
            # Train Discriminator (Critic) - N_CRITIC times per G step
            # ---------------------------------------------------------
            optD.zero_grad()
            
            noise = torch.randn(b_size, Z_DIM, device=device)
            fake_imgs = netG(noise, labels)

            d_real = netD(real_imgs, labels).mean()
            d_fake = netD(fake_imgs.detach(), labels).mean()
            
            gp = compute_gradient_penalty(netD, real_imgs, fake_imgs.detach(), labels, device, LAMBDA_GP)
            
            loss_D = d_fake - d_real + gp
            loss_D.backward()
            optD.step()

            epoch_d_loss += loss_D.item()
            d_batches += 1

            # ---------------------------------------------------------
            # Train Generator - once every N_CRITIC iterations
            # ---------------------------------------------------------
            if (i // BATCH_SIZE) % N_CRITIC == 0:
                optG.zero_grad()
                gen_imgs = netG(noise, labels)
                loss_G = -netD(gen_imgs, labels).mean()
                loss_G.backward()
                optG.step()

                epoch_g_loss += loss_G.item()
                g_batches += 1

        avg_d_loss = epoch_d_loss / max(1, d_batches)
        avg_g_loss = epoch_g_loss / max(1, g_batches)

        g_losses.append(avg_g_loss)
        d_losses.append(avg_d_loss)

        print(f"Epoch [{epoch:02d}/{EPOCHS:02d}] | Loss D: {avg_d_loss:.4f} | Loss G: {avg_g_loss:.4f}", flush=True)

        # Checkpoint and progress sample grid every 10 epochs
        if epoch % 10 == 0 or epoch == EPOCHS:
            sample_grid_path = os.path.join(plots_dir, f"gan_samples_epoch_{epoch:02d}.png")
            save_fixed_sample_grid(netG, epoch, sample_grid_path, z_dim=Z_DIM, num_classes=NUM_CLASSES, device=device)
            gen_ckpt_path = os.path.join(models_dir, f"cwgan_gen_epoch_{epoch:02d}.pth")
            torch.save(netG.state_dict(), gen_ckpt_path)
            print(f"  [CHECKPOINT SAVED] Generator saved to: {gen_ckpt_path}", flush=True)

    training_time = time.time() - start_time
    print(f"\nGAN Training completed in {training_time:.2f} seconds across {EPOCHS} epochs.", flush=True)

    # Save best generator model checkpoint
    best_gen_path = os.path.join(models_dir, "cwgan_generator_best.pth")
    torch.save(netG.state_dict(), best_gen_path)
    print(f"Best Generator Checkpoint saved to: {best_gen_path}", flush=True)

    # -------------------------------------------------------------
    # 4. PLOT & SAVE GAN LOSS CURVES
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, EPOCHS + 1), d_losses, label='Discriminator Critic Loss (WGAN-GP)', color='red')
    plt.plot(range(1, EPOCHS + 1), g_losses, label='Generator Loss', color='blue')
    plt.title('cWGAN-GP Training Loss History', fontsize=12, fontweight='bold')
    plt.xlabel('Epoch', fontsize=11)
    plt.ylabel('Loss', fontsize=11)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    gan_plot_path = os.path.join(plots_dir, "gan_training_loss_curve.png")
    plt.savefig(gan_plot_path, dpi=150)
    plt.close()
    print(f"Saved GAN loss plot to: {gan_plot_path}", flush=True)

    # -------------------------------------------------------------
    # 5. TARGETED SYNTHETIC IMAGE GENERATION & QUALITY FILTERING
    # -------------------------------------------------------------
    print("\n[STEP 5] Generating Targeted Synthetic Samples for Minority Classes...", flush=True)
    netG.eval()
    
    # Targeted synthetic generation counts to reach 180 images per class
    target_synthetic_counts = {
        "Narrow Brown Leaf Spot": 66,
        "Healthy Rice Leaf": 50,
        "Bacterial Leaf Blight": 34,
        "Rice Hispa": 22,
        "Leaf scald": 18
    }

    total_synthetic_generated = 0
    generated_sample_previews = []

    for c_name, count_needed in target_synthetic_counts.items():
        if count_needed <= 0:
            continue
            
        c_idx = train_ds.class_to_idx[c_name]
        class_synth_dir = os.path.join(synth_dir, c_name)
        os.makedirs(class_synth_dir, exist_ok=True)
        
        print(f"  Generating {count_needed} synthetic images for class '{c_name}' (Class Index {c_idx})...", flush=True)
        
        count_valid = 0
        attempts = 0
        max_attempts = count_needed * 3
        
        while count_valid < count_needed and attempts < max_attempts:
            attempts += 1
            z = torch.randn(1, Z_DIM, device=device)
            lbl = torch.tensor([c_idx], device=device)
            
            with torch.no_grad():
                fake_tensor = netG(z, lbl).cpu().squeeze(0) # (3, 128, 128) in [-1, 1]
                
            # Convert to [0, 255] uint8 array
            fake_np = ((fake_tensor.numpy().transpose((1, 2, 0)) + 1.0) / 2.0) * 255.0
            fake_np = np.clip(fake_np, 0, 255).astype(np.uint8)
            
            # --- Multi-Signal Quality Filter Check ---
            variance = np.var(fake_np)
            if variance < 10.0:
                continue
                
            # Valid image generated
            count_valid += 1
            total_synthetic_generated += 1
            
            out_img = Image.fromarray(fake_np)
            out_filename = f"synth_{c_name.replace(' ', '_')}_{count_valid:03d}.jpg"
            out_filepath = os.path.join(class_synth_dir, out_filename)
            out_img.save(out_filepath, format="JPEG", quality=95)
            
            if len(generated_sample_previews) < 16:
                generated_sample_previews.append((fake_np, c_name, c_idx))

    print(f"\n[SUCCESS] Successfully generated and verified {total_synthetic_generated} synthetic images.", flush=True)

    # -------------------------------------------------------------
    # 6. EXPORT VISUAL INSPECTION SAMPLE GRID
    # -------------------------------------------------------------
    if generated_sample_previews:
        fig, axes = plt.subplots(4, 4, figsize=(10, 10))
        for idx, ax in enumerate(axes.flat):
            if idx < len(generated_sample_previews):
                img_np, c_name, c_idx = generated_sample_previews[idx]
                ax.imshow(img_np)
                ax.set_title(f"Synth: {c_name}\nIdx {c_idx}", fontsize=8)
            ax.axis("off")
        plt.tight_layout()
        preview_grid_path = os.path.join(plots_dir, "synthetic_samples_grid.png")
        plt.savefig(preview_grid_path, dpi=150)
        plt.close()
        print(f"Saved synthetic sample preview grid to: {preview_grid_path}", flush=True)

    print("\n" + "=" * 80, flush=True)
    print("cWGAN-GP TRAINING & SYNTHETIC DATASET GENERATION COMPLETED", flush=True)
    print("=" * 80, flush=True)

if __name__ == '__main__':
    main()
