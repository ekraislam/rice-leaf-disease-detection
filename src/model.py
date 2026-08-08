"""
Baseline CNN Model Architecture (ResNet18)
Adapted for 8-class Rice Leaf Disease Classification.
"""

import torch
import torch.nn as nn
import torchvision.models as models


def get_baseline_cnn(num_classes=8, pretrained=True):
    """
    Constructs ResNet18 baseline CNN classifier.
    If pretrained=True, loads ImageNet pretrained weights and replaces
    the final fc layer.
    """
    if pretrained:
        weights = models.ResNet18_Weights.DEFAULT
        model = models.resnet18(weights=weights)
    else:
        model = models.resnet18(weights=None)

    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)

    return model


def count_parameters(model):
    """Counts total and trainable parameters in the model."""
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(
        p.numel() for p in model.parameters() if p.requires_grad
    )
    return total_params, trainable_params
