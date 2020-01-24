import re
import requests


python_url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

google_url = 'https://www.google.com'

search = R'google'
search_dict = {'q': search}
search_api = '/search'

search_results = requests.get(google_url + search_api, params = search_dict)

urls_in_search = re.findall(python_url_regex, search_results.text)
_likely_option = ''.join(urls_in_search[2])


if '<' in _likely_option:
    site_to_scrape = _likely_option[0:_likely_option.index('<')]
    print(site_to_scrape)
else:
    site_to_scrape = _likely_option
    print(site_to_scrape)