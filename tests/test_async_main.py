import json
import pytest

from httpx import AsyncClient


@pytest.mark.anyio
async def test_read_main():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == ['Connect']


@pytest.mark.anyio
async def test_read_tracks():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/api/musics/list", params={"page": 1, "limit": 30})
        assert response.status_code == 200
        assert len(response.json()["tracks"]) == 30


@pytest.mark.anyio
async def test_read_search_tracks():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/api/musics/search", params={"name": "Halo", "artist": ""})
        assert response.status_code == 200
        assert response.json()["track"][0]["artist"]["name"] == "Beyoncé"


@pytest.mark.anyio
async def test_user_auth():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        headers = {"Content-Type": 'application/x-www-form-urlencoded'}
        response = await ac.post("/api/user/login",
                                 data={"username": "testuser", "password": "Test1234!"}, headers=headers)
        assert response.status_code == 200
        token = response.json()["access_token"]
        assert token is not None
        # profile get test
        response = await ac.get("/api/user/profile", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        assert response.json()["email"] == "user@example.com"
