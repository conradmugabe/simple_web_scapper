import requests
import re
import functions


google_url = 'https://www.google.com'
website = requests.get(google_url)
urls = functions.readFile('sites_to_scrape.txt')
for url in urls:
    results_from_search = requests.get('https://www.google.com/search', params={'q': url.rstrip().replace(' ', '+')})
    url_json = results_from_search.json()
    repository = url_json['items'][0]
    print(f'Repository name: {repository["name"]}')
    print(f'Repository description: {repository["description"]}')
