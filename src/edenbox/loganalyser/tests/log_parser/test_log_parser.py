#!/usr/bin/env python3.7

import pytest
from log_analyser.log_parser import LogParser
from log_analyser.log_filter import LogFilter
from tests.log_parser.tests_config import Config


@pytest.fixture
def default_log_filter():
    """"
    Returns a dummy LogFilter
    """
    return LogFilter()


@pytest.fixture
def default_log_parser():
    """"
    Returns a dummy LogParser
    """
    return LogParser(Config.DUMMY_FILE, default_log_filter)


class TestLogParserSetup:

    def test_dummy_a(self):
        assert default_log_parser is default_log_parser

    def test_dummy_b(self):
        assert default_log_filter is not default_log_parser
