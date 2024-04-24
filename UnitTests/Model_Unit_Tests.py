import unittest
import pickle
from scipy.sparse import hstack
import pandas as pd
import numpy as np
import sys
from TextPreprocess import preprocessText #Copied into unit testing folder


class TestPreprocessText(unittest.TestCase):
    #Testing preprocessing of shorter text
    def test_text_process(self):
        testText = "This is a test $sentEnce with <b>HTML tags</b> and some special characters!*% It will be prePROcEssed."
        self.assertEqual(preprocessText(testText), "test sentence html tag special character preprocessed")

class TestModel(unittest.TestCase):
    #Testing the models
    def test_model(self):
        #Change to most recent models and vectorizers
        #Load models
        sentiment_model = pickle.load(open('TrainedModels/SentimentAnalysisModel_V1.pkl', 'rb'))
        sentiment_vectorizer = pickle.load(open('TrainedModels/sentimentVectorizer_V1.pkl', 'rb'))
        fakeNews_model = pickle.load(open('TrainedModels/FakeNewsModel_V2.pkl', 'rb'))
        fakeNews_vectorizer = pickle.load(open('TrainedModels/fakeNewsVectorizer_V1.pkl', 'rb'))

        #Load test text
        filePath = 'UnitTests/modelTestText.txt' #A labelled FAKE news article taken from another dataset

        with open(filePath, 'r', encoding= 'utf-8') as file:
            test_text = file.read()

        #Preprocess text
        preprocessedText = preprocessText(test_text)

        #Get sentiment
        sentiment_sampleText = sentiment_vectorizer.transform([preprocessedText]) #Vectorize text for sentiment model
        sentiment_Label = sentiment_model.predict(sentiment_sampleText) #Predict text sentiment


        fakeNews_sampleText = fakeNews_vectorizer.transform([preprocessedText]) #Vectorize text for fake news model

        features = hstack([fakeNews_sampleText, sentiment_Label]) #Stack text and sentiment 

        samplePrediction = fakeNews_model.predict(features) #Predict wether news is real or fake, using text and sentiment
        

        self.assertEqual(samplePrediction[0], 'FAKE') #Assert

            
if __name__ == '__main__':
    unittest.main()


