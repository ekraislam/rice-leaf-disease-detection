"""
Grad-CAM (Gradient-weighted Class Activation Mapping) for ResNet18.
Provides Explainable AI (XAI) visual heatmaps for disease lesion localization.
"""

import io
import base64
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image


class GradCAM:
    def __init__(self, model, target_layer=None):
        self.model = model
        self.target_layer = target_layer if target_layer is not None else model.layer4[-1].conv2
        self.activations = None
        self.gradients = None
        self.handles = []
        self._register_hooks()

    def _register_hooks(self):
        def forward_hook(module, input, output):
            self.activations = output

        def backward_hook(module, grad_input, grad_output):
            self.gradients = grad_output[0]

        h1 = self.target_layer.register_forward_hook(forward_hook)
        h2 = self.target_layer.register_full_backward_hook(backward_hook)
        self.handles = [h1, h2]

    def generate(self, input_tensor, class_idx=None):
        """
        Computes the Grad-CAM activation map for the given input tensor.
        input_tensor: shape (1, 3, 224, 224)
        """
        output = self.model(input_tensor)

        if class_idx is None:
            class_idx = torch.argmax(output, dim=1).item()

        score = output[0, class_idx]
        score.backward(retain_graph=False)

        if self.gradients is None or self.activations is None:
            return None

        # Global average pooling on gradients
        weights = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        cam = torch.sum(weights * self.activations, dim=1, keepdim=True)
        cam = F.relu(cam)
        cam = F.interpolate(cam, size=(224, 224), mode="bilinear", align_corners=False)
        cam = cam.squeeze().detach().cpu().numpy()

        self.activations = None
        self.gradients = None

        # Normalize 0..1
        cam_min, cam_max = cam.min(), cam.max()
        if cam_max > cam_min:
            cam = (cam - cam_min) / (cam_max - cam_min)
        else:
            cam = np.zeros_like(cam)

        return cam

    def overlay_heatmap(self, original_pil_image, cam_numpy, alpha=0.45):
        """
        Blends the jet colormap heatmap with the original PIL image.
        Returns a base64 Data URI string.
        """
        h_uint8 = (cam_numpy * 255).astype(np.uint8)
        lut = np.zeros((256, 3), dtype=np.uint8)
        for i in range(256):
            v = i / 255.0
            r = np.clip(1.5 - abs(4.0 * v - 3.0), 0, 1)
            g = np.clip(1.5 - abs(4.0 * v - 2.0), 0, 1)
            b = np.clip(1.5 - abs(4.0 * v - 1.0), 0, 1)
            lut[i] = [int(r * 255), int(g * 255), int(b * 255)]

        colored_heatmap = lut[h_uint8]
        heatmap_img = Image.fromarray(colored_heatmap).resize(
            original_pil_image.size, Image.Resampling.BILINEAR
        )

        blended = Image.blend(original_pil_image.convert("RGB"), heatmap_img, alpha=alpha)

        buffered = io.BytesIO()
        blended.save(buffered, format="JPEG", quality=85)
        return "data:image/jpeg;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8")

    def close(self):
        for h in self.handles:
            h.remove()
