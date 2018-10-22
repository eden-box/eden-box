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
        if not self.__entries.full():
            try:
                self.__entries.put_nowait(entry)
            except Full:  # when queue is full
                raise FullQueueException

    def get(self):
        """
        Get entry
        :return: entry
        """
        try:
            return self.__entries.get_nowait()
        except Empty: # when queue is empty
            raise EmptyQueueException

    def size(self):
        """
        Current queue size
        :return:
        """
        return self.__entries.qsize()

    def max_size(self):
        """
        Max queue size
        :return: max queue size
        """
        return self.__entries.maxsize

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
