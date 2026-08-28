"""
Grad-CAM (Gradient-weighted Class Activation Mapping) for ResNet18.
Provides Explainable AI (XAI) visual heatmaps for disease lesion localization.

Optimized: Single-pass mode reuses activations captured during the main
inference forward pass, eliminating the need for a second model forward pass.
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
            self.activations = output.detach()

        def backward_hook(module, grad_input, grad_output):
            self.gradients = grad_output[0].detach()

        h1 = self.target_layer.register_forward_hook(forward_hook)
        h2 = self.target_layer.register_full_backward_hook(backward_hook)
        self.handles = [h1, h2]

    def generate_from_logits(self, logits, class_idx):
        """
        Computes Grad-CAM using already-captured activations from a previous
        forward pass. This avoids a second model forward pass entirely.

        Call this AFTER running the model with requires_grad=True on the input.
        The hooks must have captured activations during that forward pass.

        Args:
            logits:    Raw model output tensor (shape: [1, num_classes])
            class_idx: The predicted class index to explain
        """
        if self.activations is None:
            return None

        # Zero any previous gradients
        if logits.grad_fn is None:
            return None

        score = logits[0, class_idx]
        score.backward(retain_graph=False)

        if self.gradients is None:
            return None

        return self._build_cam()

    def generate(self, input_tensor, class_idx=None):
        """
        Legacy method: runs its own forward+backward pass.
        Use generate_from_logits() when possible to avoid double pass.

        Args:
            input_tensor: shape (1, 3, 224, 224), requires_grad=True
            class_idx:    class to explain (None = argmax)
        """
        output = self.model(input_tensor)

        if class_idx is None:
            class_idx = torch.argmax(output, dim=1).item()

        score = output[0, class_idx]
        score.backward(retain_graph=False)

        if self.gradients is None or self.activations is None:
            return None

        return self._build_cam()

    def _build_cam(self):
        """Shared CAM construction from captured activations & gradients."""
        # Global average pooling on gradients
        weights = torch.mean(self.gradients, dim=(2, 3), keepdim=True)
        cam = torch.sum(weights * self.activations, dim=1, keepdim=True)
        cam = F.relu(cam)
        cam = F.interpolate(cam, size=(224, 224), mode="bilinear", align_corners=False)
        cam = cam.squeeze().cpu().numpy()

        self.activations = None
        self.gradients = None

        # Normalize 0..1
        cam_min, cam_max = cam.min(), cam.max()
        if cam_max > cam_min:
            cam = (cam - cam_min) / (cam_max - cam_min)
        else:
            cam = np.zeros_like(cam)

        return cam

    def overlay_heatmap(self, original_pil_image, cam_numpy, alpha=0.45, max_dim=640):
        """
        Blends the jet colormap heatmap with the original PIL image.
        Constrains output resolution to max_dim (default 640px) to prevent
        uncompressed bitmap memory spikes on low-memory cloud instances.
        Returns a base64 Data URI string.
        """
        # Ensure working image is bounded in size and in RGB mode
        img_rgb = original_pil_image.convert("RGB")
        w, h = img_rgb.size
        if max(w, h) > max_dim:
            scale = max_dim / float(max(w, h))
            new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))
            img_rgb = img_rgb.resize((new_w, new_h), Image.Resampling.BILINEAR)

        target_size = img_rgb.size

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
            target_size, Image.Resampling.BILINEAR
        )

        blended = Image.blend(img_rgb, heatmap_img, alpha=alpha)

        buffered = io.BytesIO()
        blended.save(buffered, format="JPEG", quality=80, optimize=True)
        encoded_data = "data:image/jpeg;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8")

        # Explicitly close buffers
        buffered.close()
        del heatmap_img, blended, img_rgb, colored_heatmap, lut
        return encoded_data

    def close(self):
        for h in self.handles:
            h.remove()
        self.handles = []
        self.activations = None
        self.gradients = None
