#!/usr/bin/env python3.7

import time
from threading import Thread
from multiprocessing import Pool
from log_analyser.log_entry_processor import LogEntryProcessor
from .log_parser_config import LogParserConfig as Config


class LogParser:
    """
    Parses a log file

    Tails a file and passes added lines to the log filter
    """

    """active states whether the file is being parsed"""
    active = False

    """default pooling time interval"""
    __def_sleep = Config.DEFAULT_SLEEP

    """max pooling time interval"""
    __max_sleep = Config.MAX_SLEEP

    def __init__(self, file, log_filter):

        self.__file = file
        self.__log_filter = log_filter

        # Process Pool creation
        self.__process_pool = Pool(processes=Config.PROCESSES)

        # Thread creation
        thread = Thread(target=self.__run, args=self.__file, daemon=True)
        thread.start()

        # Blocks until thread stops
        thread.join()
        self.active = False

        # Cleanup
        self.__process_pool.close()
        self.__process_pool.join()

    def __run(self, file_path):
        """
        Send each fetched line fetched to process
        :param file_path: log file to be parsed and analysed
        """
        file = open(file_path)
        lines = self.__tail(file)

        for line in lines:
            self.__process(line)

    def __tail(self, file):
        """
        Periodically fetches a line from the file and yields it
        :param file: log file to be parsed and analysed
        """

        file.seek(0, 2)  # go to the end of the file
        sleep = self.__def_sleep

        self.active = True

        # reads are less frequent depending on file update frequency
        while self.active:
            line = file.readline()
            if not line:
                time.sleep(sleep)  # sleep briefly
                if sleep < self.__max_sleep:
                    sleep += self.__def_sleep
                continue
            sleep = self.__def_sleep
            yield line

    def __process(self, entry):
        """
        Processes an entry
        Sends the entry to the log pool, to be processed by the LogEntryProcessor
        :param entry: json entry from the log file
        """
        self.__process_pool.apply_async(func=LogEntryProcessor.process, args=(self.__log_filter, entry))
