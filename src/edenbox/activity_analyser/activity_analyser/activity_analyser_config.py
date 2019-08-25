#!/usr/bin/env python3.7

from .common.configuration.config import Config


class ActivityAnalyserConfig(Config):
    """
    Log Analyser configuration wrapper
    """

    _identifier = __name__

    _config_section = "activity_analyser"

    def sentry_dsn(self):
        return self.get_property("sentry_dsn")

    def activity_fetcher_config(self):
        return self.get_property("activity_fetcher")

    def activity_filter_config(self):
        return self.get_property("activity_filter")

    def database_connector_config(self):
        return self.get_property("database_connector")
