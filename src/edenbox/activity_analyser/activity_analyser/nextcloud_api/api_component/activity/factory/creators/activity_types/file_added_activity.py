#!/usr/bin/env python3.7

from .activity import Activity


class FileAddedActivity(Activity):
    """
    Generated when a file is added
    """

    __procedure = "file_added"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
