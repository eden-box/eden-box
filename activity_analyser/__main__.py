#!/usr/bin/env python3.7

import asyncio
import logging.config
import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

from activity_analyser.common import LoggerConfig
from .activity_analyser import ActivityAnalyser
from .activity_analyser_config import ActivityAnalyserConfig


async def main():
    config = ActivityAnalyserConfig()

    sentry_sdk.init(
        dsn=config.sentry_dsn(),
        integrations=[AioHttpIntegration()]
    )

    logging.config.dictConfig(LoggerConfig().logging_config())

    log_analyser = ActivityAnalyser(config)

    await log_analyser.run()

if __name__ == '__main__':

    asyncio.run(main())

    exit(0)
