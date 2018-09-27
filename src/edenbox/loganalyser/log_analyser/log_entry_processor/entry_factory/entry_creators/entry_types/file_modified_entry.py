#!/usr/bin/env python3.7

from .entry import _Entry as Entry


class FileModifiedEntry(Entry):
    """
    Generated when a file is modified
    """

    def add_to_filter(self, log_filter):
        pass
