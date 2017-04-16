import feedparser
import pprint
from dateutil import parser

pp = pprint.PrettyPrinter(indent=4)
feed_url = "http://www.vg.no/rss/feed/forsiden/?frontId=1"

class RssDataHandler:

    def read_rss_feed(self, url):
        raw_feed = feedparser.parse(url)
        return raw_feed

    def sort_rss_feed(self, rss_feed):                    
        sorted_feed = sorted(
            rss_feed['items'],
            key=lambda item: parser.parse(item['published']),
            reverse=True
        )
        return sorted_feed

    def handle_missing_title(self, rss_feed):
        for i in rss_feed:
            if not i['title'] or i['title'].isspace():
                i['title'] = i['link']
        return rss_feed

    def trim_rss_feed(self, rss_data):
        trimmed_rss = []
        for i in rss_data:
            rss_item = {}
            rss_item['title'] = i['title']
            rss_item['link'] = i['link']
            rss_item['published'] = i['published']        
            trimmed_rss.append(rss_item)
        return trimmed_rss

    def sorted_rss(self):
        rss_feed = self.read_rss_feed(feed_url)
        sorted_feed = self.sort_rss_feed(rss_feed)        
        return self.trim_rss_feed(self.handle_missing_title(sorted_feed))
        

# tmp = RssDataHandler()
# foo = tmp.sorted_rss()

# for i in foo:
#     print i['published']