#!/usr/bin/env python3.7

import abc
from .entry import _Entry as Entry


class _DefaultEntry(Entry):
    """
    Default entry
    """

    def add_to_filter(self, log_filter):
        """
        Defines how to add a default entry to a filter
        :param log_filter: filter to which the entry will be added
        """
        log_filter.filter_default_entry(self)

    @abc.abstractmethod
    def dispatch(self, db_cursor):
        """
        Defines method used to communicate with database
        :param db_cursor: database cursor
        """
        pass
