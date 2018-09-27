#!/usr/bin/env python3.7

from .entry import _Entry as Entry


class FileAccessEntry(Entry):
    """
    Generated when a file is accessed
    """

    def add_to_filter(self, log_filter):
        pass
