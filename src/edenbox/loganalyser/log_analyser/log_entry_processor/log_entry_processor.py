#!/usr/bin/env python3.7

import json


class LogEntryProcessor:

    def process(self, args):
        log_filter = args[0]
        entry = args[1]
        data = json.loads(entry)
        print(data)
        log_filter.process(data)
