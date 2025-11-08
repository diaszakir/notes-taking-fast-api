from fastapi.testclient import TestClient
from starlette import status
from main import app

client = TestClient(app)

def test_api():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "success"}