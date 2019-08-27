#!/usr/bin/env python3.7

from .activity import Activity


class FileModifiedActivity(Activity):
    """
    Generated when a file is modified
    """

    __procedure = "file_modified"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
