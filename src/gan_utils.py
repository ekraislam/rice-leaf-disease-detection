"""
cWGAN-GP Utilities: Gradient Penalty Calculation & Fixed Noise Grid Visualization
"""

import os
import torch
import numpy as np
import matplotlib.pyplot as plt

def compute_gradient_penalty(discriminator, real_samples, fake_samples, labels, device, lambda_gp=10.0):
    """
    Calculates 1-Lipschitz Gradient Penalty for WGAN-GP:
    GP = E[(||grad_{x_hat} D(x_hat, c)||_2 - 1)^2]
    """
    batch_size = real_samples.size(0)
    # Random interpolation weight alpha ~ U(0, 1)
    alpha = torch.rand(batch_size, 1, 1, 1, device=device)
    interpolates = (alpha * real_samples + (1 - alpha) * fake_samples).requires_grad_(True)
    
    d_interpolates = discriminator(interpolates, labels)
    fake_grad_outputs = torch.ones_like(d_interpolates, device=device)
    
    gradients = torch.autograd.grad(
        outputs=d_interpolates,
        inputs=interpolates,
        grad_outputs=fake_grad_outputs,
        create_graph=True,
        retain_graph=True,
        only_inputs=True
    )[0]
    
    gradients = gradients.view(batch_size, -1)
    gradient_norm = gradients.norm(2, dim=1)
    gradient_penalty = lambda_gp * ((gradient_norm - 1) ** 2).mean()
    return gradient_penalty

def save_fixed_sample_grid(generator, epoch, save_path, z_dim=100, num_classes=8, device='cpu'):
    """
    Generates a fixed 4x4 visual sample grid tracking lesion generation progress across epochs.
    Takes 2 fixed samples per class.
    """
    generator.eval()
    fixed_noise = torch.randn(16, z_dim, device=device)
    fixed_labels = torch.tensor([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7], device=device)
    
    with torch.no_grad():
        fake_imgs = generator(fixed_noise, fixed_labels).cpu()
        # Scale [-1.0, 1.0] to [0.0, 1.0] for plotting
        fake_imgs = (fake_imgs + 1.0) / 2.0
        fake_imgs = torch.clamp(fake_imgs, 0.0, 1.0)
        
    fig, axes = plt.subplots(4, 4, figsize=(10, 10))
    for idx, ax in enumerate(axes.flat):
        img_np = fake_imgs[idx].numpy().transpose((1, 2, 0)) # CHW -> HWC
        class_idx = fixed_labels[idx].item()
        ax.imshow(img_np)
        ax.set_title(f"Class {class_idx} (Epoch {epoch})", fontsize=8)
        ax.axis("off")
        
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    generator.train()
