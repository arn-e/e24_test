import os.path
import parse_varnish
import parse_rss
import parse_json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def default_index():  
    varnish_handler = parse_varnish.VarnishDataHandler()
    rss_handler = parse_rss.RssDataHandler()
    json_handler = parse_json.JsonDataHandler()

    top_5_hosts, top_5_files, top_file_map = varnish_handler.top_5_hosts_and_files()
    sorted_rss = rss_handler.sorted_rss()
    sorted_json = json_handler.sorted_json()

    return render_template('index.html', 
        top_5_hosts=top_5_hosts, 
        top_5_files=top_5_files,
        sorted_rss=sorted_rss,
        sorted_json=sorted_json,
        top_file_map=top_file_map)

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()
