import os
import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 🔹 BASE DIRECTORY
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🔹 DATASET PATH
data_path = os.path.join(BASE_DIR, 'dataset', 'dataset.csv')

# 🔹 LOAD DATA
print("📂 Loading dataset...")
data = pd.read_csv(data_path, encoding='latin-1')

# 🔹 CLEAN COLUMN NAMES (important)
data.columns = data.columns.str.strip()
print("Columns:", data.columns)

# 🔹 CONVERT LABELS (bad/good → 1/0)
def convert_label(x):
    return 1 if str(x).lower() == 'bad' else 0

data['label'] = data['Label'].apply(convert_label)

# 🔹 FEATURES & TARGET
X = data['URL']
y = data['label']

# 🔹 VECTORIZATION (optimized)
print("🔄 Vectorizing...")
vectorizer = CountVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)

# 🔹 TRAIN-TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 MODEL (FAST + EFFECTIVE)
print("🤖 Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🔹 EVALUATION
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy * 100:.2f}%")

# 🔹 SAVE MODEL
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'model', 'vectorizer.pkl')

print("💾 Saving model...")

with open(model_path, 'wb') as f:
    pickle.dump(model, f)

with open(vectorizer_path, 'wb') as f:
    pickle.dump(vectorizer, f)

print("🎉 Training complete! Model saved successfully.")