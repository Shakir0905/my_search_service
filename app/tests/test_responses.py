# app/tests/test_responses.py
from app.responses import clean_up_response

def test_clean_up_response():
    response_text = "This is a test sentence. Here is another one. And a third one for good measure."
    cleaned_text = clean_up_response(response_text)
    assert cleaned_text.count('.') == 2  
    assert "test sentence" in cleaned_text
    assert "another one" in cleaned_text
    assert "third one" in cleaned_text
