#!/usr/bin/env python3.7

import sys
from pkg_resources import resource_filename
from .log_analyser import LogAnalyser

if __name__ == '__main__':

    config_file = resource_filename(__name__, "config.yaml")

    log_file_name = sys.argv[1]

    log_analyser = LogAnalyser(log_file_name)

    log_analyser.run()

    exit(0)
