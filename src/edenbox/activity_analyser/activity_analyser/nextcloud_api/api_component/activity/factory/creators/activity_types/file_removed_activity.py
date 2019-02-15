#!/usr/bin/env python3.7

from .activity import Activity


class FileRemovedActivity(Activity):
    """
    Generated when a file is removed
    """

    __procedure = "file_removed"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
