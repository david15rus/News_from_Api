import requests
import os

API_KEY = os.getenv('Api_key')
url = f'https://newsapi.org/v2/everything?q=russia&from=2023-02-19&' \
      f'sortBy=publishedAt&apiKey={API_KEY}'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
      print(article['title'])
