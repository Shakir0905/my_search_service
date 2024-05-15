# app/elastic_client.py
import os
from elasticsearch import Elasticsearch, exceptions

class ElasticClient:
    def __init__(self):
        self.client = Elasticsearch(
            [os.getenv('ELASTIC_HOST', 'https://localhost:9200')],
            http_auth=(os.getenv('ELASTIC_USER', 'elastic'), os.getenv('ELASTIC_PASS', 'password')),
            verify_certs=False
        )
    
    def index_document(self, index, doc_id, document):
        return self.client.index(index=index, id=str(doc_id), body=document)
    
    def get_document(self, index, doc_id):
        return self.client.get(index=index, id=str(doc_id))
    
    def search_documents(self, index, query, size=3):
        body = {"size": size, "query": {"match": {"text": query}}}
        return self.client.search(index=index, body=body)
    
    def document_exists(self, index, doc_id):
        return self.client.exists(index=index, id=str(doc_id))
