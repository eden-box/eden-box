#!/usr/bin/env python3.7

from queue import Queue
from asyncio import QueueFull
from .log_filter_config import LogFilterConfig as Config


class LogFilter:
    """
    Stores entry data to be processed
    """

    """log entries to process"""
    __log_entries = Queue(Config.MAX_QUEUE_SIZE)

    def filter(self, entry):
        """
        Add entry to processment queue
        :param entry: entry to process
        """

        if not self.__log_entries.full():
            try:
                self.__log_entries.put_nowait(entry)
            except QueueFull:  # when queue is full
                pass  # TODO handle exception

    def count(self):
        """
        Number of not yet processed log entries
        :return: number of log entries
        """
        return self.__log_entries.qsize()
