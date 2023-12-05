import requests as req
import os
import keyboard
import webbrowser
from config import API_KEY

TOPIC = "technology"

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="+TOPIC+"&api-key="+API_KEY+"&page=0"

response = req.get(url).json()

"""
KEYS: 
    'abstract', 
    'web_url', 
    'snippet', 
    'lead_paragraph', 
    'source', 
    'multimedia', 
    'headline', 
    'keywords', 
    'pub_date', 
    'document_type', 
    'news_desk', 
    'section_name', 
    'byline', 
    'type_of_material', 
    '_id', 
    'word_count', 
    'uri'
"""
i = 0

articles = response['response']['docs']

while (i < len(articles))+1:
    os.system('clear')
    if i > len(articles):
        break
    elif i == len(articles):
        print("No more Articles...")
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
            break
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'left':
            i -= 1
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            break
    else:
        print('\n'+articles[i]['headline']['main'])
        print('\n'+articles[i]['lead_paragraph']+'\n')
        print(articles[i]['pub_date'])
        print('Source: ' + articles[i]['source'])
        print('Article link: ' + articles[i]['web_url'])
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'right':
            i += 1
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'left':
            if (i > 0):
                i -= 1
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'enter':
            webbrowser.open(articles[i]['web_url'])
        elif event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            break
