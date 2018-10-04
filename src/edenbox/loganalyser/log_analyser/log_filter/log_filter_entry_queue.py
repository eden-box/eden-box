#!/usr/bin/env python3.7

from queue import Queue, Empty
from asyncio import QueueFull


class EntryQueue:

    def __init__(self, queue_size):
        self.__entries = Queue(queue_size)

    def add(self, entry):
        if not self.__entries.full():
            try:
                self.__entries.put_nowait(entry)
            except QueueFull:  # when queue is full
                pass  # TODO handle exception

    def get(self):
        try:
            return self.__entries.get_nowait()
        except Empty:
            pass  # TODO decide what to do

    def size(self):
        return self.__entries.qsize()

    def max_size(self):
        return self.__entries.maxsize

    def full(self):
        return self.__entries.full()

    def reset(self):
        """
        Creates a new entry queue, returning the old one
        :return: previous entry queue
        """
        prev_queue = self.__entries
        self.__entries = Queue(self.max_size())  # TODO is a mutex needed?
        return prev_queue
