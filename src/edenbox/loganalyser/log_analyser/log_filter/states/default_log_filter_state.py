#!/usr/bin/env python3.7

from .log_filter_state import _LogFilterState as LogFilterState


class DefaultLogFilterState(LogFilterState):
    """
    Defines default log filter behavior
    Default entries are added to default filter queue,
    while high priority entries are also added to high priority queue
    """

    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        self._log_filter.add_to_default_queue(entry)

    def add_high_priority_entry(self, entry):
        """
        Add high priority entry
        :param entry: high priority entry
        """
        self._log_filter.add_to_high_priority_queue(entry)

    def process(self):
        """
        Process entry queues

        Reset default high priority queue and process default priority queue only
        """

        self._log_filter.high_priority_log_entries.reset()

        old_queue = self._log_filter.log_entries.reset()

        while old_queue.qsize() > 0:
            entry = old_queue.get()
            entry.dispatch()  # TODO
