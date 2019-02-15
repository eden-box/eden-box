#!/usr/bin/env python3.7

import abc


class _ActivityFilterState(metaclass=abc.ABCMeta):
    """
    Log filter behavior
    Defines how entries are added to the filter and how they are processed
    """

    def __init__(self, log_filter):
        log_filter.bind_state(self)
        self._log_filter = log_filter

    @property
    @abc.abstractmethod
    def identifier(self):
        pass

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
        :return: log filter
        """
        from .state_manager import StateManager

        StateManager.register_state(
            state_type,
            self._log_filter
        )

    @abc.abstractmethod
    def add_activity(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
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
        if not queue.empty():
            self._log_filter.database_connector.dispatch(queue)
