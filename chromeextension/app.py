
def scraper(url):
    from bs4 import BeautifulSoup
    import requests
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    ptags = soup.findAll("p")
    articletags = soup.findAll("article")   #Selects certain tags in the HTML file
    news =  ptags + articletags

    for new in news:
        print(new.text)

from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
