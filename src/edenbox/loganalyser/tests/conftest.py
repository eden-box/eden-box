#!/usr/bin/env python3.7

import pytest
from log_analyser.common.configuration import ConfigManager
from tests.common import Constants, Methods


class Helper:
    """
    Helper class used for more flexible access to helper methods and constants
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
