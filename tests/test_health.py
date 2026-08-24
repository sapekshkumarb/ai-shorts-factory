"""Tests for health and diagnostics endpoints."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    """Test basic health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OK"
    assert data["version"] == "0.1.0"
    assert "environment" in data
    assert "debug" in data


def test_health_providers():
    """Test provider health endpoint."""
    response = client.get("/health/providers")
    assert response.status_code == 200
    data = response.json()
    assert "overall_status" in data
    assert "providers" in data
    assert isinstance(data["providers"], dict)
    # With defaults, we expect mock providers to be OK
    assert data["overall_status"] in ["OK", "WARNING"]
