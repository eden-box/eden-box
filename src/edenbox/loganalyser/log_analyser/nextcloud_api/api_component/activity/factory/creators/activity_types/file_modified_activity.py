#!/usr/bin/env python3.7

from .prioritary_activity import _PrioritaryActivity


class FileModifiedActivity(_PrioritaryActivity):
    """
    Generated when a file is modified
    """

    __procedure = "file_modified"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
