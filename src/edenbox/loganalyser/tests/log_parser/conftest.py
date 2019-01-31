#!/usr/bin/env python3.7

import pytest
from log_analyser.log_filter import LogFilter
from log_analyser.log_parser import LogParser


@pytest.fixture(scope="function")
def default_file(tmpdir):
    """"
    Returns a dummy log file
    """
    file_n = tmpdir.join("dummy_file.txt")
    file_n.write("")  # force file creation
    return file_n


@pytest.fixture(scope="function")
def default_log_filter(mocked_db_connector):
    """"
    Returns a dummy LogFilter
    """
    return LogFilter(mocked_db_connector)


@pytest.fixture(scope="function")
def default_log_parser(default_file, default_log_filter):
    """"
    Returns a dummy LogParser
    """
    log_parser = LogParser(default_file.realpath(), default_log_filter)
    log_parser.run(keepalive=False)
    return log_parser
