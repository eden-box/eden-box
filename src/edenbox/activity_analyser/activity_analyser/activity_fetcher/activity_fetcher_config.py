#!/usr/bin/env python3.7

from pkg_resources import resource_filename
from activity_analyser.common.configuration.config import Config


class __ActivityFetcherConfig(Config):
    """
    Activity Fetcher configuration wrapper
    """

    _identifier = __name__

    _file_path = resource_filename(__name__, "config.yaml")

    def process_interval(self):
        return self.get_property("process_interval")

    def endpoint(self):
        return self.get_property("endpoint")

    def username(self):
        return self.get_property("username")

    def password(self):
        return self.get_property("password")

    def max_activities(self):
        return self.get_property("max_activities")


ActivityFetcherConfig = __ActivityFetcherConfig()
