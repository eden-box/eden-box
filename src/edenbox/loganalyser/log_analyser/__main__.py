#!/usr/bin/env python3.7

import sys
from .log_parser import LogParser
from .log_filter import LogFilter


def main(file_name):

    LogParser(file_name, LogFilter())

    print("Parsing finished")

    exit(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
