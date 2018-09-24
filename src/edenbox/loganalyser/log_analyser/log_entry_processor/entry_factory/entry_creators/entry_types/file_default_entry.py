#!/usr/bin/env python3.7

from .entry import _Entry as Entry


class FileDefaultEntry(Entry):
    """
    Generated when no file entry is identified
    """

    def add_to_filter(self, log_filter):
        pass
