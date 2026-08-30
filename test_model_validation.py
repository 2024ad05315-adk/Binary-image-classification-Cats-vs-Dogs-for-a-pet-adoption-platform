"""Model validation tests"""

import pytest
import torch
from pathlib import Path
from src.model import SimpleCNN

class TestSimpleCNN:
    def test_model_creation(self):
        model = SimpleCNN(num_classes=2)
        assert model is not None
    
    def test_forward_pass(self):
        model = SimpleCNN(num_classes=2)
        dummy_input = torch.randn(1, 3, 224, 224)
        output = model(dummy_input)
        assert output.shape == (1, 2)
    
    def test_parameter_count(self):
        model = SimpleCNN(num_classes=2)
        params = sum(p.numel() for p in model.parameters())
        assert params > 0
