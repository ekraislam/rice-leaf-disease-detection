"""
Optimized cWGAN‑GP training script (64×64, batch 16, n_critic 2, 20 epochs).
Features:
- Uses lightweight DCGAN model (src/dcgan_model.py).
- Saves a checkpoint after every epoch (models/cwgan_gen_epoch_XX.pth).
- Saves resume state (models/cwgan_resume_state.pth) containing epoch, generator/discriminator
  state_dicts and optimizer state_dicts.
- On start, loads latest resume state if present and continues training.
- Supports a dry‑run mode via "--dry" argument (runs 1 epoch, skips synthetic generation).
- Prints epoch, critic loss, generator loss, elapsed time, and checkpoint path.
"""
import os
import sys
import time
import argparse
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import torch
import torch.optim as optim

# Optimize CPU threads for PyTorch – keep a modest number to avoid oversubscription
torch.set_num_threads(max(1, os.cpu_count() // 2))

# Ensure workspace root is in sys.path
workspace_dir = r"c:\\Users\\HP\\Desktop\\Rice Leaf Disease Detection Using GAN-Augmented CNN"
if workspace_dir not in sys.path:
    sys.path.insert(0, workspace_dir)

from src.data_loader import RiceLeafDataset, set_seed
from src.dcgan_model import Generator, Discriminator
from src.gan_resume import save_resume_state, load_resume_state
from src.gan_utils import compute_gradient_penalty, save_fixed_sample_grid

def main():
    parser = argparse.ArgumentParser(description="Optimized cWGAN‑GP training with dry‑run support")
    parser.add_argument("--dry", action="store_true", help="Run a 1‑epoch dry‑run diagnostic (no synthetic generation)")
    args = parser.parse_args()

    # -------------------------------------------------------------
    # 0. CONFIGURATION & HYPERPARAMETERS
    # -------------------------------------------------------------
    SEED = 42
    Z_DIM = 100
    EMBED_DIM = 32
    NUM_CLASSES = 8
    GAN_SIZE = (64, 64)
    BATCH_SIZE = 16
    LR = 0.0002
    BETAS = (0.0, 0.9)
    N_CRITIC = 2
    LAMBDA_GP = 10.0
    EPOCHS = 1 if args.dry else 20
    RESUME_PATH = os.path.join(workspace_dir, "models", "cwgan_resume_state.pth")

    set_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # -------------------------------------------------------------
    # Dataset paths
    # -------------------------------------------------------------
    dataset_root = os.path.join(workspace_dir, "Rice leaf disease")
    train_split_dir = os.path.join(dataset_root, "Training data")

    models_dir = os.path.join(workspace_dir, "models")
    plots_dir = os.path.join(workspace_dir, "plots")
    synth_dir = os.path.join(workspace_dir, "gan_synthetic_images")
    for d in [models_dir, plots_dir, synth_dir]:
        os.makedirs(d, exist_ok=True)

    # -------------------------------------------------------------
    # Logging header
    # -------------------------------------------------------------
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
    # 1. LOAD TRAINING DATASET (GAN only)
    # -------------------------------------------------------------
    print("\n[STEP 1] Loading Training Dataset strictly for GAN training...", flush=True)
    train_ds = RiceLeafDataset(train_split_dir, target_size=GAN_SIZE, normalize_imagenet=False, preload=True)
    # Scale to [-1, 1] for Tanh activation
    tensor_images = ((train_ds.tensor_images * 2.0) - 1.0).to(device)
    tensor_labels = train_ds.tensor_labels.to(device)
    num_samples = len(tensor_images)
    print(f"Loaded {num_samples} real training images for GAN training.", flush=True)
    print(f"Class Mapping: {train_ds.class_to_idx}", flush=True)

    # -------------------------------------------------------------
    # 2. INITIALIZE MODELS (or resume)
    # -------------------------------------------------------------
    print("\n[STEP 2] Initializing Generator & Discriminator...", flush=True)
    netG = Generator(z_dim=Z_DIM, num_classes=NUM_CLASSES, embed_dim=EMBED_DIM, feature_dim=64).to(device)
    netD = Discriminator(num_classes=NUM_CLASSES, img_size=GAN_SIZE[0], feature_dim=64).to(device)
    optG = optim.Adam(netG.parameters(), lr=LR, betas=BETAS)
    optD = optim.Adam(netD.parameters(), lr=LR, betas=BETAS)

    start_epoch = 1
    if os.path.exists(RESUME_PATH):
        print("[RESUME] Loading resume state...", flush=True)
        resume_state = load_resume_state(RESUME_PATH, device)
        netG.load_state_dict(resume_state["netG"])
        netD.load_state_dict(resume_state["netD"])
        optG.load_state_dict(resume_state["optG"])
        optD.load_state_dict(resume_state["optD"])
        start_epoch = resume_state["epoch"] + 1
        print(f"Resuming from epoch {resume_state['epoch']} (starting at {start_epoch}).", flush=True)

    # -------------------------------------------------------------
    # 3. TRAINING LOOP
    # -------------------------------------------------------------
    print("\n[STEP 3] Starting cWGAN-GP training loop...", flush=True)
    g_losses = []
    d_losses = []
    total_start = time.time()

    for epoch in range(start_epoch, EPOCHS + 1):
        epoch_start = time.time()
        # Shuffle dataset each epoch
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

            # ---------------------
            # Train Critic (N_CRITIC steps per Generator update)
            # ---------------------
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

            # Train Generator every N_CRITIC iterations
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

        epoch_time = time.time() - epoch_start
        ckpt_path = os.path.join(models_dir, f"cwgan_gen_epoch_{epoch:02d}.pth")
        torch.save(netG.state_dict(), ckpt_path)
        torch.save(netG.state_dict(), os.path.join(models_dir, "cwgan_generator_latest.pth"))
        # Save full resume state after this epoch
        resume_state = {
            "epoch": epoch,
            "netG": netG.state_dict(),
            "netD": netD.state_dict(),
            "optG": optG.state_dict(),
            "optD": optD.state_dict()
        }
        save_resume_state(resume_state, RESUME_PATH)
        print(f"Epoch [{epoch}/{EPOCHS}] | D loss: {avg_d_loss:.4f} | G loss: {avg_g_loss:.4f} | Time: {epoch_time:.1f}s | Checkpoint: {ckpt_path}", flush=True)

    total_time = time.time() - total_start
    print(f"\nGAN training completed in {total_time:.2f}s across {EPOCHS} epochs.", flush=True)

    # -------------------------------------------------------------
    # 4. SAVE LOSS CURVE
    # -------------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(d_losses) + 1), d_losses, label='Discriminator Critic Loss (WGAN‑GP)', color='red')
    plt.plot(range(1, len(g_losses) + 1), g_losses, label='Generator Loss', color='blue')
    plt.title('cWGAN‑GP Training Loss History', fontsize=12, fontweight='bold')
    plt.xlabel('Epoch', fontsize=11)
    plt.ylabel('Loss', fontsize=11)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    loss_plot_path = os.path.join(plots_dir, "gan_training_loss_curve.png")
    plt.savefig(loss_plot_path, dpi=150)
    plt.close()
    print(f"Saved GAN loss plot to: {loss_plot_path}", flush=True)

    # -------------------------------------------------------------
    # 5. SYNTHETIC IMAGE GENERATION (skipped in dry‑run)
    # -------------------------------------------------------------
    if not args.dry:
        print("\n[STEP 5] Generating targeted synthetic images for minority classes...", flush=True)
        netG.eval()
        target_synthetic_counts = {
            "Narrow Brown Leaf Spot": 66,
            "Healthy Rice Leaf": 50,
            "Bacterial Leaf Blight": 34,
            "Rice Hispa": 22,
            "Leaf scald": 18
        }
        total_generated = 0
        preview_samples = []
        for c_name, count_needed in target_synthetic_counts.items():
            c_idx = train_ds.class_to_idx[c_name]
            class_dir = os.path.join(synth_dir, c_name)
            os.makedirs(class_dir, exist_ok=True)
            print(f"  Generating {count_needed} images for class '{c_name}' (idx {c_idx})...", flush=True)
            generated = 0
            attempts = 0
            max_attempts = count_needed * 3
            while generated < count_needed and attempts < max_attempts:
                attempts += 1
                z = torch.randn(1, Z_DIM, device=device)
                lbl = torch.tensor([c_idx], device=device)
                with torch.no_grad():
                    fake = netG(z, lbl).cpu().squeeze(0)
                fake_np = ((fake.numpy().transpose((1, 2, 0)) + 1) / 2 * 255.0).astype(np.uint8)
                if np.var(fake_np) < 10.0:
                    continue
                generated += 1
                total_generated += 1
                img = Image.fromarray(fake_np)
                out_path = os.path.join(class_dir, f"synth_{c_name.replace(' ', '_')}_{generated:03d}.jpg")
                img.save(out_path, format="JPEG", quality=95)
                if len(preview_samples) < 16:
                    preview_samples.append((fake_np, c_name, c_idx))
        print(f"\n[SUCCESS] Generated {total_generated} synthetic images.", flush=True)
        if preview_samples:
            fig, axes = plt.subplots(4, 4, figsize=(10, 10))
            for idx, ax in enumerate(axes.flat):
                if idx < len(preview_samples):
                    img_np, c_name, c_idx = preview_samples[idx]
                    ax.imshow(img_np)
                    ax.set_title(f"{c_name}\nIdx {c_idx}", fontsize=8)
                ax.axis('off')
            grid_path = os.path.join(plots_dir, "synthetic_samples_grid.png")
            plt.tight_layout()
            plt.savefig(grid_path, dpi=150)
            plt.close()
            print(f"Saved synthetic sample grid to: {grid_path}", flush=True)

    print("\n" + "=" * 80, flush=True)
    print("cWGAN-GP TRAINING & SYNTHETIC DATASET GENERATION COMPLETED", flush=True)
    print("=" * 80, flush=True)

if __name__ == '__main__':
    main()
