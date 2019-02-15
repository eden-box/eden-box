#!/usr/bin/env python3.7

import logging.config
from .activity_filter import ActivityFilter
from .activity_fetcher import ActivityFetcher
from .database_connector import DatabaseConnector


class ActivityAnalyser:
    """
    Parses a log file, filtering relevant entries and forwards them to a database
    """

    def __init__(self, file_name):

        self.file_name = file_name

        self.logger = logging.getLogger(__name__)

        self.logger.info("Setting up Activity Analyser")

        self.logger.info("Creating Database connector")
        self.db_connector = DatabaseConnector()
        self.logger.info("Database connector created")

        self.logger.info("Creating Activity Filter")
        self.log_filter = ActivityFilter(self.db_connector)
        self.logger.info("Log Filter created")

        self.logger.info("Log Analyser set up")

    def run(self):
        """
        Initializes the log analysis
        Blocks while filtering the log file
        """

        self.logger.info("Starting Activity Analyser")

        self.logger.info("Starting Activity Fetcher")
        log_parser = ActivityFetcher(self.log_filter)

        log_parser.run()  # blocks for parsing

        self.logger.info("Activity Fetcher stopped")

        self.logger.info("Exiting Activity Analyser")
