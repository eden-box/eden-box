#!/usr/bin/env python3.7

from concurrent.futures import ThreadPoolExecutor
from psycopg2 import pool, DatabaseError
from .database_connector_config import DatabaseConnectorConfig as Config
from .exceptions import FailedConnectionException, ConnectionPoolException


class DatabaseConnector:
    """
    Database connection manager
    Establishes connections to the database and processes requests
    """

    def __init__(self):

        self.__thread_pool = ThreadPoolExecutor(max_workers=Config.MAX_WORKERS)

        try:
            self.__connection_pool = pool.ThreadedConnectionPool(
                minconn=Config.MIN_CONNECTIONS,
                maxconn=Config.MAX_CONNECTIONS,
                host=Config.HOST,
                port=Config.PORT,
                database=Config.DATABASE,
                user=Config.USER,
                sslmode=Config.SSL_MODE,
                connect_timeout=Config.TIMEOUT
            )
        except DatabaseError as e:
            raise FailedConnectionException(e, "Failed to establish connection to database")

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
            raise ConnectionPoolException(e, "Unable to obtain connection from pool")
        except DatabaseError as e:
            raise FailedConnectionException(e, "Failed to obtain connection to database")
        finally:
            if conn is not None:
                self.__put_connection(conn)
