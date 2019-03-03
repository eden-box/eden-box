#!/usr/bin/env python3.7

from .common.configuration.config import Config


class __ActivityAnalyserConfig(Config):
    """
    Log Analyser configuration wrapper
    """

    _identifier = __name__

    def sentry_dsn(self):
        return self.get_property("sentry_dsn")

    def log_file(self):
        return self.get_property("log_file")


ActivityAnalyserConfig = __ActivityAnalyserConfig()
