#!/usr/bin/env python3.7

import logging.config
from .activity_filter import ActivityFilter
from .activity_fetcher import ActivityFetcher
from .database_connector import DatabaseConnector


class ActivityAnalyser:
    """
    Fetches activities from an API, filtering relevant information and forwards it to a database
    """

    def __init__(self, file_name):

        self.file_name = file_name

        self.logger = logging.getLogger(__name__)

        self.logger.info("Setting up Activity Analyser.")

        self.logger.info("Creating Database connector.")
        self.db_connector = DatabaseConnector()
        self.logger.info("Database connector created.")

        self.logger.info("Creating Activity Filter.")
        self.activity_filter = ActivityFilter(self.db_connector)
        self.logger.info("Log Filter created.")

        self.logger.info("Log Analyser set up.")

    def run(self):
        """
        Initializes the activity analysis
        Blocks
        """

        self.logger.info("Starting Activity Analyser.")

        self.logger.info("Starting Activity Fetcher.")
        activity_fetcher = ActivityFetcher(self.activity_filter)

        activity_fetcher.run()  # blocks

        self.logger.info("Activity Fetcher stopped.")

        self.logger.info("Exiting Activity Analyser.")
