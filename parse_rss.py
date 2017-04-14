import feedparser
import pprint

pp = pprint.PrettyPrinter(indent=4)
feed_url = "http://www.vg.no/rss/feed/forsiden/?frontId=1"

def read_rss_feed(url):
    raw_feed = feedparser.parse(url)
    return raw_feed

def sorted_rss_feed(rss_feed):
    sorted_feed = sorted(rss_feed['items'], key=lambda item: item['published'], reverse=True)
    return sorted_feed

rss_feed = read_rss_feed(feed_url)
sorted_feed = sorted_rss_feed(rss_feed)

for i in sorted_feed:
    # print i['title']
    # print i['link']
    print i['published']