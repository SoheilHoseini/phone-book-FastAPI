from fastapi.testclient import TestClient
from main import app
import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_root2():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Narvan Phone Book App :)"}



client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Narvan Phone Book App :)"}


def test_inexistent_contact():
    response = client.get("/find/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "No such a contact found"}


def test_existng_contact():
    response = client.get("/find/fatemeh")
    assert response.status_code == 404
    assert response.json() == {"detail": "No such a contact found"}

@pytest.mark.anyio
async def test_existng_contact2():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/find/fatemeh")
    # assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Narvan Phone Book App :)"}


