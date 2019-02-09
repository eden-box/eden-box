#!/usr/bin/env python3.7

from .prioritary_activity import _PrioritaryActivity


class FileRemovedActivity(_PrioritaryActivity):
    """
    Generated when a file is removed
    """

    __procedure = "file_removed"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
