#!/usr/bin/env python3.7

import time
import logging
from pathlib import Path
from threading import Thread
from multiprocessing import Pool
from log_analyser.log_entry_processor import LogEntryProcessor
from .log_parser_config import LogParserConfig as Config
from .exceptions import NoLogFileException

logger = logging.getLogger(__name__)


class LogParser:
    """
    Parses a log file

    Tails a file and passes added lines to the log filter
    """

    """active states whether the file is being parsed"""
    active = False

    """default pooling time interval"""
    __def_sleep = None

    """max pooling time interval"""
    __max_sleep = None

    """thread responsible for log file parsing"""
    __parser_thread = None

    def __init__(self, file, log_filter):

        self.__def_sleep = Config.default_sleep()

        self.__max_sleep = Config.max_sleep()

        if Path(file).is_file():
            self.__file = file
        else:
            logger.critical("Log file does not exist")
            raise NoLogFileException("Log file does not exist")

        self.__log_filter = log_filter

        # Process Pool creation
        self.__process_pool = Pool(processes=Config.processes())

    def run(self, keepalive=True):
        # Thread creation
        self.__parser_thread = Thread(target=self.__run, args=(self.__file,), daemon=True)
        self.__parser_thread.start()

        if keepalive:
            self.__parser_thread.join()
            self.stop()

    def stop(self):

        self.active = False

        self.__parser_thread.join()

        # Cleanup
        self.__process_pool.close()
        self.__process_pool.join()

    def __run(self, file_path):
        """
        Send each fetched line to process
        :param file_path: log file to be parsed and analysed
        """
        try:
            with open(file=file_path, mode=Config.file_access_mode()) as file:
                lines = self.__tail(file)

                for line in lines:
                    self.__process(line)
        except IOError as e:
            logger.critical("Log file does not exist")
            raise NoLogFileException(e, "Log file does not exist")

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
