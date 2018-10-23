#!/usr/bin/env python3.7

from .log_filter_state import _LogFilterState
from .state_factory import *
from ..exceptions import FullDefaultException, FullHighException


class DefaultState(_LogFilterState):
    """
    Defines default log filter behavior

    Default entries are added to default filter queue,
    while high priority entries are also added to high priority queue.

    Temporal coherency of the events is assured, even if contingency measures are enforced.
    """

    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        try:
            self._log_filter.add_to_default_queue(entry)
        except FullDefaultException:
            self._log_filter.bind_state(
                StateFactory.get_state(
                    StateType.CONTINGENCY,
                    self._log_filter
                )
            )  # enter contingency state

    def add_high_priority_entry(self, entry):
        """
        Add high priority entry
        :param entry: high priority entry
        """
        try:
            self._log_filter.add_to_default_queue(entry)
            self._log_filter.add_to_high_priority_queue(entry)
        except (FullDefaultException, FullHighException):
            self._log_filter.bind_state(
                StateFactory.get_state(
                    StateType.CONTINGENCY,
                    self._log_filter
                )
            )  # enter contingency state

            self._log_filter.filter_high_priority_entry(entry)  # delegate choice to log filter

    def process(self):
        """
        Process entry queues

        Reset default high priority queue and process default priority queue only
        """

        self._log_filter.high_priority_log_entries.reset()

        old_queue = self._log_filter.log_entries.reset()

        self._dispatch_queue(old_queue)
