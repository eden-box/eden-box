#!/usr/bin/env python3.7

from .log_parser_exception import LogParserException


class NoLogFileException(LogParserException):
    """
    Exception raised when a Log File does not exist
    """
    pass
