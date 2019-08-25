#!/usr/bin/env python3.7

import logging
from concurrent.futures import ThreadPoolExecutor
from psycopg2 import pool, DatabaseError
from .database_connector_config import DatabaseConnectorConfig
from .exceptions import FailedConnectionException, ConnectionPoolException

logger = logging.getLogger(__name__)


class DatabaseConnector:
    """
    Database connection manager
    Establishes connections to the database and processes requests
    """

    def __init__(self, config=None):

        config = DatabaseConnectorConfig(config)

        self.__thread_pool = ThreadPoolExecutor(max_workers=config.max_workers())

        try:
            self.__connection_pool = pool.ThreadedConnectionPool(
                minconn=config.min_connections(),
                maxconn=config.max_connections(),
                host=config.host(),
                port=config.port(),
                dbname=config.database(),
                user=config.user(),
                sslmode=config.ssl_mode(),
                connect_timeout=config.timeout()
            )
        except DatabaseError as e:
            logger.critical("Failed to establish connection to database.")
            raise FailedConnectionException(e, "Failed to establish connection to database.")

    def __get_connection(self):
        """
        Obtain a connection to the database
        :return: free connection from the pool
        """
        return self.__connection_pool.getconn()

    def __put_connection(self, connection):
        """
        Return connection to the pool
        :param connection: to return to the pool
        """
        self.__connection_pool.putconn(connection)

    def dispatch(self, queue):
        """
        Submit request to dispatch queue
        :param queue: to dispatch
        """
        self.__thread_pool.submit(self.__dispatch_queue, queue)

    def __dispatch_queue(self, queue):
        """
        Process queue of requests to database
        :param queue: to dispatch
        """

        conn = None

        try:
            conn = self.__get_connection()

            cur = conn.cursor()
            for entry in iter(queue.get, queue.empty()):
                entry.dispatch(cur)
                conn.commit()
            cur.close()
        except pool.PoolError as e:
            logger.warning("Unable to obtain connection from pool.")
            raise ConnectionPoolException(e, "Unable to obtain connection from pool.")
        except DatabaseError as e:
            logger.warning("Failed to obtain connection to database.")
            raise FailedConnectionException(e, "Failed to obtain connection to database.")
        finally:
            if conn:
                self.__put_connection(conn)
