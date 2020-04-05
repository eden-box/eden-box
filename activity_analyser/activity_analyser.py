#!/usr/bin/env python3.7

import logging.config

from .activity_filter import ActivityFilter
from .activity_fetcher import ActivityFetcher
from .database_connector import DatabaseConnector
from .activity_analyser_config import ActivityAnalyserConfig


class ActivityAnalyser:
    """
    Fetches activities from an API, filtering relevant information and forwards it to a database
    """

    def __init__(self, config: ActivityAnalyserConfig = None):

        self.custom_fetcher_config = config.activity_fetcher_config()  # to use on run method

        self.logger = logging.getLogger(__name__)

        self.logger.info("Setting up Activity Analyser.")

        self.logger.info("Creating Database connector.")
        self.db_connector = DatabaseConnector(config.database_connector_config())
        self.logger.info("Database connector created.")

        self.logger.info("Creating Activity Filter.")
        self.activity_filter = ActivityFilter(self.db_connector, config=config.activity_filter_config())
        self.logger.info("Log Filter created.")

        self.logger.info("Log Analyser set up.")

    async def run(self):
        """
        Initializes the activity analysis
        Blocks
        """

        self.logger.info("Starting Activity Analyser.")

        self.logger.info("Starting Activity Fetcher.")
        activity_fetcher = ActivityFetcher(self.activity_filter, config=self.custom_fetcher_config)
        self.logger.info("Activity Fetcher timer started.")

        await activity_fetcher.run()  # blocks

        self.logger.info("Activity Fetcher stopped.")

        self.logger.info("Exiting Activity Analyser.")
