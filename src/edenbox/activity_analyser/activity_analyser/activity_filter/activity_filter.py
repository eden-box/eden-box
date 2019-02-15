#!/usr/bin/env python3.7

from threading import Timer
from .activity_filter_config import ActivityFilterConfig as Config
from .states import StateType, StateManager
from .entry_queue import EntryQueue
from .entry_queue.exceptions import FullQueueException
from .exceptions import FullActivityQueueException


class ActivityFilter:
    """
    Stores entry data to be processed

    Entry queues are periodically processed given a Timer.
    File management related entries have high priority, like file addition, renaming or removal, for example.

    If, by any reason, the log filter is overflown with entries, it will enter in contingency
    mode, where only high priority entries will be added and processed.
    After contingency is over, the state returns to the default one, processing all entries.
    """

    """database connection manager"""
    database_connector = None

    """log filter state"""
    __state = None

    """log entries"""
    activities = None

    def __init__(self, db_connector):

        self.activities = EntryQueue(Config.max_queue_size())

        StateManager.register_state(
            StateType.DEFAULT,
            self
        )

        self.database_connector = db_connector

        self.__process_timer = Timer(interval=Config.process_interval(), function=self.__process)
        self.__process_timer.daemon = True
        self.__process_timer.start()

    def bind_state(self, state):
        """
        Binds a given state, unbinding the old one
        :param state: state to bind
        """
        self.__unbind_state()
        self.__state = state

        return self

    def __unbind_state(self):
        """
        Unbinds the current state
        """
        self.__state = None

    @property
    def state_identifier(self):
        """
        Current state identifier
        :return: state identifier
        """
        return self.__state.identifier

    def filter(self, entry):
        """
        Add entry to filter
        :param entry: entry to add
        """
        entry.add_to_filter(self)

    def add_activity(self, entry):
        """
        Add an entry to default priority queue
        :param entry: entry to add
        """
        try:
            self.__state.add_activity(entry)
        except FullQueueException as e:
            raise FullActivityQueueException(e, "Entry cannot be added, activity queue is full")

    def __process(self):
        """
        Process entry queues
        """
        self.__state.process()
