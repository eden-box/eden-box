#!/usr/bin/env python3.7

from .log_filter_state import _LogFilterState as LogFilterState
from .default_log_filter_state import DefaultLogFilterState


class ContingencyLogFilterState(LogFilterState):
    """
    Defines contingency log filter behavior
    During contingency, only prioritary entries are added, while default ones are ignored
    """

    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        return

    def add_prioritary_entry(self, entry):
        """
        Add prioritary entry
        Entry is added only if queue is not empty
        :param entry: prioritary entry
        """
        self._log_filter.add_to_prioritary_queue(entry)

    def process(self):

        self._log_filter.log_entries.reset()

        old_p_queue = self._log_filter.prioritary_log_entries.reset()

        while old_p_queue.qsize() > 0:
            entry = old_p_queue.get()
            entry.dispatch()  # TODO

        self._log_filter.bind_state(DefaultLogFilterState(self._log_filter))  # return to default state
