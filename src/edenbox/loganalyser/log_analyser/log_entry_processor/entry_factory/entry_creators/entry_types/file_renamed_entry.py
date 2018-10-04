#!/usr/bin/env python3.7

from .prioritary_entry import _PrioritaryEntry as PrioritaryEntry


class FileRenamedEntry(PrioritaryEntry):
    """
    Generated when a file is renamed
    """

    def dispatch(self, db_cursor):
        pass
