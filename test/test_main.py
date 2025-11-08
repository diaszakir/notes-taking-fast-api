from fastapi import testclient
from starlette import status
from ..main import app

client = testclient(app)

def test_api():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK