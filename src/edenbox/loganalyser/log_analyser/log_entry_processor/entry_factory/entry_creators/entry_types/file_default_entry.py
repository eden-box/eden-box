#!/usr/bin/env python3.7

from .default_entry import _DefaultEntry as DefaultEntry


class FileDefaultEntry(DefaultEntry):
    """
    Generated when no file entry is identified
    """

    def dispatch(self, db_cursor):
        pass
