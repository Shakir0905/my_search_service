# app/tests/test_main.py
import pytest
import requests
import uuid

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture
def session():
    return requests.Session()

def test_create_document(session):
    document_id = str(uuid.uuid4())
    response = session.post(f"{BASE_URL}/documents/", json={"id": document_id, "text": "Тестовый документ"})
    assert response.status_code == 200
    assert "status" in response.json()

def test_read_document(session):
    document_id = str(uuid.uuid4())
    session.post(f"{BASE_URL}/documents/", json={"id": document_id, "text": "Тестовый документ"})
    response = session.get(f"{BASE_URL}/documents/{document_id}")
    assert response.status_code == 200
    assert "text" in response.json()

def test_search_documents(session):
    response = session.get(f"{BASE_URL}/search/", params={"query": "Тестовый"})
    assert response.status_code == 200
    assert "results" in response.json()
