import pytest
from app import app  # Ensure 'app' is the Flask app instance from your script

def test_app_running():
    """
    Test if the Flask app is running and responding to a basic route.
    """
    # Use Flask's test client
    client = app.test_client()
    response = client.get("/")  # Test the home route

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"