#!/usr/bin/env python3.7

import sys
from .log_filter import LogFilter
from .log_parser import LogParser
from .database_connector import DatabaseConnector


def main(file_name):

    db_connector = DatabaseConnector()

    log_filter = LogFilter(db_connector)

    LogParser(file_name, log_filter)  # blocks for parsing

    exit(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
