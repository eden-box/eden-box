#!/usr/bin/env python3.7

import sys
import logging.config
from .log_analyser_config import LogAnalyserConfig as Config
from .log_analyser import LogAnalyser

if __name__ == '__main__':

    logging.config.dictConfig(Config.logging_file)

    log_file_name = sys.argv[1]

    log_analyser = LogAnalyser(log_file_name)

    log_analyser.run()

    exit(0)
