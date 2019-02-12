#!/usr/bin/env python3.7

import logging.config
from log_analyser.common import LoggerConfig
from .log_analyser_config import LogAnalyserConfig
from .log_analyser import LogAnalyser

if __name__ == '__main__':

    logging.config.dictConfig(LoggerConfig.logging_config())

    log_analyser = LogAnalyser(LogAnalyserConfig.log_file())

    log_analyser.run()

    exit(0)
