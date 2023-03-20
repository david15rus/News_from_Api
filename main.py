import requests
import os
from send_email import send_email
topic = input('Введите интересующую тематику: ')
API_KEY = os.getenv('Api_key')
url = f'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      f'from=2023-03-19&' \
      f'language=ru&' \
      f'sortBy=publishedAt&' \
      f'apiKey={API_KEY}'

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
message = "Subject: Новости на сегодня \n"

# Access the article titles and description
for article in content['articles']:
    message += article['title'] + '\n'
    message += article['description'] + '\n'
    message += article['url'] + 2*'\n'

send_email(message.encode('utf-8'))
