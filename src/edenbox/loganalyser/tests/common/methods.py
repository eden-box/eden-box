#!/usr/bin/env python3.7

import json
import time
from random import shuffle
from log_analyser.log_entry_processor.entry_factory.entry_creators.entry_types import FileAccessEntry, FileAddedEntry
from log_analyser.log_filter.log_filter_config import LogFilterConfig  # allow access to round dispatch time config


class Methods:

    @staticmethod
    def wait_for_dispatch(rounds):
        """
        Wait for a given number of dispatch rounds to pass
        :param rounds: number of rounds to wait for
        """

        if rounds > 0:
            wait_time = (rounds * LogFilterConfig.process_interval()) + 1  # acceptably strict time
            time.sleep(wait_time)

    @staticmethod
    def dummy_entry(default=True):
        """
        Obtain a dummy default or high priority entry
        :param default: True for a default entry request, False for a high priority entry
        :return: default priority entry or high priority entry
        """

        line = '{"time": "<date>", "method": "GET", "message": "<file>"}'
        line = json.loads(line)

        if default:
            operation = "File accessed"
            entry = FileAccessEntry(operation, line)
        else:  # high priority
            operation = "File added"
            entry = FileAddedEntry(operation, line)
        return entry

    @staticmethod
    def dummy_queue(default_priority=0, high_priority=0, randomize=False):
        """
        Obtain a list of entries
        The list contains the requested default priority entries followed by the high priority entries
        :param default_priority: quantity of high priority entries
        :param high_priority: quantity of high priority entries
        :param randomize: whether the entries order should be randomized
        :return: list of entries
        """

        entries = []

        for i in range(default_priority):
            entries.append(Methods.dummy_entry(default=True))

        for e in range(high_priority):
            entries.append(Methods.dummy_entry(default=False))

        if randomize:
            shuffle(entries)

        return entries

    @staticmethod
    def process_queue(log_filter, queue=(), default=0, high=0):
        """
        Utility to make log_filter process a queue
        If a queue is provided, that is the one to process, if default or high values are set,
        a queue with the requested quantity of entries will be processed.
        :param log_filter: log filter used to process queue
        :param queue: queue to process
        :param default: number of default priority entries to process
        :param high: number of high priority entries to process
        """

        if default or high:
            queue = Methods.dummy_queue(default, high)

        for entry in queue:
                log_filter.filter(entry)

    @staticmethod
    def in_default_state(log_filter):
        """
        Verify if log_filter is in default state
        :param log_filter: log filter to verify
        :return: True if the log_filter is in default state
        """
        return log_filter.state_identifier == "Default"

    @staticmethod
    def in_contingency_state(log_filter):
        """
        Verify if log_filter is in contingency state
        :param log_filter: log filter to verify
        :return: True if the log_filter is in contingency state
        """
        return log_filter.state_identifier == "Contingency"

    @staticmethod
    def get_dispatched_arguments(mocked_db):
        """
        Obtain a list with all the arguments processed by a mock
        :param mocked_db: mocked database connector
        :return: list of dispatched queues, with dispatched queues being also lists
        """
        call_args_list = mocked_db.dispatch.call_args_list
        args = []
        for arg in call_args_list:
            args.append(list(arg[0][0].queue))
        return args
