#!/usr/bin/env python3.7

from activity_analyser.common.configuration.config import Config


class __ActivityFetcherConfig(Config):
    """
    Activity Fetcher configuration wrapper
    """

    _identifier = __name__

    def process_interval(self):
        """
        Time, in seconds, between a new set of activities is requested to the API
        """
        return self.get_property("process_interval")

    def endpoint(self):
        return self.get_property("endpoint")

    def username(self):
        return self.get_property("username")

    def password(self):
        return self.get_property("password")

    def max_activities_per_request(self):
        return self.get_property("max_activities_per_request")


ActivityFetcherConfig = __ActivityFetcherConfig()
