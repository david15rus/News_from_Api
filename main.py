import requests
import os
from send_email import send_email

API_KEY = os.getenv('Api_key')
url = f'https://newsapi.org/v2/everything?q=russia&' \
      f'from=2023-02-19&language=ru&' \
      f'sortBy=publishedAt&apiKey={API_KEY}'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
message = ''

# Access the article titles and description
for article in content['articles']:
    message += article['title'] + '\n'
    message += article['description'] + '\n'
    message += article['source']['name'] + 2*'\n'

send_email(message.encode('utf-8'))
