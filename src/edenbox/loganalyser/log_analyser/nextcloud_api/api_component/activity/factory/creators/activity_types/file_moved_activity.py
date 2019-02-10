#!/usr/bin/env python3.7

from .prioritary_activity import _PrioritaryActivity


class FileMovedActivity(_PrioritaryActivity):
    """
    Generated when a file is moved or renamed
    """

    """previous path of the file"""
    old_file = str

    """new path of the file"""
    new_file = str

    __procedure = "file_moved"

    def _activity_process(self, xml_dict):
        changes = xml_dict["subject_rich"]["element"][1]

        self.old_file = "/{}".format(changes["oldfile"]["path"])
        self.new_file = "/{}".format(changes["newfile"]["path"])

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.old_file, self.new_file, self.time))
