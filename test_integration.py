"""Integration tests for MLOps API"""

import pytest
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestHealthEndpoint:
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

class TestModelInfoEndpoint:
    def test_model_info(self):
        response = client.get("/model-info")
        assert response.status_code == 200
        data = response.json()
        assert "model_loaded" in data
        assert "model_type" in data

class TestPredictionEndpoint:
    def test_prediction_missing_file(self):
        response = client.post("/predict")
        assert response.status_code in [400, 422]
