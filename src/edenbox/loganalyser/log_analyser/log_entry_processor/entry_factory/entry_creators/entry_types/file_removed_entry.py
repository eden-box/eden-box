#!/usr/bin/env python3.7

from .prioritary_entry import _PrioritaryEntry as PrioritaryEntry


class FileRemovedEntry(PrioritaryEntry):
    """
    Generated when a file is removed
    """

    def dispatch(self, db_cursor):
        pass
