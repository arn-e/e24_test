import json
import urllib
import pprint
import locale
from datetime import datetime

pp = pprint.PrettyPrinter(indent=4)
locale.setlocale(locale.LC_ALL, 'no_NO')

class JsonDataHandler:

    def read_json(self,url):
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        return data

    def sort_json_by_date(self,json_data):
        sorted_json = sorted(
            json_data, 
            key=lambda item: datetime.strptime(item['date'], '%d %B %Y'), 
            reverse=True)
        return sorted_json

    def sorted_json(self):
        raw_json_data = self.read_json('http://static.e24.no/testfeed.json')
        json_sorted_by_date = self.sort_json_by_date(raw_json_data)
        return json_sorted_by_date

# tmp = JsonDataHandler()
# foo = tmp.sorted_json()

# for i in foo:
#     print i['date']
