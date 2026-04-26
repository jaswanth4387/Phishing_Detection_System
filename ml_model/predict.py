import pickle

# Load model once
with open('ml_model/model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('ml_model/model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)


def predict_url(url):
    vector = vectorizer.transform([url])
    result = model.predict(vector)[0]

    return "Phishing URL" if result == 1 else "Legitimate URL"