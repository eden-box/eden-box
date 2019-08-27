#!/usr/bin/env python3.7

import abc
import datetime


class Activity(metaclass=abc.ABCMeta):
    """
    Explicit representation of an activity
    """

    """activity ID"""
    activity_id = int

    """file handled in this activity"""
    file = str

    """activity timestamp"""
    time = datetime.datetime

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

    def add_to_filter(self, activity_filter):
        """
        Defines how to add an activity to a filter
        :param activity_filter: filter to which the activity will be added
        """
        activity_filter.add_activity(self)

    @abc.abstractmethod
    def dispatch(self, db_cursor):
        """
        Defines method used to communicate with database
        :param db_cursor: database cursor
        """
        pass
