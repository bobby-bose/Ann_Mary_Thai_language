import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

train_data = pd.read_csv('train_5500.label.txt', sep=':',encoding='ISO-8859-1',on_bad_lines='skip',names=['label','text'])
test_data = pd.read_csv('test_5500.label.txt', sep=':',encoding='ISO-8859-1',on_bad_lines='skip',names=['label','text'])
def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if not token in stop_words]
    processed_text = ' '.join(tokens)
    return processed_text

train_data['text'] = train_data['text'].apply(preprocess_text)
test_data['text'] = test_data['text'].apply(preprocess_text)
print(train_data.head())
print(test_data.head())
train_data['text'] = train_data['text'].apply(preprocess_text)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(train_data['text'])
y = train_data['label']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
nb = MultinomialNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_val)
print("Accuracy:", accuracy_score(y_val, y_pred))
print("Classification Report:\n", classification_report(y_val, y_pred))
# Test the model on a new sentence
sentence = "what is the full form of com?"
sentence = preprocess_text(sentence)
sentence = vectorizer.transform([sentence])
prediction = nb.predict(sentence)
print("Prediction:", prediction[0])


