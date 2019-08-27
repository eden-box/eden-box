#!/usr/bin/env python3.7

from queue import Queue, Empty, Full
from .exceptions import FullQueueException, EmptyQueueException


class ActivityQueue:
    """
    FIFO Activity queue

    Stores activities to be processed
    """

    def __init__(self, queue_size):
        self.__activities = Queue(queue_size)

    def add(self, activity):
        """
        Add an activity to the queue
        :param activity: activity to add
        """
        try:
            self.__activities.put_nowait(activity)
        except Full as e:  # when queue is full
            raise FullQueueException(e, "Activity could not be added, queue is full.")

    def get(self):
        """
        Get activity
        :return: activity
        """
        try:
            return self.__activities.get_nowait()
        except Empty as e:  # when queue is empty
            raise EmptyQueueException(e, "No activity could not be obtained, queue is empty.")

    def size(self):
        """
        Current queue size
        :return: current queue size
        """
        return self.__activities.qsize()

    def max_size(self):
        """
        Max queue size
        :return: max queue size
        """
        return self.__activities.maxsize

    def empty(self):
        """
        Check if the queue is empty
        :return: true if the queue is empty
        """
        return self.__activities.empty()

    def full(self):
        """
        Check if queue is full
        :return: true if queue is full
        """
        return self.__activities.full()

    def reset(self):
        """
        Creates a new queue, returning the old one
        :return: previous queue
        """
        prev_queue = self.__activities
        self.__activities = Queue(self.max_size())
        return prev_queue
