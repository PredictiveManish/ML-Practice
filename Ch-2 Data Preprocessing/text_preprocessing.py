import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
# Sample text data
corpus = [
    'This is a positive example',
    'I love working with Machine Learning.',
    'Text data pre-processing is important for ML',
    'Negative examples can be challenging too.',
    'Machine Learning models learn from data.'
]
# Corresponding labels (0 for negative, 1 for positive)

labels = [1,1,1,0,1]

X_train, X_test, y_train, y_test = train_test_split(corpus, labels, test_size=0.2, random_state=42)

# Text vectorization using Bag-of-words (Count Vectorizer)
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectoriezd = vectorizer.transform(X_test)

# Train a simple classifier (Naive Bayes in this case)

classifier = MultinomialNB()
classifier.fit(X_train_vectorized,y_train)

# Make predicitons on the test set
predictions = classifier.predict(X_test_vectoriezd)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Results print
print(f"\nAccuracy: {accuracy:.2f}")
print(f"\nClassification Report: \n{report}")