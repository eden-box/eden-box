#!/usr/bin/env python3.7

import pytest
from pytest_mock import mocker
from activity_analyser import ActivityFilter


class TestActivityFilter:

    @pytest.fixture(scope="function")
    def get_filter(self, helper, mocked_db_connector):
        """
        Returns a reference for a method able to generate a filter
        This method is used to overcome the limitation of fixtures of not allowing versatile parametrization of inputs
        :param helper: test helper class
        :param mocked_db_connector: database_connector class, mocked for test suite usage
        :return: a reference for the inner function 'dummy'
        """

        def dummy(activities=0):
            """
            Returns an activity filter, after processing some entries, and the contained mocked db connector
            :param activities: number of activities to process
            :return: activity filter and corresponding mocked db connector
            """

            log_filter = ActivityFilter(
                mocked_db_connector,
                config={
                    "activity_filter": {
                        "process_interval": helper.constants.dummy_process_interval(),
                    }
                }
            )

            helper.methods.process_queue(log_filter, activities=activities)

            return mocked_db_connector, log_filter

        return dummy

    @pytest.mark.parametrize("activities, expected", [
        (0, 0),
        (1, 1)
    ])
    def test_base_filtering(self, helper, get_filter, activities, expected):
        """
        Verify if dispatch method is only called when there are activities to process
        :param helper: test helper class
        :param get_filter: method used to obtain a filter
        :param activities: number of activities to process
        :param expected: expected value of dispatched entries
        """
        mocked_db_connector, log_filter = get_filter()

        helper.methods.process_queue(log_filter, activities=activities)

        helper.methods.wait_for_dispatch(1)

        assert mocked_db_connector.dispatch.call_count == expected
