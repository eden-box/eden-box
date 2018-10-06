#!/usr/bin/env python3.7

from threading import Timer
from .log_filter_config import LogFilterConfig as Config
from .states import DefaultLogFilterState
from .log_filter_entry_queue import EntryQueue


class LogFilter:
    """
    Stores entry data to be processed
    """

    """log filter state"""
    __state = None

    """prioritary log entries to process"""
    prioritary_log_entries = EntryQueue(Config.MAX_QUEUE_SIZE)  # FIXME define size

    """log entries to process"""
    log_entries = EntryQueue(Config.MAX_QUEUE_SIZE)

    def __init__(self):
        self.bind_state(DefaultLogFilterState(self))
        self.__process_timer = Timer(Config.PROCESS_INTERVAL, self.__process)
        self.__process_timer.start()

    def bind_state(self, state):
        self.__unbind_state()
        self.__state = state

    def __unbind_state(self):
        if self.__state:
            self.__state.unbind()
            self.__state = None

    def filter(self, entry):
        """
        Add entry to processment queue
        :param entry: entry to process
        """
        entry.add_to_filter(self)

    def filter_default_entry(self, entry):
        self.__state.add_default_entry(entry)

    def filter_prioritary_entry(self, entry):
        self.__state.add_prioritary_entry(entry)

    def add_to_default_queue(self, entry):
        self.log_entries.add(entry)

    def add_to_prioritary_queue(self, entry):
        self.log_entries.add(entry)
        self.prioritary_log_entries.add(entry)

    def __process(self):
        self.__state.process()
