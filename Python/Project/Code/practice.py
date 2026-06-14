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
df = pd.read_csv('./Code/spam.csv',encoding='latin1')

pd.set_option('display.max_columns',None)
pd.set_option('display.expand_frame_repr', True)
pd.set_option('max_colwidth' ,None)

df = df.rename(columns={'v1' : 'category','v2': 'text'})
df = df[['text','category']]

df.isnull().sum()

class_distribution = df['category'].value_counts()


fig,ax = plt.subplots(figsize = (6,6))

ax.bar(class_distribution.index[0],class_distribution.values[0],color = 'Green' , label  = 'Ham')

ax.bar(class_distribution.index[1],class_distribution.values[1],color = 'Red',label = 'Spam')

ax.set_title('Class Distribution of Ham vs spam')
ax.set_xlabel('category')
ax.set_ylabel('frequency')

ax.legend(loc = 'upper right')
# plt.show()

text_corpus = " ".join(df['text'])

wordcloud = WordCloud(width=800 ,height=400,random_state=42,background_color='black').generate(text_corpus)

plt.figure(figsize=(10,6))
plt.imshow(wordcloud,interpolation='bilinear')

plt.axis('off')
plt.title('Word Cloud for english')
plt.show()

stop = set(stopwords.words('english'))
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation and non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.split(" ")
    
    text = [x for x in text if x not in stop]
    return " ".join(text)

df['cleaned_text'] = df['text'].apply(preprocess_text)

newdf = df[['category','cleaned_text']]

# print(newdf)

X_train, X_test, y_train, y_test = train_test_split(
    newdf['cleaned_text'], 
    newdf['category'], 
    test_size=0.2, 
    random_state=42
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
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Reds', xticklabels=['Spam', 'Ham'], yticklabels=['Spam', 'Ham'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()


# print(df[['text','cleaned_text']].head(6))
# print(df[['cleaned_text','text']])
# print(df.index)
# text_corpus = text_corpus.lower()

# text2 = re.sub(r'[^a-zA-Z0-9/s]' , ' ' , text_corpus)
# text2 = text2.split(" ")

# text1 = [i for i  in text2 if i not in stop_words]
# # print(text1)

