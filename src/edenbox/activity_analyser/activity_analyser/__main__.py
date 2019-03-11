#!/usr/bin/env python3.7

import sentry_sdk
import logging.config
from activity_analyser.common import LoggerConfig
from .activity_analyser import ActivityAnalyser
from .activity_analyser_config import ActivityAnalyserConfig

if __name__ == '__main__':

    sentry_sdk.init(ActivityAnalyserConfig.sentry_dsn())

    logging.config.dictConfig(LoggerConfig.logging_config())

    log_analyser = ActivityAnalyser(ActivityAnalyserConfig.log_file())

    log_analyser.run()

    exit(0)
