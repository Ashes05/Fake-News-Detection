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

#Looks for all the files in same directory so we aren't sending stuff around, not sure if this is convenient or good but for now it might have to do
app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')

#programDirectory = "C:/user/documents/Project/app.py"
programDirectory = os.path.abspath(os.path.dirname(__file__))


with open('FakeNewsModel_V1.pkl', 'rb') as file:
    rf, tfidf_vectorizer = pickle.load(file)


#Process data sets
def preprocessDataset(dataset,textColumn):
    review = dataset[textColumn].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))
    review = review.apply(lambda x: x.lower())
    stop_words = set(stopwords.words('english'))
    processedSet = review.apply(lambda x: [word for word in x.split() if word not in stop_words])
    processedSet = processedSet.apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
    finalText = processedSet.apply(lambda x:  ' '.join(x))
    return finalText

def prediction(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower().split()
    stemmedReview = []

    for word in review:
        if word not in stopwords.words('english'):
            temp = lemmatizer.lemmatize(word)
            stemmedReview.append(temp)

    document = ' '.join(stemmedReview)
    temp = tfidf_vectorizer.transform([document])
    prediction = rf.predict(temp)

    return prediction



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
