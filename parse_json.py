import json
import urllib
import pprint
import locale
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)
locale.setlocale(locale.LC_ALL, 'no_NO')

def read_json(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

def sort_json_by_date(json_data):
    sorted_json = sorted(json_data, key=lambda item: datetime.strptime(item['date'], '%d %B %Y'), reverse=True)
    return sorted_json

raw_json_data = read_json('http://static.e24.no/testfeed.json')
json_sorted_by_date = sort_json_by_date(raw_json_data)

for i in json_sorted_by_date:
    print i['date']
