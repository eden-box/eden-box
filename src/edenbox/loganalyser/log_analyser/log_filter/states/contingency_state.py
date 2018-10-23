#!/usr/bin/env python3.7

from .log_filter_state import _LogFilterState
from .state_factory import *
from ..exceptions import FullHighException


class ContingencyState(_LogFilterState):
    """
    Defines contingency log filter behavior

    During contingency, only high priority entries are added, while default ones are ignored.
    Only high priority entries are processed.
    """

    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        return

    def add_high_priority_entry(self, entry):
        """
        Add high priority entry
        :param entry: high priority entry
        """
        try:
            self._log_filter.add_to_high_priority_queue(entry)
        except FullHighException:
            old_p_queue = self._log_filter.high_priority_log_entries.reset()

            self._dispatch_queue(old_p_queue)

    def process(self):
        """
        Process entry queues

        Reset default priority queue and process high priority queue only
        Revert state back to default
        """

        self._log_filter.log_entries.reset()

        old_p_queue = self._log_filter.high_priority_log_entries.reset()

        self._log_filter.bind_state(
            StateFactory.get_state(
                StateType.DEFAULT,
                self._log_filter
            )
        )  # return to default state

        self._dispatch_queue(old_p_queue)
