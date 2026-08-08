import torch
import torch.nn as nn

class Generator(nn.Module):
    """DCGAN‑style Generator for 64×64 RGB images with class conditioning.
    Args:
        z_dim (int): Latent vector dimension.
        num_classes (int): Number of disease classes.
        embed_dim (int): Dimension of class embedding.
        feature_dim (int): Base feature dimension.
    """
    def __init__(self, z_dim=100, num_classes=8, embed_dim=32, feature_dim=64):
        super(Generator, self).__init__()
        self.label_emb = nn.Embedding(num_classes, embed_dim)
        self.project = nn.Sequential(
            nn.Linear(z_dim + embed_dim, feature_dim * 8 * 4 * 4, bias=False),
            nn.BatchNorm1d(feature_dim * 8 * 4 * 4),
            nn.ReLU(True)
        )
        self.net = nn.Sequential(
            nn.ConvTranspose2d(feature_dim * 8, feature_dim * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 4),
            nn.ReLU(True),
            nn.ConvTranspose2d(feature_dim * 4, feature_dim * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim * 2),
            nn.ReLU(True),
            nn.ConvTranspose2d(feature_dim * 2, feature_dim, 4, 2, 1, bias=False),
            nn.BatchNorm2d(feature_dim),
            nn.ReLU(True),
            nn.ConvTranspose2d(feature_dim, 3, 4, 2, 1, bias=False),
            nn.Tanh()
        )
    def forward(self, noise, labels):
        embed = self.label_emb(labels)
        x = torch.cat([noise, embed], dim=1)
        x = self.project(x)
        x = x.view(x.size(0), -1, 4, 4)
        return self.net(x)

class Discriminator(nn.Module):
    """DCGAN‑style Critic with class conditioning for WGAN‑GP.
    Takes an image and a class label, concatenates the embedding as extra channels.
    """
    def __init__(self, num_classes=8, img_size=64, embed_dim=32, feature_dim=64):
        super(Discriminator, self).__init__()
        self.label_emb = nn.Embedding(num_classes, embed_dim * img_size * img_size)
        self.img_size = img_size
        self.embed_dim = embed_dim
        self.net = nn.Sequential(
            nn.Conv2d(3 + embed_dim, feature_dim, 4, 2, 1),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(feature_dim, feature_dim * 2, 4, 2, 1),
            nn.InstanceNorm2d(feature_dim * 2, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(feature_dim * 2, feature_dim * 4, 4, 2, 1),
            nn.InstanceNorm2d(feature_dim * 4, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(feature_dim * 4, feature_dim * 8, 4, 2, 1),
            nn.InstanceNorm2d(feature_dim * 8, affine=True),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(feature_dim * 8, 1, 4, 1, 0)
        )
    def forward(self, images, labels):
        B = images.size(0)
        # Reshape embedding to (B, embed_dim, H, W)
        c_map = self.label_emb(labels).view(B, self.embed_dim, self.img_size, self.img_size)
        x = torch.cat([images, c_map], dim=1)
        return self.net(x).view(B, -1)
