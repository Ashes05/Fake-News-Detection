# Fake-News-Detection
TextPreprocess.py - 
    Has two functions for preprocessing text, one for a full dataset, the other for a 
    single text file.
    It Removes special characters and any HTML tags that might be present from copying and pasting, converts text to lowercase, removes stop words, and lemmatizes the words.

RandomForest_FakeNews.ipynb - 
    Goes through step by step creation of a random forest model for classifying text as
    either real or fake news. 
    - Text Preprocessing (using TextPreprocess.py)
    - Splitting data into training and testing
    - Vectorizing data using a TFIDF Vectorizer
    - Training a Random Forest Classifier Model
    - Accuracy metrics
    - Testing other texts (Test_Text.txt)
    - Saving the model using Pickle
    
Combined_RF_and_SVM.ipynb - 
    Combines a random forest model and a support vector machine using soft voting which allows us to reap the benefits of both algorithms.
    Also compares different types of vectorizers.


Test_Text.txt - 
    Copy and paste an external article into this file to predict wether it is real/fake in RandomForest_FakeNews.ipynb

*Model*.pkl - 
    Pickle files containing trained models

    (14/03/2024) V1 - Random forest model without sentiment analysis
