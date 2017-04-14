import urllib
from urlparse import urlparse
from collections import Counter

class VarnishDataHandler:
        
    def exclude_non_files(self, full_file_list):
        updated_file_list, excluded = [],['.php', '.js', '.html']

        for i in full_file_list:
            if (not any(word in i for word in excluded)) and ("." in i): 
                updated_file_list.append(i)
        return updated_file_list

    def full_varnish_log_from_web(self, source):
        response = urllib.urlopen(source)
        return response

    def full_varnish_log_from_file(self, source):
        with open(source) as f:
            full_log = input_lines = f.readlines()
        return full_log

    def parsed_host(self, full_path):
        parsed_line = urlparse(full_path)
        parsed_hostname = parsed_line.hostname
        return parsed_hostname

    def parsed_filename(self, full_path):
        parsed_file = full_path.rsplit('/', 1)[1]
        return parsed_file

    def host_and_filename(self, full_varnish_log):
        file_list, host_list = [], []

        for i in full_varnish_log:
            full_path = i.split()[6]
            host_list.append(self.parsed_host(full_path))
            file_list.append(self.parsed_filename(full_path))        

        return file_list, host_list

    def top_results(self, input_list, desired_count):
        to_count = (word for word in input_list)
        counted_items = Counter(to_count)
        return counted_items.most_common(desired_count)

    def top_5_hosts_and_files(self):
        # raw_varnish_log = self.full_varnish_log_from_web('http://tech.vg.no/intervjuoppgave/varnish.log')
        raw_varnish_log = self.full_varnish_log_from_file('varnish.log')
        file_list, host_list = self.host_and_filename(raw_varnish_log)

        top_hosts = self.top_results(host_list, 5)
        top_files = self.top_results(self.exclude_non_files(file_list), 5)

        return top_hosts, top_files
