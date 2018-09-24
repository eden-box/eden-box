#!/usr/bin/env python3.7

from .entry import _Entry as Entry


class FileAddedEntry(Entry):
    """
    Generated when a file is added
    """

    def add_to_filter(self, log_filter):
        pass
