# app/tests/test_elastic_client.py
import pytest
from unittest.mock import MagicMock, patch
from app.elastic_client import ElasticClient

@pytest.fixture
def elastic_client():
    return ElasticClient()

def test_index_document(elastic_client):
    with patch.object(elastic_client.client, 'index', return_value={"result": "created"}):
        result = elastic_client.index_document("documents", "test_id", {"text": "test"})
        assert result["result"] == "created"

def test_get_document(elastic_client):
    with patch.object(elastic_client.client, 'get', return_value={"_source": {"text": "test"}}):
        result = elastic_client.get_document("documents", "test_id")
        assert result["_source"]["text"] == "test"

def test_search_documents(elastic_client):
    with patch.object(elastic_client.client, 'search', return_value={"hits": {"hits": [{"_id": "1", "_source": {"text": "test"}}]}}):
        result = elastic_client.search_documents("documents", "test")
        assert len(result["hits"]["hits"]) == 1
        assert result["hits"]["hits"][0]["_source"]["text"] == "test"

def test_document_exists(elastic_client):
    with patch.object(elastic_client.client, 'exists', return_value=True):
        result = elastic_client.document_exists("documents", "test_id")
        assert result is True
