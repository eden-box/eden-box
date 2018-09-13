#!/usr/bin/env python3.7

import time
from threading import Thread
from multiprocessing import Pool
from log_analyser.log_entry_processor import LogEntryProcessor


class LogParser:

    active = False
    __def_sleep = 0.00001

    def __init__(self, file, log_filter):

        # Configuration
        self.__file = file
        self.__log_filter = log_filter

        # Process Pool creation
        self.__process_pool = Pool(processes=4)  # TODO refactor number of processes and/or move to config file

        # Thread creation
        thread = Thread(target=self.__run, args=self.__file, daemon=True)  # TODO move this to another place
        thread.start()
        thread.join()
        self.active = False

        # Cleanup
        self.__process_pool.close()
        self.__process_pool.join()

    def __run(self, file_path):
        """
        Processes each line fetched from the file
        :param file_path: log to be parsed and analysed
        """
        file = open(file_path)
        lines = self.__tail(file)

        for line in lines:
            self.__process(line)

    def __tail(self, file):
        """
        Periodically fetches a line from the file and yields it
        :param file: log to be parsed and analysed
        """

        file.seek(0, 2)  # go to the end of the file
        sleep = self.__def_sleep

        self.active = True

        while self.active:
            line = file.readline()
            if not line:
                time.sleep(sleep)  # sleep briefly
                if sleep < 1.0:
                    sleep += self.__def_sleep
                continue
            sleep = self.__def_sleep
            yield line

    def __process(self, entry):
        self.__process_pool.apply_async(func=LogEntryProcessor.process, args=(self.__log_filter, entry))
