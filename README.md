# FastAPI and Elasticsearch Document Service

This project is a HTTP REST service developed using FastAPI and connected to Elasticsearch, allowing storage, retrieval, and search of documents, along with generating responses using the GPT-2 model.

## Technologies

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **Elasticsearch**: A distributed, RESTful search and analytics engine.
- **Transformers (Hugging Face)**: A library for working with pre-trained NLP models.

## Getting Started

### Prerequisites

- Python 3.7+
- Elasticsearch
- Git (for cloning the repository)

### Installation and Running Elasticsearch

1. Download and install Elasticsearch from the [official website](https://www.elastic.co/downloads/elasticsearch).
2. Unpack and start Elasticsearch:
   ```bash
   tar -xzf elasticsearch-<version>.tar.gz
   cd elasticsearch-<version>
   ./bin/elasticsearch
   ```

   On Windows:
   ```bash
   .\bin\elasticsearch.bat
   ```

3. Check that Elasticsearch is operational by accessing `http://localhost:9200/`.

### Project Setup

1. Clone the project repository:
   ```bash
   git clone https://github.com/Shakir0905/my_search_service.git
   cd my_search_service
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Unix/MacOS
   .\venv\Scripts\activate   # On Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Use the following command to run the application:
```bash
uvicorn app.main:app --reload
```

### Testing

To test the API, run `test_main.py` which checks the main functions of creating, searching, and responding to documents:
```bash
python3 test_main.py
```

### Using the API

#### Adding a Document

```bash
curl -X POST "http://127.0.0.1:8000/documents/" -H "Content-Type: application/json" -d "{\"id\": \"unique-uuid\", \"text\": \"Your document text.\"}"
```

#### Retrieving a Document by ID

```bash
curl "http://127.0.0.1:8000/documents/{document_id}"
```

#### Searching Documents

```bash
curl "http://127.0.0.1:8000/search/?query=your-query"
```

#### Generating a Response

```bash
curl -X POST "http://127.0.0.1:8000/generate-answer/" -H "Content-Type: application/json" -d "{\"text\": \"Your query text.\"}"
```

### Visual Representation of Service Operation

The screenshot `project_screen.png` demonstrates the running Elasticsearch and FastAPI servers, as well as the output of the test script, confirming the functionality of the service.

## Authors

- **Ramazanov Shakir** - *Initial work* - [ramazanovshakir9@gmail.com](mailto:ramazanovshakir9@gmail.com)
