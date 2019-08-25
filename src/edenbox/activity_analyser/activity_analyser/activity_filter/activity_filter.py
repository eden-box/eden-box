#!/usr/bin/env python3.7

from threading import Timer
from .activity_filter_config import ActivityFilterConfig
from .states import StateType, StateManager
from .activity_queue import ActivityQueue
from .activity_queue.exceptions import FullQueueException
from .exceptions import FullActivityQueueException


class ActivityFilter:
    """
    Stores activity data to be processed

    The activity queue is periodically processed, according to a Timer.
    """

    """database connection manager"""
    database_connector = None

    """activity filter state"""
    __state = None

    """stored activities"""
    activities = None

    def __init__(self, db_connector, config=None):

        config = ActivityFilterConfig(config)

        self.activities = ActivityQueue(config.max_queue_size())

        StateManager.register_state(
            StateType.DEFAULT,
            self
        )

        self.database_connector = db_connector

        self.__process_timer = Timer(interval=config.process_interval(), function=self.__process)
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

    def filter(self, activity):
        """
        Filter an activity
        :param activity: activity to filter
        """
        activity.add_to_filter(self)

    def add_activity(self, activity):
        """
        Add an activity to the activity queue
        :param activity: activity to add
        """
        try:
            self.__state.add_activity(activity)
        except FullQueueException as e:
            raise FullActivityQueueException(e, "Activity cannot be added, activity queue is full.")

    def __process(self):
        """
        Process activity queue
        """
        self.__state.process()
