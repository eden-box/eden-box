#!/usr/bin/env python3.7

import pytest
from pytest_mock import mocker
from log_analyser import DatabaseConnector, LogFilter


class TestLogFilter:

    @pytest.fixture(scope="function")
    def mocked_db_connector(self, mocker):
        """"
        Returns a dummy database connector
        This dummy will serve as an analyser of the method calls issued by the Log Filter
        """

        mocker.patch.object(DatabaseConnector, "__init__", return_value=None)  # avoid database connection
        mocker.patch.object(DatabaseConnector, "dispatch", return_value=None)  # mock dispatch calls

        db_conn = DatabaseConnector()

        mocker.spy(db_conn, 'dispatch')  # used to access dispatch method calls

        return db_conn

    @pytest.fixture(scope="function")
    def get_filter(self, helper, mocked_db_connector):
        """
        Returns a reference for a method able to generate a filter
        This method is used to overcome the limitation of fixtures of not allowing versatile parametrization of inputs
        :param helper:
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

            if contingency:  # if contingency is requested, fill the queue with default priority entries
                default += helper.constants.max_default_entries() + 1

            d_queue = helper.methods.dummy_queue(default, high)

            log_filter = LogFilter(mocked_db_connector)

            for entry in d_queue:
                log_filter.filter(entry)

            return mocked_db_connector, log_filter

        return dummy

    def test_config(self, helper):
        """
        Limit of default priority entries must be superior to the limit of high priority entries
        """
        assert helper.constants.max_default_entries() >= helper.constants.max_high_entries()

    def test_initial_state(self, helper, get_filter):
        """
        Verify if the initial state of the filter is default
        """

        mocked_db_connector, log_filter = get_filter()

        assert helper.methods.in_default_state(log_filter)

    @pytest.mark.parametrize("default, high, expected", [
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1)
    ])
    def test_base_filtering(self, helper, get_filter, default, high, expected):
        """
        Verify if dispatch method is called in all cases
        :param default: number of default priority entries
        :param high: number of high priority entries
        :param expected: expected value of dispatched entries
        """

        mocked_db_connector, log_filter = get_filter()

        helper.methods.process_queue(log_filter, default=default, high=high)

        helper.methods.wait_for_dispatch(1)

        assert mocked_db_connector.dispatch.call_count == expected

    def test_no_contingency_default(self, helper, get_filter):
        """
        Verify if processing the limit number of default priority entries does not trigger contingency
        """

        mocked_db_connector, log_filter = get_filter()

        assert helper.methods.in_default_state(log_filter)

        helper.methods.process_queue(log_filter, default=helper.constants.max_default_entries())

        assert helper.methods.in_default_state(log_filter)

    def test_enter_contingency_default(self, helper, get_filter):
        """
        Verify if surpassing the limit number of processed default priority entries triggers contingency
        """

        mocked_db_connector, log_filter = get_filter()

        assert helper.methods.in_default_state(log_filter)

        helper.methods.process_queue(log_filter, default=helper.constants.max_default_entries() + 1)

        assert helper.methods.in_contingency_state(log_filter)

    def test_no_contingency_high(self, helper, get_filter):
        """
        Verify if processing the limit number of high priority entries does not trigger contingency
        """

        mocked_db_connector, log_filter = get_filter()

        assert helper.methods.in_default_state(log_filter)

        helper.methods.process_queue(log_filter, high=helper.constants.max_high_entries())

        assert helper.methods.in_default_state(log_filter)

    def test_enter_contingency_high(self, helper, get_filter):
        """
        Verify if surpassing the limit number of processed high priority entries triggers contingency
        """

        mocked_db_connector, log_filter = get_filter()

        assert helper.methods.in_default_state(log_filter)

        helper.methods.process_queue(log_filter, high=helper.constants.max_high_entries() + 1)

        assert helper.methods.in_contingency_state(log_filter)

    @pytest.mark.parametrize("default_entry, expected", [
        (True, 0),
        (False, 1)
    ])
    def test_contingency(self, helper, get_filter, default_entry, expected):
        """
        Verify if in contingency state only high priority entries are processed
        :param default_entry: True for a default entry, False for a high priority entry
        :param expected: expected value of dispatched entries
        """

        mocked_db_connector, log_filter = get_filter(contingency=True)

        entry = helper.methods.dummy_entry(default_entry)

        log_filter.filter(entry)

        helper.methods.wait_for_dispatch(1)

        assert mocked_db_connector.dispatch.call_count == expected

    def test_contingency_transition(self, helper, get_filter):
        """
        Verify if a high priority entry added during default state, is processed after contingency is triggered
        """

        mocked_db_connector, log_filter = get_filter()

        high_entry = helper.methods.dummy_entry(False)

        log_filter.filter(high_entry)

        helper.methods.process_queue(log_filter, default=helper.constants.max_default_entries())

        helper.methods.wait_for_dispatch(1)

        args_list = helper.methods.get_dispatched_arguments(mocked_db_connector)

        expected_args_list = [[high_entry]]

        assert args_list == expected_args_list

    def test_recovery(self, helper, get_filter):
        """
        Verify if the log filter can return to default state, after contingency
        """

        mocked_db_connector, log_filter = get_filter(contingency=True)

        assert helper.methods.in_contingency_state(log_filter)

        helper.methods.wait_for_dispatch(1)

        assert helper.methods.in_default_state(log_filter)

    def test_retrigger(self, helper, get_filter):
        """
        Verify if after triggering contingency and returning to default, contingency can be triggered again
        """

        mocked_db_connector, log_filter = get_filter(contingency=True)

        assert helper.methods.in_contingency_state(log_filter)

        helper.methods.wait_for_dispatch(1)

        assert helper.methods.in_default_state(log_filter)

        d_queue = helper.methods.dummy_queue(helper.constants.max_default_entries() + 1, 0)

        helper.methods.process_queue(log_filter, d_queue)

        assert helper.methods.in_contingency_state(log_filter)
