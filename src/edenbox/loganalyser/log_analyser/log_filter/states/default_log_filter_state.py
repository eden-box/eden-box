#!/usr/bin/env python3.7

from .log_filter_state import _LogFilterState as LogFilterState


class DefaultLogFilterState(LogFilterState):
    """
    Defines default log filter behavior
    Default entries are added to default filter queue, while prioritary are added to prioritary queue
    """

    def add__default_entry(self, entry):
        """
        Add default priority entry
        :param entry: default priority entry
        """
        self._log_filter.add_to_default_queue(entry)

    def add_prioritary_entry(self, entry):
        """
        Add prioritary entry
        Entry is added only if queue is not empty
        :param entry: prioritary entry
        """
        self._log_filter.add_to_prioritary_queue(entry)

    def process(self):

        old_queue = self._log_filter.log_entries.reset()

        old_p_queue = self._log_filter.prioritary_log_entries.reset()

        while old_p_queue.qsize() > 0:
            entry = old_queue.get()
            entry.dispatch()  # TODO

        while old_queue.qsize() > 0:
            entry = old_queue.get()
            entry.dispatch()  # TODO
