#!/usr/bin/env python3.7

import json
from .entry_factory import EntryFactory


class LogEntryProcessor:
    """
    Handles log entries conversion from json

    Converts json entries from the log file to objects and forwards them to the log filter
    """

    @staticmethod
    def process(args):
        """
        Converts line from json and passes it to the log filter
        :param args: tuple containing the log line to process and the log filter to which it will be passed to
        """

        log_filter = args[0]
        line = args[1]

        data = json.loads(line)

        entry = EntryFactory().get_entry(data)

        if entry is not None:
            log_filter.filter(entry)
