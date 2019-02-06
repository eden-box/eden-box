#!/usr/bin/env python3.7

import abc
from .activity import Activity


class _DefaultActivity(Activity):
    """
    Default entry
    """

    def add_to_filter(self, filter_):
        """
        Defines how to add a default entry to a filter
        :param filter_: filter to which the entry will be added
        """
        filter_.filter_default_entry(self)

    @abc.abstractmethod
    def dispatch(self, db_cursor):
        """
        Defines method used to communicate with database
        :param db_cursor: database cursor
        """
        pass
