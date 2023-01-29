import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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
