#pip install flask nltk
from flask import Flask, render_template, request
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import os
import re
import pickle
import pandas as pd

#Looks for all the files in same directory so we aren't sending stuff around, not sure if this is convenient or good but for now it might have to do
app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')

#programDirectory = "C:/user/documents/Project/app.py"
programDirectory = os.path.abspath(os.path.dirname(__file__))


with open('Model/TrainedModels/FakeNewsModel_V3.pkl', 'rb') as file:
    rf_model,tfidf_vectorizer_text,tfidf_vectorizer_combined_sentiment = pickle.load(file)

def filter(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    stemmed_review = [word for word in review if word not in stopwords.words('english')]
    text_string = ' '.join(stemmed_review)
    return text_string

def prediction(text):
    text = filter(text)

    tfidf_sampletext = tfidf_vectorizer_text.transform([text])
    tfidf_sentiment = tfidf_vectorizer_combined_sentiment.transform([text])

    test_features = pd.concat([pd.DataFrame(tfidf_sampletext.toarray()), 
                           pd.DataFrame(tfidf_sentiment.toarray())], axis=1)
    samplePred = rf_model.predict(test_features)
    return samplePred



@app.route('/',methods =['GET','POST'])
def base():
    if request.method == 'POST':
        text = request.form['text']
        push = prediction(text)
        return render_template('FakeNew.html',push = push)
    return render_template('FakeNew.html')

if __name__ == "__main__":
    app.run()

#Testing
#text = "Hello, there folks today we are going to contribute contribution contributed like likes likely liked i dont care anymore!!!"
#prediction(text)
