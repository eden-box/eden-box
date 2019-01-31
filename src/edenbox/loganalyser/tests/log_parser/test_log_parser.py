#!/usr/bin/env python3.7

import pytest
from log_analyser.log_parser import LogParser, NoLogFileException


class TestLogParser:

    def test_no_file_exception(self, default_log_filter):
        with pytest.raises(NoLogFileException):
            LogParser("wrong_path.txt", default_log_filter)
