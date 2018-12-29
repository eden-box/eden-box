#!/usr/bin/env python3.7

import pytest
from pytest_mock import mocker
import json
import time
from random import shuffle
from log_analyser import DatabaseConnector, LogFilter
from log_analyser.common.configuration import ConfigManager
from log_analyser.log_filter.log_filter_config import LogFilterConfig  # allow access to round dispatch time config
from log_analyser.log_entry_processor.entry_factory.entry_creators.entry_types import FileAccessEntry, FileAddedEntry


def wait_for_dispatch(rounds):
    """
    Wait for a given number of dispatch rounds to pass
    :param rounds: number of rounds to wait for
    """
    if rounds > 0:
        wait_time = (rounds * LogFilterConfig.process_interval()) + 1  # acceptably strict time
        time.sleep(wait_time)


def dummy_entry(default=True):

    line = '{"time": "<date>", "method": "GET", "message": "<file>"}'
    line = json.loads(line)

    if default:
        operation = "File accessed"
        entry = FileAccessEntry(operation, line)
    else:  # high priority
        operation = "File added"
        entry = FileAddedEntry(operation, line)
    return entry


def dummy_queue(default_priority=0, high_priority=0, randomize=False):
    """"
    Returns a dummy queue
    """
    entries = []

    for i in range(default_priority):
        entries.append(dummy_entry(default=True))

    for e in range(high_priority):
        entries.append(dummy_entry(default=False))

    if randomize:
        shuffle(entries)

    return entries


class TestLogFilter:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        """
        Setup, runs once, before all tests
        """
        ConfigManager().set_test()

    @pytest.fixture(scope="function")
    def mocked_db_connector(self, mocker):
        """"
        Returns a dummy database connector
        This dummy will serve as an analyser of the method calls issued by the Log Filter
        """

        mocker.patch.object(DatabaseConnector, "__init__", return_value=None)  # avoid connection to database
        mocker.patch.object(DatabaseConnector, "dispatch", return_value=None)  # mock dispatch calls

        db_conn = DatabaseConnector()

        mocker.spy(db_conn, 'dispatch')  # used to count number of dispatch calls

        return db_conn

    @pytest.fixture(scope="function")
    def get_filter(self, mocked_db_connector):
        """
        Returns a reference for a method able to generate a filter
        This method is used to overcome the limitation of fixtures of not allowing versatile parametrization of inputs
        :param mocked_db_connector:
        :return: a reference for the inner function 'dummy'
        """

        def dummy(default=0, high=0, contingency=False):
            """
            Returns a log filter in a given state, after processing some entries and the contained mocked db connector
            :param default: number of default priority entries
            :param high: number of high priority entries
            :param contingency: whether the filter is in contingency mode
            :return: log filter and corresponding mocked db connector
            """

            if contingency:  # if in contingency, fill the queue with default entries
                default += LogFilterConfig.max_default_priority_queue_size()

            queue = dummy_queue(default, high)

            log_filter = LogFilter(mocked_db_connector)

            for entry in queue:
                log_filter.filter(entry)

            return mocked_db_connector, log_filter

        return dummy

    @pytest.fixture(scope="function")
    def contingency_filter(self):
        """
        Return a filter in contingency state
        :return: Log Filter with mocked database connector
        """
        return self.get_filter(contingency=True)

    @pytest.mark.parametrize("default, high, expected", [
        (0, 0, 1),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1)
    ])
    def test_default_filtering(self, get_filter, default, high, expected):
        """
        Check if dispatch method is called in all cases
        :param default: number of default priority entries
        :param high: number of high priority entries
        :param expected: expected value of dispatched entries
        """

        mocked_db_connector, log_filter = get_filter(default=default, high=high)

        wait_for_dispatch(1)

        assert mocked_db_connector.dispatch.call_count == expected
