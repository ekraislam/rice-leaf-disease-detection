import torch

def save_resume_state(state: dict, path: str) -> None:
    """Save GAN training resume state containing epoch, generator, discriminator, and optimizer states."""
    torch.save(state, path)

def load_resume_state(path: str, device: torch.device) -> dict:
    """Load resume state and map tensors to the given device."""
    return torch.load(path, map_location=device)
