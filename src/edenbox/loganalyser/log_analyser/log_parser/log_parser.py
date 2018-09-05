#!/usr/bin/env python3.7

import sys
import time
from threading import Thread


class LogParser:

    active = False
    __file = ""
    __def_sleep = 0.00001

    def __init__(self, file):

        # Configuration
        self.__file = file

        # Thread creation
        thread = Thread(target=self.__run, args=self.__file)  # TODO move this to another place
        thread.setDaemon(True)

        thread.start()

        thread.join()

    def __run(self, file_path):
        file = open(file_path)
        lines = self.__tail(file)

        for line in lines:
            print(line)

    def __tail(self, file):
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


def main(file_name):

    LogParser(file_name)

    print("Parsing finished")

    exit(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
