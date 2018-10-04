#!/usr/bin/env python3.7

import abc

"""
Received json object
{
   "reqId":"<id>",
   "level":1,
   "time":"2018-12-31T17:00:00+00:00",
   "remoteAddr":"<ip>",
   "user":"<user>",
   "app":"<app>",
   "method":"GET|PUT|DELETE|MOVE",
   "url":"<url>",
   "message":"<action>: \"<file_path>\"",
   "userAgent":"<userAgent>",
   "version":"<fs_version>"
}
"""


class _Entry(metaclass=abc.ABCMeta):
    """
    Explicit representation of a log file entry
    """

    def __init__(self, file, line):
        self.file = file
        self.__process_json_entry(line)

    def __process_json_entry(self, json_entry):
        """
        Extracts data from the json entry
        :param json_entry: contains log entry information
        """
        self.time = json_entry.time
        self.method = json_entry.method

    @abc.abstractmethod
    def add_to_filter(self, log_filter):
        """
        Defines how to add an entry to a filter
        :param log_filter: filter to which the entry will be added
        """
        pass

    @abc.abstractmethod
    def dispatch(self, db_cursor):
        """
        Defines method used to communicate with database
        :param db_cursor: database cursor
        """
        # db_cursor.callproc(‘stored_procedure_name’, (value1,value2))
        pass
