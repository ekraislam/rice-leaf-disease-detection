"""
Conditional Wasserstein GAN with Gradient Penalty (cWGAN-GP) Model Architecture
Target Resolution: 128x128 RGB
Target Classes: 8 Rice Leaf Disease Classes
"""

import torch
import torch.nn as nn

class Generator(nn.Module):
    """
    cWGAN-GP Generator.
    Maps latent noise vector (z_dim=100) + class embedding (embed_dim=32)
    to a (3, 128, 128) synthetic rice leaf image in [-1.0, 1.0].
    """
    def __init__(self, z_dim=100, num_classes=8, embed_dim=32, feature_dim=64):
        super(Generator, self).__init__()
        self.z_dim = z_dim
        self.num_classes = num_classes
        self.embed_dim = embed_dim
        
        self.label_emb = nn.Embedding(num_classes, embed_dim)
        
        # Combined latent vector size: 100 + 32 = 132
        input_dim = z_dim + embed_dim
        
        self.net = nn.Sequential(
            # Project to (feature_dim * 16) x 4 x 4
            nn.ConvTranspose2d(input_dim, feature_dim * 16, kernel_size=4, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(feature_dim * 16),
            nn.ReLU(True),
            # (feature_dim * 16) x 4 x 4  -> (feature_dim * 8) x 8 x 8
            nn.ConvTranspose2d(feature_dim * 16, feature_dim * 8, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(feature_dim * 8),
            nn.ReLU(True),
            # (feature_dim * 8) x 8 x 8   -> (feature_dim * 4) x 16 x 16
            nn.ConvTranspose2d(feature_dim * 8, feature_dim * 4, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(feature_dim * 4),
            nn.ReLU(True),
            # (feature_dim * 4) x 16 x 16 -> (feature_dim * 2) x 32 x 32
            nn.ConvTranspose2d(feature_dim * 4, feature_dim * 2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(feature_dim * 2),
            nn.ReLU(True),
            # (feature_dim * 2) x 32 x 32 -> (feature_dim) x 64 x 64
            nn.ConvTranspose2d(feature_dim * 2, feature_dim, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(feature_dim),
            nn.ReLU(True),
            # (feature_dim) x 64 x 64     -> 3 x 128 x 128
            nn.ConvTranspose2d(feature_dim, 3, kernel_size=4, stride=2, padding=1, bias=False),
            nn.Tanh() # Output scaled to [-1.0, 1.0]
        )

    def forward(self, noise, labels):
        # noise: (B, z_dim), labels: (B,)
        c_emb = self.label_emb(labels) # (B, embed_dim)
        x = torch.cat([noise, c_emb], dim=1) # (B, z_dim + embed_dim)
        x = x.unsqueeze(-1).unsqueeze(-1) # (B, input_dim, 1, 1)
        return self.net(x)


class Discriminator(nn.Module):
    """
    cWGAN-GP Discriminator (Critic).
    Takes (3, 128, 128) image + class label, maps to scalar critic score D(x, c).
    Uses InstanceNorm2d instead of BatchNorm (required by WGAN-GP rules).
    """
    def __init__(self, num_classes=8, img_size=128, feature_dim=64):
        super(Discriminator, self).__init__()
        self.num_classes = num_classes
        self.img_size = img_size
        
        self.label_emb = nn.Embedding(num_classes, img_size * img_size)
        
        # 3 channels (image) + 1 channel (class map) = 4 input channels
        self.net = nn.Sequential(
            # 4 x 128 x 128 -> (feature_dim) x 64 x 64
            nn.Conv2d(4, feature_dim, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2, inplace=True),
            # (feature_dim) x 64 x 64 -> (feature_dim * 2) x 32 x 32
            nn.Conv2d(feature_dim, feature_dim * 2, kernel_size=4, stride=2, padding=1),
            nn.InstanceNorm2d(feature_dim * 2, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            # (feature_dim * 2) x 32 x 32 -> (feature_dim * 4) x 16 x 16
            nn.Conv2d(feature_dim * 2, feature_dim * 4, kernel_size=4, stride=2, padding=1),
            nn.InstanceNorm2d(feature_dim * 4, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            # (feature_dim * 4) x 16 x 16 -> (feature_dim * 8) x 8 x 8
            nn.Conv2d(feature_dim * 4, feature_dim * 8, kernel_size=4, stride=2, padding=1),
            nn.InstanceNorm2d(feature_dim * 8, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            # (feature_dim * 8) x 8 x 8 -> (feature_dim * 16) x 4 x 4
            nn.Conv2d(feature_dim * 8, feature_dim * 16, kernel_size=4, stride=2, padding=1),
            nn.InstanceNorm2d(feature_dim * 16, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            # (feature_dim * 16) x 4 x 4 -> 1 x 1 x 1
            nn.Conv2d(feature_dim * 16, 1, kernel_size=4, stride=1, padding=0)
            # No Sigmoid! (Wasserstein Critic returns raw linear score)
        )

    def forward(self, images, labels):
        # images: (B, 3, 128, 128), labels: (B,)
        B, C, H, W = images.size()
        c_map = self.label_emb(labels).view(B, 1, H, W)
        x = torch.cat([images, c_map], dim=1) # (B, 4, 128, 128)
        return self.net(x).view(B, -1)
