#!/usr/bin/env python3.7

import asyncio
import sentry_sdk
import logging.config

from activity_analyser.common import LoggerConfig
from .activity_analyser import ActivityAnalyser
from .activity_analyser_config import ActivityAnalyserConfig


async def main():
    config = ActivityAnalyserConfig()

    sentry_sdk.init(config.sentry_dsn())

    logging.config.dictConfig(LoggerConfig().logging_config())

    log_analyser = ActivityAnalyser(config)

    log_analyser.run()

if __name__ == '__main__':

    asyncio.run(main())

    exit(0)
