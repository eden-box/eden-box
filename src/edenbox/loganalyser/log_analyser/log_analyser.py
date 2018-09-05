#!/usr/bin/env python3.7

import sys
from log_analyser.log_filter import LogFilter


def main(file_name):

    LogFilter(file_name)

    exit(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
