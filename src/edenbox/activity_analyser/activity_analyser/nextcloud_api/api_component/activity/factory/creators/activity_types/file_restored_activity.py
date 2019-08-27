#!/usr/bin/env python3.7

from .activity import Activity


class FileRestoredActivity(Activity):
    """
    Generated when a file is restored
    """

    __procedure = "file_restored"

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.file, self.time))
