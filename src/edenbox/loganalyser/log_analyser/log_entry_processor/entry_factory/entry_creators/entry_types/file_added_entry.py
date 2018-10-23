#!/usr/bin/env python3.7

from .prioritary_entry import _PrioritaryEntry as PrioritaryEntry


class FileAddedEntry(PrioritaryEntry):
    """
    Generated when a file is added
    """

    def dispatch(self, db_cursor):
        pass
