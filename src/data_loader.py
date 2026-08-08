"""
Rice Leaf Disease Preprocessing & Data Loading Module
Ultra-high speed PyTorch CPU memory-mapped DataLoader.
"""

import os
import random
import numpy as np
from PIL import Image

try:
    import torch
    torch.set_num_threads(max(1, os.cpu_count() // 2))
    HAS_TORCH = True
except Exception:
    HAS_TORCH = False

def set_seed(seed=42):
    """Set random seed for reproducibility across random, numpy, and torch."""
    random.seed(seed)
    np.random.seed(seed)
    if HAS_TORCH:
        try:
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)
        except Exception:
            pass

class RiceLeafDataset:
    """
    Ultra-fast Dataset class for Rice Leaf Disease images.
    Caches preprocessed dataset as contiguous RAM tensors for instant CPU batching.
    """
    def __init__(self, split_dir, target_size=(224, 224), normalize_imagenet=False, preload=True):
        self.split_dir = split_dir
        self.target_size = target_size
        self.normalize_imagenet = normalize_imagenet
        self.preload = preload
        
        if not os.path.exists(split_dir):
            raise FileNotFoundError(f"Split directory not found: {split_dir}")
            
        self.classes = sorted([
            d for d in os.listdir(split_dir)
            if os.path.isdir(os.path.join(split_dir, d))
        ])
        
        self.class_to_idx = {c: i for i, c in enumerate(self.classes)}
        self.idx_to_class = {i: c for i, c in enumerate(self.classes)}
        
        self.samples = []
        self.corrupt_files = []
        
        for c in self.classes:
            c_dir = os.path.join(split_dir, c)
            for fname in sorted(os.listdir(c_dir)):
                fpath = os.path.join(c_dir, fname)
                if os.path.isfile(fpath):
                    self.samples.append((fpath, self.class_to_idx[c]))

        self.tensor_images = None
        self.tensor_labels = None
        
        if self.preload and len(self.samples) > 0:
            imgs = []
            lbls = []
            for idx in range(len(self.samples)):
                img_chw, label = self.load_image_and_label(idx)
                imgs.append(img_chw)
                lbls.append(label)
                
            imgs_np = np.stack(imgs, axis=0) # (N, 3, H, W)
            lbls_np = np.array(lbls, dtype=np.int64) # (N,)
            
            if HAS_TORCH:
                self.tensor_images = torch.from_numpy(imgs_np)
                self.tensor_labels = torch.from_numpy(lbls_np)
            else:
                self.tensor_images = imgs_np
                self.tensor_labels = lbls_np

    def __len__(self):
        return len(self.samples)

    def load_image_and_label(self, idx):
        """Loads single image as preprocessed NumPy array (3, H, W)."""
        fpath, label = self.samples[idx]
        try:
            with Image.open(fpath) as img:
                img = img.convert("RGB")
                img_resized = img.resize(self.target_size, Image.Resampling.BILINEAR)
                img_np = np.array(img_resized, dtype=np.float32) / 255.0
                
                if self.normalize_imagenet:
                    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32).reshape(1, 1, 3)
                    std = np.array([0.229, 0.224, 0.225], dtype=np.float32).reshape(1, 1, 3)
                    img_np = (img_np - mean) / std
                    
                img_chw = np.transpose(img_np, (2, 0, 1))
        except Exception as e:
            img_chw = np.zeros((3, self.target_size[0], self.target_size[1]), dtype=np.float32)
            self.corrupt_files.append((fpath, str(e)))
            
        return img_chw, label

    def __getitem__(self, idx):
        if self.preload and self.tensor_images is not None:
            return self.tensor_images[idx], self.tensor_labels[idx]
        img_chw, label = self.load_image_and_label(idx)
        if HAS_TORCH:
            return torch.from_numpy(img_chw), torch.tensor(label, dtype=torch.long)
        return img_chw, label


class BatchDataLoader:
    """
    Framework-agnostic & PyTorch-optimized DataLoader iterator.
    """
    def __init__(self, dataset, batch_size=32, shuffle=False, seed=42, return_tensor=True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.seed = seed
        self.return_tensor = return_tensor
        self.indices = np.arange(len(dataset))
        self.reset()

    def reset(self):
        if self.shuffle:
            rng = np.random.RandomState(self.seed)
            rng.shuffle(self.indices)

    def __len__(self):
        return (len(self.dataset) + self.batch_size - 1) // self.batch_size

    def __iter__(self):
        self.reset()
        for idx in range(0, len(self.dataset), self.batch_size):
            batch_indices = self.indices[idx:idx + self.batch_size]
            
            if self.dataset.preload and self.dataset.tensor_images is not None:
                # Direct slice from contiguous tensor - zero allocation overhead!
                yield self.dataset.tensor_images[batch_indices], self.dataset.tensor_labels[batch_indices]
            else:
                batch_images = []
                batch_labels = []
                for b_idx in batch_indices:
                    img, label = self.dataset[b_idx]
                    batch_images.append(img)
                    batch_labels.append(label)
                    
                if HAS_TORCH and isinstance(batch_images[0], torch.Tensor):
                    yield torch.stack(batch_images, dim=0), torch.tensor(batch_labels, dtype=torch.long)
                else:
                    batch_images_np = np.stack(batch_images, axis=0)
                    batch_labels_np = np.array(batch_labels, dtype=np.int64)
                    if self.return_tensor and HAS_TORCH:
                        yield torch.from_numpy(batch_images_np), torch.from_numpy(batch_labels_np)
                    else:
                        yield batch_images_np, batch_labels_np


def create_data_loaders(dataset_root, batch_size=32, target_size=(224, 224), seed=42, normalize_imagenet=False, return_tensor=True, preload=True):
    set_seed(seed)
    
    splits = {
        'train': 'Training data',
        'val': 'Validation data',
        'test': 'Testing data'
    }
    
    datasets = {}
    loaders = {}
    
    for split_key, split_folder in splits.items():
        split_path = os.path.join(dataset_root, split_folder)
        ds = RiceLeafDataset(split_path, target_size=target_size, normalize_imagenet=normalize_imagenet, preload=preload)
        datasets[split_key] = ds
        
        is_train = (split_key == 'train')
        
        loaders[split_key] = BatchDataLoader(
            dataset=ds,
            batch_size=batch_size,
            shuffle=is_train,
            seed=seed,
            return_tensor=return_tensor
        )
        
    return loaders, datasets
