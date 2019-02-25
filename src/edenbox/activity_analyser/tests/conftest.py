#!/usr/bin/env python3.7

import pytest
from pytest_mock import mocker
from tests.common import Constants, Methods
from activity_analyser.common.configuration import ConfigManager
from activity_analyser.database_connector import DatabaseConnector


class Helper:
    """
    Helper class used for flexible access to helper methods and constants
    """

    """Helper constants to be used on tests"""
    constants = Constants()

    """Helper methods to be used on tests"""
    methods = Methods()


@pytest.fixture(scope="class")
def helper():
    """
    Return Helper class
    """
    return Helper()


@pytest.fixture(autouse=True, scope="session")
def _setup():
    """
    Initial test setup, run once, for all test sessions
    """
    ConfigManager().set_test()


@pytest.fixture(scope="function")
def mocked_db_connector(mocker):
    """"
    Returns a dummy database connector
    This dummy will serve as an analyser of the method calls issued by the Activity Filter
    """

    mocker.patch.object(DatabaseConnector, "__init__", return_value=None)  # avoid database connection
    mocker.patch.object(DatabaseConnector, "dispatch", return_value=None)  # mock dispatch calls

    db_conn = DatabaseConnector()

    mocker.spy(db_conn, 'dispatch')  # used to access dispatch method calls

    return db_conn
