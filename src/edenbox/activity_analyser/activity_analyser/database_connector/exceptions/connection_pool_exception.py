#!/usr/bin/env python3.7

from .database_connector_exception import DatabaseConnectorException


class ConnectionPoolException(DatabaseConnectorException):
    """
    Exception raised on connection pool failure
    """
    pass
