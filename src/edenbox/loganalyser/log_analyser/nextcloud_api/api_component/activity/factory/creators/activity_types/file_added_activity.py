#!/usr/bin/env python3.7

from .prioritary_activity import _PrioritaryActivity


class FileAddedActivity(_PrioritaryActivity):
    """
    Generated when a file is added
    """

    __procedure = "file_added"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
