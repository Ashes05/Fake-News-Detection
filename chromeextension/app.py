
def scraper(url):
    from bs4 import BeautifulSoup
    import requests
    import re

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    
    if(re.search("https://www.thejournal.ie/", url)):
        main_article = soup.find('div', id='main-content-wrapper')
        main_article_paragraphs = main_article.find_all('p')

        for paragraph in main_article_paragraphs[:-2]:
             if(re.search("Read Next", paragraph.text)):
                 continue
             else:
                print(paragraph.text)
    elif(re.search("https://www.rte.ie/", url)):
        main_article = soup.find('article', class_='rte-article article-pillar-news document')
        main_article_paragraphs = main_article.find_all('p')

        for paragraph in main_article_paragraphs:
             print(paragraph.text)
    elif(re.search("https://www.irishtimes.com/", url)):
        main_article = soup.find('article', class_='default__ArticleBody-sc-1nhbny4-2 kWWtWa article-body-wrapper article-sub-wrapper')
        main_article_paragraphs = main_article.find_all('p')

        for paragraph in main_article_paragraphs:
             print(paragraph.text)
    elif(re.search("https://www.irishexaminer.com/", url)):
        main_article = soup.find('story')
        main_article_paragraphs = main_article.find_all('p')

        for paragraph in main_article_paragraphs:
             print(paragraph.text)
    elif(re.search("https://www.breakingnews.ie/", url)):
        main_article = soup.find('div', class_='flex-1 lg:w-1/2')
        main_article_paragraphs = main_article.find_all('p')

        for paragraph in main_article_paragraphs:
             print(paragraph.text)







from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

@app.route('/data', methods=['POST'])
def handle_data():
    # Retrieve the JSON data from the request body
    data = request.json
    
    # Process the data as needed
    url = data.get('url')
    scraper(url) #Runs scraper method 

    
    # Optionally, you can return a response to the client
    return 'Data received successfully'

if __name__ == '__main__':
    app.run(debug=True)
