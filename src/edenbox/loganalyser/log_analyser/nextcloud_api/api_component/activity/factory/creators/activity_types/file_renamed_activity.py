#!/usr/bin/env python3.7

from .prioritary_activity import _PrioritaryActivity


class FileRenamedActivity(_PrioritaryActivity):
    """
    Generated when a file is renamed
    """

    """previous path of the renamed file"""
    old_file = str

    """new path of the renamed file"""
    new_file = str

    __procedure = "file_renamed"

    def _activity_process(self, xml_dict):
        changes = xml_dict["subject_rich"]["element"][1]

        self.old_file = "/{}".format(changes["oldfile"]["path"])
        self.new_file = "/{}".format(changes["newfile"]["path"])

    def dispatch(self, db_cursor):
        db_cursor.callproc(self.__procedure, (self.old_file, self.new_file, self.time))
