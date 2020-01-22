import re
import requests
from bs4 import BeautifulSoup

google_url = 'https://www.google.com'
daily_monitor_url = 'https://www.monitor.co.ug'
search_url = '/search'
get_google_url = requests.get(google_url)
what_to_search = 'daily monitor uganda'
what_to_search_dict = {'q': what_to_search}
sample = requests.get(google_url + search_url, params = what_to_search_dict)

regex_for_url = R'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

urls_from_search = (re.findall(regex_for_url, sample.text))
get_daily_monitor = requests.get(daily_monitor_url)
source_html = get_daily_monitor.text

search_result = BeautifulSoup(sample.text, 'html.parser')
all_links_in_search_result = (search_result.find_all('a'))

print(search_result(href=re.compile(daily_monitor_url)))