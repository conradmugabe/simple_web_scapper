import requests
import re
import functions

website = requests.get('https://www.google.com')
urls = functions.readingAFile('sites_to_scrape.txt')
for url in urls:
    results_from_search = requests.get('https://www.google.com/search', params={'q': url.rstrip().replace(' ', '+')})
    url_json = results_from_search.json()
    repository = url_json['items'][0]
    print(f'Repository name: {repository["name"]}')  # Python 3.6+
    print(f'Repository description: {repository["description"]}')  # Python 3.6+
