#!/usr/bin/env python3.7

import abc


class _LogFilterState(metaclass=abc.ABCMeta):
    """
    Defines log filter behavior
    """

    def __init__(self, log_filter):
        self._log_filter = log_filter

    def unbind(self):
        self._log_filter = None

    @abc.abstractmethod
    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        pass

    @abc.abstractmethod
    def add_prioritary_entry(self, entry):
        """
        Add prioritary entry
        Entry is added only if queue is not empty
        :param entry: prioritary entry
        """
        pass

    @abc.abstractmethod
    def process(self):
        """
        Process entry queues
        """
        pass
