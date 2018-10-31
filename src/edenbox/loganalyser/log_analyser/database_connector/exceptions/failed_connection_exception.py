#!/usr/bin/env python3.7

from .database_connector_exception import DatabaseConnectorException


class FailedConnectionException(DatabaseConnectorException):
    """
    Exception raised on connection establishment failure
    """
    pass
