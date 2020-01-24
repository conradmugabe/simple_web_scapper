import re
import requests
from bs4 import BeautifulSoup

google_url = 'https://www.google.com'
daily_monitor_url = R'https://www.monitor.co.ug'
search_url = '/search'

get_google_url = requests.get(google_url)
what_to_search = 'facebook'
what_to_search_dict = {'q': what_to_search}
sample = requests.get(google_url + search_url, params = what_to_search_dict)

url_from_search_result = re.findall(daily_monitor_url, sample.text)

get_daily_monitor_url = requests.get(url_from_search_result[0])

regex_url = R'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

regex_url_html = R'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

python_url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

search_urls = (re.findall(python_url_regex, sample.text))
interested_url = ''.join(search_urls[2])
if '<' in interested_url:
    print(interested_url[0:interested_url.index('<')])
else:
    print(interested_url)
