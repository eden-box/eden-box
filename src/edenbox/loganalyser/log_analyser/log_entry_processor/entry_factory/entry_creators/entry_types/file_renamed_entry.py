#!/usr/bin/env python3.7

from .prioritary_entry import _PrioritaryEntry as PrioritaryEntry


class FileRenamedEntry(PrioritaryEntry):
    """
    Generated when a file is renamed
    """

    __procedure = "file_renamed"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
