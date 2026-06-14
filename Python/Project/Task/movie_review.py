# from urduhack.preprocessing import (
#     normalize_whitespace,
#     remove_punctuation,
#     normalize_urdu,
#     remove_accents,
#     replace_urls,
#     replace_emails,
#     replace_numbers,
#     replace_phone_numbers
# )
# from urduhack.tokenization import word_tokenizer
from sklearn.pipeline import Pipeline

import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import nltk
from nltk.corpus import stopwords
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# sentiment analysis of urdu movies reviews

df = pd.read_csv('task.csv',encoding='utf-8')
# print(df)
pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr', True)
pd.set_option('max_colwidth' ,None)

# print(df.columns)
# print()

def remove_punctuation_urdu(text):
    # Remove Urdu/English punctuation except spaces and periods
    return re.sub(r'[^\w\s۔]+', '', text)


# text = remove_punctuation_urdu(singleString)
# # Output: "کیا حال ہے Hello"
# print(newdf)

def normalize_whitespace(text):
    return ' '.join(text.split())


# clean_text = normalize_whitespace(text)
# Output: "یہ ایک ٹیسٹ ہے"
#cleantext is taken as another variable

def replace_entities(text):
    text = re.sub(r'http\S+', '[URL]', text)  # URLs
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)  # Emails
    text = re.sub(r'\d+', '[NUMBER]', text)  # Numbers
    return text

urdu_stopwords = set(["اور", "لیکن", "تھا", "تھی", "تھے", "ہے", "ہیں", "کو", "میں"])

def remove_urdu_stopwords(text):
    words = text.split()
    return ' '.join([word for word in words if word not in urdu_stopwords])

def tokenize_urdu(text):
    # Split on spaces and Urdu-specific punctuation (۔،؟)
    return re.findall(r'[\w]+|[۔،؟]', text)


# tokens = tokenize_urdu(clean_text)
# print(tokens)


def clean_urdu_text(text):
    text = remove_punctuation_urdu(text)
    text = normalize_whitespace(text)
    text = replace_entities(text)
    text = remove_urdu_stopwords(text)
    # text = tokenize_urdu(text)
    return text

# Example

# clean_text = clean_urdu_text(singleString)
# print(clean_text)

# newdf1 = df[['sentiment','']]
df['clean_text'] = df['review'].apply(clean_urdu_text)

# newdf = df[['clean_text' , 'sentiment']]
# print(newdf[['clean_text','sentiment']].head(10))



X_train , X_test ,y_train ,y_test = train_test_split(
    df['clean_text'],
    df['sentiment'],
    test_size = 0.2,
    random_state=42,
    # stratify=df['sentiment']

)
vectorizer = CountVectorizer(ngram_range=(1, 1))  # Extract unigrams, 
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

print(X_train_vectorized.shape)
print(X_test_vectorized.shape)


classifier = MultinomialNB() 
classifier.fit(X_train_vectorized, y_train)

# Make predictions
y_pred = classifier.predict(X_test_vectorized)

# Evaluate the model
# Evaluate the model
report=classification_report(y_test, y_pred)

print(report)
print("############################################################\n")

# # Create pipeline for consistent preprocessing
# # pipeline = Pipeline([
# #     ('vectorizer', CountVectorizer(ngram_range=(1, 2))),  # Using bigrams
# #     ('classifier', MultinomialNB())
# # ])

# # #Train Model
# # pipeline.fit(X_train, y_train)

# # # Evaluate
# # y_pred = pipeline.predict(X_test)
# # # print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Reds',
            xticklabels=['Positive', 'Negative'],
            yticklabels=['Positive', 'Negative'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix for Urdu Sentiment Analysis')
plt.show()
# vectorizer = CountVectorizer(ngram_range=(1,1))

# X_train_vectorized = vectorizer.fit_transform(X_train)

# X_test_vectorized = vectorizer.transform(X_test)

# print(X_train_vectorized.shape)
# print(X_test_vectorized.shape)


# classifier = MultinomialNB() 
# classifier.fit(X_train_vectorized, y_train)

# # Make predictions
# y_pred = classifier.predict(X_test_vectorized)

# # Evaluate the model
# # Evaluate the model
# report=classification_report(y_test, y_pred)

# # print(report)
# print("############################################################\n")

# conf_matrix = confusion_matrix(y_test, y_pred)
# print(conf_matrix)

# plt.figure(figsize=(8, 6))
# sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Reds', xticklabels=['Positive', 'Negative'], yticklabels=['Positive', 'Negative'])
# plt.xlabel('Predicted Label')
# plt.ylabel('True Label')
# plt.title('Confusion Matrix')
# plt.show()