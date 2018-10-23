#!/usr/bin/env python3.7

from .prioritary_entry import _PrioritaryEntry as PrioritaryEntry


class FileModifiedEntry(PrioritaryEntry):
    """
    Generated when a file is modified
    """

    def dispatch(self, db_cursor):
        pass
