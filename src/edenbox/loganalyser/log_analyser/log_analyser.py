#!/usr/bin/env python3.7

import logging.config
from .log_filter import LogFilter
from .log_parser import LogParser
from .database_connector import DatabaseConnector


class LogAnalyser:

    def __init__(self, file_name):

        self.file_name = file_name

        self.db_connector = DatabaseConnector()
        self.log_filter = LogFilter(self.db_connector)

    def run(self):

        self.logger.info("Starting Log Analyser")

        LogParser(self.file_name, self.log_filter)  # blocks for parsing

        self.logger.info("Exiting Log Analyser")
