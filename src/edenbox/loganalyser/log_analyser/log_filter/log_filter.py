#!/usr/bin/env python3.7

from log_analyser.log_filter import _Filter as Filter


class LogFilter(Filter):

    filters = []
    log_entries = []
    process_limit = 100  # TODO choose a good limit and extract value to config file

    def __init__(self, file):
        self.file = file

    def add_filter(self, filter_part):
        self.filters.append(filter_part)

    def filter(self, log_entry):
        self.log_entries.append(log_entry)

    def process(self):

        # verification used to minimize impact of webcrawler fake access
        if len(self.log_entries) < self.process_limit:
            for entry in self.log_entries:
                for log_filter in self.filters:
                    log_filter.filter(entry)

        self.filters.clear()
