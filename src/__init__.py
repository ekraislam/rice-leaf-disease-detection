"""
Rice Leaf Disease Detection package.
"""
# Only import what the web app needs for inference.
# GAN training utilities are excluded to keep the deployment lightweight.
from .model import get_baseline_cnn, count_parameters

__all__ = [
    "get_baseline_cnn",
    "count_parameters",
]
