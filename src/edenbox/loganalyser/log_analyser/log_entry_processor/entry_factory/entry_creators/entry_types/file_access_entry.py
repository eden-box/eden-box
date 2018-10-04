#!/usr/bin/env python3.7

from .default_entry import _DefaultEntry as DefaultEntry


class FileAccessEntry(DefaultEntry):
    """
    Generated when a file is accessed
    """

    def dispatch(self, db_cursor):
        pass
