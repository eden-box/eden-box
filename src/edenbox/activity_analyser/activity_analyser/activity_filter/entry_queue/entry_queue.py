#!/usr/bin/env python3.7

from queue import Queue, Empty, Full
from .exceptions import FullQueueException, EmptyQueueException


class EntryQueue:
    """
    FIFO Entry queue

    Stores entries to be processed
    """

    def __init__(self, queue_size):
        self.__entries = Queue(queue_size)

    def add(self, entry):
        """
        Add an entry to the queue
        :param entry: entry to add
        """
        try:
            self.__entries.put_nowait(entry)
        except Full as e:  # when queue is full
            raise FullQueueException(e, "Entry could not be added, queue is full")

    def get(self):
        """
        Get entry
        :return: entry
        """
        try:
            return self.__entries.get_nowait()
        except Empty as e:  # when queue is empty
            raise EmptyQueueException(e, "No entry could not be obtained, queue is empty")

    def size(self):
        """
        Current queue size
        :return: current queue size
        """
        return self.__entries.qsize()

    def max_size(self):
        """
        Max queue size
        :return: max queue size
        """
        return self.__entries.maxsize

    def empty(self):
        """
        Check if the queue is empty
        :return: true if the queue is empty
        """
        return self.__entries.empty()

    def full(self):
        """
        Check if queue is full
        :return: true if queue is full
        """
        return self.__entries.full()

    def reset(self):
        """
        Creates a new entry queue, returning the old one
        :return: previous entry queue
        """
        prev_queue = self.__entries
        self.__entries = Queue(self.max_size())  # TODO is a mutex needed?
        return prev_queue
