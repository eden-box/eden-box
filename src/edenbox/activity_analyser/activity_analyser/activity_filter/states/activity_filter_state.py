#!/usr/bin/env python3.7

import abc


class _ActivityFilterState(metaclass=abc.ABCMeta):
    """
    Activity filter behavior
    Defines how activities are added to the filter and how they are processed
    """

    def __init__(self, activity_filter):
        activity_filter.bind_state(self)
        self._activity_filter = activity_filter

    @property
    @abc.abstractmethod
    def identifier(self):
        pass

    def unbind(self):
        """
        Unbinds state
        Used to assure garbage collection
        """
        self._activity_filter = None

    def _change_state(self, state_type):
        """
        Change state
        :param state_type: next state type
        :return: activity filter
        """
        from .state_manager import StateManager

        StateManager.register_state(
            state_type,
            self._activity_filter
        )

    @abc.abstractmethod
    def add_activity(self, activity):
        """
        Add activity
        :param activity: activity to add
        """
        pass

    @abc.abstractmethod
    def process(self):
        """
        Process activity queue
        """
        pass

    def _dispatch_queue(self, queue):
        """
        Dispatches queue activities to a database connector
        :param queue: queue to be dispatched
        """
        if not queue.empty():
            self._activity_filter.database_connector.dispatch(queue)
