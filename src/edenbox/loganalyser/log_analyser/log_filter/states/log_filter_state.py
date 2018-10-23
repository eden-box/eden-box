#!/usr/bin/env python3.7

import abc
from .state_factory import *


class _LogFilterState(metaclass=abc.ABCMeta):
    """
    Log filter behavior
    Defines how entries are added to the filter and how they are processed
    """

    def __init__(self, log_filter):
        self._log_filter = log_filter

    def unbind(self):
        """
        Unbinds state
        Used to assure garbage collection
        """
        self._log_filter = None

    def _change_state(self, state_type):
        """
        Change state
        :param state_type: next state type
        """
        self._log_filter.bind_state(
            StateFactory.get_state(
                    state_type,
                    self._log_filter
            )
        )

    @abc.abstractmethod
    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        pass

    @abc.abstractmethod
    def add_high_priority_entry(self, entry):
        """
        Add high priority entry
        :param entry: high priority entry
        """
        pass

    @abc.abstractmethod
    def process(self):
        """
        Process entry queues
        """
        pass

    def _dispatch_queue(self, queue):
        """
        Dispatches queue entries to a database connector
        :param queue: queue to be dispatched
        """
        while queue.qsize() > 0:
            entry = queue.get()
            entry.dispatch()  # TODO
