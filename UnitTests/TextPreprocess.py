# Code reformatted from TextCleaning.ipynb
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocessDataset(dataset, textColumn):
    '''This function is used to preprocess text from a given dataset (textColumn 
    is the title of the column in the dataset containing the text we want to process). It Removes
    special characters and any HTML tags that might be present from copying and pasting, 
    converts text to lowercase, removes stop words, lemmatizes the words, and returns a string for each
    document contained within the dataset'''
    # Removal of Special Characters
    processedSet = dataset[textColumn].apply(lambda x: re.sub(r'<.*?>', '', x))

    processedSet = processedSet.apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

    # Convert to Lower Case
    processedSet = processedSet.apply(lambda x: x.lower())

    # Remove Stop Words
    stop_words = set(stopwords.words('english'))
    processedSet = processedSet.apply(lambda x: [word for word in x.split() if word not in stop_words])

    # Lemmatization
    # Lemmatization solves the problem we were getting with stemming, where words had a chance
    # of becoming invalid, as stemming would just remove the last few letters of certain words.
    # Lemmatization stems words, but ensures that the resulting words are valid words in the dictionary.
    lemmatizer = WordNetLemmatizer()
    processedSet = processedSet.apply(lambda x: [lemmatizer.lemmatize(word) for word in x])

    # Joining individual words back into strings
    # Vectorizer will tokenise words
    finalText = processedSet.apply(lambda x:  ' '.join(x))

    return finalText

def preprocessText(text):
    '''This function is used to preprocess a given piece of text. It Removes
    special characters and any HTML tags that might be present from copying and pasting, 
    converts text to lowercase, removes stop words, lemmatizes the words, and returns a string'''
    # Removal of Special Characters
    processedText = re.sub(r'<.*?>', '', text)

    processedText = re.sub(r'[^a-zA-Z0-9\s]', '', processedText)

    # Convert to Lower Case
    processedText = processedText.lower()

    # Remove Stop Words
    stop_words = set(stopwords.words('english'))
    processedText = [word for word in processedText.split() if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    processedText = [lemmatizer.lemmatize(word) for word in processedText]

    # Joining individual words back into a string
    # Vectorizer will tokenise words
    finalText = ' '.join(processedText)

    return finalText

