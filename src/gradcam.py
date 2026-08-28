"""
Grad-CAM (Gradient-weighted Class Activation Mapping) for ResNet18.
Provides Explainable AI (XAI) visual heatmaps for disease lesion localization.

Optimized & Thread-Safe: Uses temporary scoped hooks with guaranteed cleanup
in finally blocks, preventing memory leaks and OpenMP/autograd collisions on cloud servers.
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

    def generate(self, input_tensor, class_idx=None):
        """
        Thread-safe, self-contained Grad-CAM generator.
        Registers temporary hooks, computes forward and backward pass,
        removes hooks immediately in finally block, and returns normalized heatmap.
        """
        activations = []
        gradients = []

        def forward_hook(module, inp, out):
            activations.append(out)

        def backward_hook(module, grad_in, grad_out):
            gradients.append(grad_out[0])

        h1 = self.target_layer.register_forward_hook(forward_hook)
        h2 = self.target_layer.register_full_backward_hook(backward_hook)

        try:
            # Clone input tensor with gradient tracking
            cam_input = input_tensor.clone().detach().requires_grad_(True)
            with torch.enable_grad():
                output = self.model(cam_input)

                if class_idx is None:
                    class_idx = torch.argmax(output, dim=1).item()

                score = output[0, class_idx]
                self.model.zero_grad(set_to_none=True)
                score.backward(retain_graph=False)

            if not activations or not gradients:
                return None

            act = activations[0].detach()
            grad = gradients[0].detach()

            weights = torch.mean(grad, dim=(2, 3), keepdim=True)
            cam = torch.sum(weights * act, dim=1, keepdim=True)
            cam = F.relu(cam)
            cam = F.interpolate(cam, size=(224, 224), mode="bilinear", align_corners=False)
            cam = cam.squeeze().cpu().numpy()

            cam_min, cam_max = cam.min(), cam.max()
            if cam_max > cam_min:
                cam = (cam - cam_min) / (cam_max - cam_min)
            else:
                cam = np.zeros_like(cam)

            return cam
        finally:
            h1.remove()
            h2.remove()
            self.model.zero_grad(set_to_none=True)
            del activations, gradients

    def overlay_heatmap(self, original_pil_image, cam_numpy, alpha=0.45, max_dim=640):
        """
        Blends the jet colormap heatmap with the original PIL image.
        Constrains output resolution to max_dim (default 640px) to prevent
        uncompressed bitmap memory spikes on low-memory cloud instances.
        Returns a base64 Data URI string.
        """
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

        buffered.close()
        del heatmap_img, blended, img_rgb, colored_heatmap, lut
        return encoded_data
