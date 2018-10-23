#!/usr/bin/env python3.7


class LogFilterConfig:
    """
    Log Filter configuration
    """

    """max size of the default priority entry queue"""
    MAX_DEFAULT_PRIORITY_QUEUE_SIZE = 100  # TODO choose a good limit

    """max size of the high priority entry queue"""
    MAX_HIGH_PRIORITY_QUEUE_SIZE = 100  # TODO choose a good limit

    """interval between queues processment"""
    PROCESS_INTERVAL = 60.0  # TODO check if interval is adequate
