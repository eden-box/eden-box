#!/usr/bin/env python3.7

from .default_activity import _DefaultActivity


class FileAccessActivity(_DefaultActivity):
    """
    Generated when a file is accessed
    """

    __procedure = "file_accessed"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
