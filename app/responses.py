# app/responses.py
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_up_response(response_text):
    vectorizer = TfidfVectorizer()
    try:
        sentences = response_text.split('. ')
        tfidf_matrix = vectorizer.fit_transform(sentences)
        importance_scores = tfidf_matrix.sum(axis=1).A1
        top_sentences = [sentences[i] for i in importance_scores.argsort()[-3:]]
        return '. '.join(top_sentences)
    except Exception as e:
        print(f"Error processing text: {e}")
        return response_text
