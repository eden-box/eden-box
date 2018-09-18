#!/usr/bin/env python3.7


class LogParserConfig:
    """
    Log parser configuration
    """

    """log parser default sleep time between readlines"""
    DEFAULT_SLEEP = 0.00001

    """log parser max sleep time between readlines, reached when file updates are less frequent"""
    MAX_SLEEP = 1.0

    """process pool size"""
    PROCESSES = 4  # TODO refactor number of processes
