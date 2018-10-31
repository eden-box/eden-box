#!/usr/bin/env python3.7

import sys
from .log_parser import LogParser
from .log_filter import LogFilter
from .database_connector import DatabaseConnector


def main(file_name):

    db_connector = DatabaseConnector()

    LogParser(file_name, LogFilter(db_connector))

    print("Parsing finished")

    exit(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
