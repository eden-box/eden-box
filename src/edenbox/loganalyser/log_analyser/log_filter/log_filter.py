#!/usr/bin/env python3.7

from threading import Timer
from .log_filter_config import LogFilterConfig as Config
from .states import DefaultLogFilterState
from .log_filter_entry_queue import EntryQueue


class LogFilter:
    """
    Stores entry data to be processed

    Entry queues are periodically processed given a Timer.
    File management related entries have high priority, like file addition, renaming or removal, for example.

    If, by any reason, the log filter is overflown with entries, it will enter in contingency
    mode, where only high priority entries will be added and processed.
    After contingency is over, the state returns to the default one, processing all entries.
    """

    """log filter state"""
    __state = None

    """log entries"""
    log_entries = EntryQueue(Config.MAX_QUEUE_SIZE)

    """prioritary log entries"""
    prioritary_log_entries = EntryQueue(Config.MAX_QUEUE_SIZE)  # FIXME define size

    def __init__(self):
        self.bind_state(DefaultLogFilterState(self))
        self.__process_timer = Timer(Config.PROCESS_INTERVAL, self.__process)
        self.__process_timer.start()

    def bind_state(self, state):
        """
        Binds a given state, unbinding the old one
        :param state:
        """
        self.__unbind_state()
        self.__state = state

    def __unbind_state(self):
        """
        Unbinds the current state
        """
        if self.__state:
            self.__state.unbind()
            self.__state = None

    def filter(self, entry):
        """
        Add entry to filter
        :param entry: entry to add
        """
        entry.add_to_filter(self)

    def filter_default_entry(self, entry):
        """
        Pass a default priority entry to state
        :param entry: default priority entry
        """
        self.__state.add_default_entry(entry)

    def filter_prioritary_entry(self, entry):
        """
        Pass a high priority entry to state
        :param entry: high priority entry
        """
        self.__state.add_prioritary_entry(entry)

    def add_to_default_queue(self, entry):
        """
        Add an entry to default priority queue
        :param entry: entry to add
        """
        self.log_entries.add(entry)

    def add_to_prioritary_queue(self, entry):
        """
        Add an entry to high priority queue
        :param entry: entry to add
        """
        self.log_entries.add(entry)
        self.prioritary_log_entries.add(entry)

    def __process(self):
        """
        Process entry queues
        """
        self.__state.process()
