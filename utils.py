"""Utilities for data preprocessing and model operations"""

import torch
import numpy as np
from PIL import Image
from torchvision import transforms

def preprocess_image(image_path, size=(224, 224)):
    """Preprocess image for model input"""
    transform = transforms.Compose([
        transforms.Resize(size),
        transforms.CenterCrop(size),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    image = Image.open(image_path).convert('RGB')
    return transform(image).unsqueeze(0)

def get_model_device():
    """Get device (cuda or cpu)"""
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')
