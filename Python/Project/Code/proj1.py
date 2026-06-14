
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('spam.csv', encoding='latin1')

pd.set_option('display.max_columns', None)  

pd.set_option('display.expand_frame_repr', True) 

pd.set_option('max_colwidth',None)  


df = df.rename(columns={'v1': 'category', 'v2': 'text'})
print(df)
newdf=df[['text', 'category']] 

# print(newdf)

# print(newdf['text'].isnull().sum(axis= 0))  #in specfic columns return 0 if value are not null
newdf.isnull().sum()  #check in al dataframe 

# print(newdf.isnull().sum())   

# print(df['category'].value_counts())

class_distribution = newdf['category'].value_counts()

fig,ax = plt.subplots(figsize = (6,6))

ax.bar(class_distribution.index[0],class_distribution.values[0], color = 'green',label = 'ham')

ax.bar(class_distribution.index[1],class_distribution.values[1],color = 'red',label = 'spam')

ax.set_title('Class Distribution of Spam vs Ham')
ax.set_xlabel('category')
ax.set_ylabel('Frequency')

ax.legend(loc = 'upper right')

# plt.show()

text_corpus = ' '.join(newdf['text'])

wordcloud = WordCloud(width=800, height=400,random_state=42,background_color='black').generate(text_corpus)

plt.figure(figsize=(10,5))

plt.imshow(wordcloud,interpolation='bilinear')

plt.axis('off')

plt.title('Word Cloud for English')

plt.show()










# Vectorize the text data with unigrams, bigrams, and trigrams
vectorizer = CountVectorizer(ngram_range=(1, 1))  # Extract unigrams, 
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

print(X_train_vectorized.shape)
print(X_test_vectorized.shape)


from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Initialize and train the classifier
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