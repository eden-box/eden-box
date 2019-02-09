#!/usr/bin/env python3.7

import abc
from .activity import Activity


class _PrioritaryActivity(Activity):
    """
    Prioritary entry
    """

    def add_to_filter(self, log_filter):
        """
        Defines how to add a prioritary entry to a filter
        :param log_filter: filter to which the entry will be added
        """
        log_filter.filter_high_priority_entry(self)

    @abc.abstractmethod
    def dispatch(self, db_cursor):
        """
        Defines method used to communicate with database
        :param db_cursor: database cursor
        """
        pass
