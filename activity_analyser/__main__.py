#!/usr/bin/env python3.7

import sentry_sdk
import logging.config

from activity_analyser.common import LoggerConfig
from .activity_analyser import ActivityAnalyser
from .activity_analyser_config import ActivityAnalyserConfig

if __name__ == '__main__':

    import socket
    def is_connected(hostname):
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname(hostname)
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:
            pass
        return False

    config = ActivityAnalyserConfig()

    print("Connection available: {}.".format(is_connected("www.google.com")))

    print("Sentry DNS value: {}.".format(config.sentry_dsn()))

    sentry_sdk.init(config.sentry_dsn())

    logging.config.dictConfig(LoggerConfig().logging_config())

    log_analyser = ActivityAnalyser(config)

    log_analyser.run()

    exit(0)
