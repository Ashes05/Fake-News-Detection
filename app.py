#pip install flask
from flask import Flask, render_template, request,jsonify
#pip install nltk
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as ps
#Allows us to use files on the device
import os
#Regular Expression
import re

#Looks for all the files in same directory so we aren't sending stuff around, not sure if this is convenient or good but for now it might have to do
app = Flask(__name__,template_folder='.')
#Gives the direct directory to the files we will be using, so rather than hardcoding-
#We just use this to retrieve any files, in short
#programDirectory = "C:/user/documents/Project/app.py"
#Good practice as isn't hardcoding
programDirectory = os.path.abspath(os.path.dirname(__file__))

#NEED TO MAKE OUR OWN MODELS
#Loading in model
#DTCmodel = os.path.join(programDirectory, 'DTCMODEL.pkl')
#TF_IDFmodel = os.path.join(programDirectory, 'TFIDFMODEL.pkl')

#Opening the trained model
#rb represents readbytes
#DTC = pk.load(open(DTCmodel,'rb'))
#TFIDF = pk.load(open(TF_IDFmodel,'rb'))

nltk.download('stopwords')
stemmer = ps()

def prediction(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    stemmedReview = []
    for word in review:
        if word not in stopwords.words('english'):
            temp = stemmer.stem(word)
            stemmedReview.append(temp)
    print(stemmedReview)

#Post is for when we submit(POST) data
#Get is when we are trying to retrieve the data/website
@app.route('/',methods =['GET','POST'])
def base():
    if request.method == 'POST':
        text = request.form['text']
        result = prediction(text)
        return render_template('index.html',result = result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

#Testing
#text = "Hello, there folks today we are going to contribute contribution contributed like likes likely liked i dont care anymore!!!"
#prediction(text)
