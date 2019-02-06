#!/usr/bin/env python3.7

import abc


class Activity(metaclass=abc.ABCMeta):
    """
    Explicit representation of an activity
    """

    def __init__(self, activity_id, timestamp, file, xml_dict):
        self.activity_id = activity_id
        self.file = file
        self.time = timestamp
        self._activity_process(xml_dict)

    def _activity_process(self, xml_dict):
        """
        Extracts specific activity data from the xml dict
        :param xml_dict: contains activity information
        """
        return

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
        pass
