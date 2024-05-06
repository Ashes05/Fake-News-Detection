#pip install flask nltk
from flask import Flask, render_template, request
from flask_cors import CORS
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import os
import re
import pickle
import pandas as pd
import numpy as np

#Looks for all the files in same directory so we aren't sending stuff around, not sure if this is convenient or good but for now it might have to do
app = Flask(__name__, static_url_path='', static_folder='.', template_folder='.')
CORS(app)
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
    consts = rf_model.predict_proba(test_features)
    max_prob_index = np.argmax(consts)
    max_prob = consts[0][max_prob_index]

    return samplePred,max_prob

def scraper(url):
    from bs4 import BeautifulSoup
    import requests
    import re

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    def paragraphmaker_id(elementtype, selector):
        main_article = soup.find(elementtype, id=selector)
        return main_article.find_all('p')
    
    def paragraphmaker_class(elementtype, selector):
        main_article = soup.find(elementtype, class_=selector)
        return main_article.find_all('p')
    
    if(re.search("https://www.thejournal.ie/", url)):
        main_article_paragraphs = paragraphmaker_id('div','main-content-wrapper')
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])
        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.rte.ie/", url)):
        main_article = soup.find('article', class_='rte-article article-pillar-news document')
        main_article_paragraphs = main_article.find_all('p')

        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])

        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.irishtimes.com/", url)):
        main_article = soup.find('article', class_='default__ArticleBody-sc-1nhbny4-2 kWWtWa article-body-wrapper article-sub-wrapper')
        main_article_paragraphs = main_article.find_all('p')

        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])

        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.irishexaminer.com/", url)):
        main_article = soup.find('story')
        main_article_paragraphs = main_article.find_all('p')

        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])

        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.breakingnews.ie/", url)):
        main_article = soup.find('article')
        main_article_paragraphs = main_article.find_all('p')
        
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])

        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://edition.cnn.com/", url)):
        main_article = soup.find('div', class_='article__content-container')
        main_article_paragraphs = main_article.find_all('p')
        
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])

        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.foxnews.com/", url)):
        main_article = soup.find('div', class_='article-body')
        main_article_paragraphs = main_article.find_all('p')
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])

        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.nbcnews.com/", url)):
        main_article_paragraphs = paragraphmaker_class('div','article-body__content')      
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])
        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://abcnews.go.com/", url)):
        main_article_paragraphs = paragraphmaker_class('div','theme-e FITT_Article_main__body oBTii mrzah')
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])
        push,prob = prediction(paragraph)
        return push,prob
    elif(re.search("https://www.newsmax.com/", url)):
        main_article_paragraphs = paragraphmaker_id('div','mainArticleDiv')
        paragraph = '\n'.join([paragraph.text for paragraph in main_article_paragraphs])
        push,prob = prediction(paragraph)
        return push,prob
    else:
        news = soup.findAll("p")
        
        for new in news:
            print(new.text)
        
        



@app.route('/',methods =['GET','POST'])
def base():
    if request.method == 'POST':
        text = request.form['text']
        push,prob = prediction(text)
        prob = prob*100
        push = ''.join(push) # Returns FALSE
        return render_template('FakeNew.html',push = push,prob = prob)
    return render_template('FakeNew.html')


@app.route('/data', methods=['POST'])
def handle_data():
    # Retrieve the JSON data from the request body
    data = request.json
    
    # Process the data as needed
    url = data.get('url')
    push,prob = scraper(url) #Runs scraper method 
    prob = prob*100
    push = ''.join(push) # Returns FALSE

    # Optionally, you can return a response to the client
    return render_template('FakeNew.html',push = push,prob = prob)

if __name__ == "__main__":
    app.run(host = '0.0.0.0')

#Testing
#text = "Hello, there folks today we are going to contribute contribution contributed like likes likely liked i dont care anymore!!!"
#prediction(text)
