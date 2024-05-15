# app/main.py
import uuid
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.elastic_client import ElasticClient
from app.responses import clean_up_response
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from functools import lru_cache

app = FastAPI()
elastic = ElasticClient()
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

class Document(BaseModel):
    id: uuid.UUID
    text: str

@app.post("/documents/")
async def create_document(document: Document):
    res = elastic.index_document("documents", document.id, document.dict())
    return {"status": res['result'], "id": str(document.id)}

@app.get("/documents/{document_id}")
async def read_document(document_id: uuid.UUID):
    if not elastic.document_exists("documents", document_id):
        raise HTTPException(status_code=404, detail="Document not found")
    res = elastic.get_document("documents", document_id)
    return {"id": str(document_id), "text": res['_source']['text']}

@app.get("/search/")
async def search_documents(query: str):
    res = elastic.search_documents("documents", query)
    hits = res['hits']['hits']
    results = [{"id": hit["_id"], "text": hit["_source"]["text"]} for hit in hits]
    return {"query": query, "results": results, "total": len(results)}

@lru_cache(maxsize=100)
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt", max_length=1024, truncation=True)
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
    return tokenizer.decode(output[0], skip_special_tokens=True)

@app.post("/generate-answer/")
async def generate_answer(request: Request):
    data = await request.json()
    query = data.get('text', '')
    res = elastic.search_documents("documents", query, size=5)
    documents_text = " ".join([hit['_source']['text'] for hit in res['hits']['hits']])
    if documents_text:
        generated_text = generate_response(documents_text)
        cleaned_text = clean_up_response(generated_text)
        return {"query": query, "generated_answer": cleaned_text}
    else:
        return {"query": query, "generated_answer": "No relevant documents found to generate an answer."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
