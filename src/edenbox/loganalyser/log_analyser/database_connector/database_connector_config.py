#!/usr/bin/env python3.7


class DatabaseConnectorConfig:
    """
    Database Connector configuration
    """

    """max threads used by thread pool"""
    MAX_WORKERS = 4  # TODO configure

    "minimum number of connections in the connection pool"
    MIN_CONNECTIONS = 1  # TODO configure

    "maximum number of connections in the connection pool"
    MAX_CONNECTIONS = 4  # TODO configure

    """host where database is located"""
    HOST = "<host>"  # TODO configure

    """host port to connect to"""
    PORT = "<port>"  # TODO configure

    """database to use"""
    DATABASE = "<database>"  # TODO configure

    """database username"""
    USER = "<user>"  # TODO configure

    """ssl usage definition"""
    SSL_MODE = "verify-full"

    """connection to database timeout, in seconds"""
    TIMEOUT = 60  # TODO configure
