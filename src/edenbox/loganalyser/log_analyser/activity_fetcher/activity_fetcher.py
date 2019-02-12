#! usr/bin/env python3.7

import logging
from threading import Timer
from pkg_resources import resource_filename
from ..nextcloud_api import NextcloudApi
from log_analyser.common.configuration import loader
from .activity_fetcher_config import ActivityFetcherConfig as Config

logger = logging.getLogger(__name__)


class ActivityFetcher:
    """
    Activity Fetcher
    Periodically requests activity updates to an external API, processes the response
    and forwards it to the activity filter
    """

    """most recent activity already processed"""
    __last_activity = None

    """default limit of activities received per request"""
    __limit = None

    def __init__(self, activity_filter):

        self.__state_file_path = resource_filename(__name__, "last_activity.yaml")

        self.__load_most_recent_activity()

        self.__limit = Config.max_activities()

        self.__activity_filter = activity_filter

        self.__base_api = NextcloudApi(
            endpoint=Config.endpoint(),
            user=Config.username(),
            password=Config.password()
        )

        self.__api = self.__base_api.activity_api

        self.__process_timer = Timer(interval=Config.process_interval(), function=self.__process_activities)
        self.__process_timer.daemon = True

    def __load_most_recent_activity(self):
        """
        Load the most recently processed activity id
        """
        config = loader.get_config(self.__state_file_path)
        self.__last_activity = config.get("last_activity")
        logger.info("Loaded activity with id: %s.", self.__last_activity)

    def __set_last_activity(self, activity_id):
        """
        Define most recent activity processed, maintaining persistent support
        The new activity_id should and be written to a file, to allow coherent system restart
        :param activity_id: new activity id
        """
        loader.save_config(
            self.__state_file_path,
            {"last_activity": activity_id}
        )
        self.__last_activity = activity_id

    def run(self, keepalive=True):
        """
        Initiate periodic requests to external API
        :param keepalive: if True, the
        """
        self.__process_timer.start()
        logger.info("Activity Fetcher is operational.")

        if keepalive:
            self.__process_timer.join()
            self.stop()

    def stop(self):
        """
        Stop periodic requests to external API and close connections
        """
        self.__process_timer.cancel()
        self.__base_api.stop()
        logger.info("Activity Fetcher has been stopped.")

    def __process_activities(self):

        limit = self.__limit

        most_recent = self.__last_activity

        activities = await self.__api.get_activities(limit=limit)

        if activities.first > most_recent:

            new_most_recent = activities.first

            stocked_activities = [activities]

            while activities.last > most_recent:
                since = activities.last
                activities = await self.__api.get_activities(since=since, limit=limit)
                stocked_activities.append(activities)

            # remove previously processed entries, if they exist
            if most_recent > activities.last:
                stocked_activities[-1].filter(most_recent)

            stocked_activities = stocked_activities[0].merge_activities(stocked_activities[1:])

            for activity in iter(stocked_activities.activities):
                self.__activity_filter.filter(activity)

            self.__set_last_activity(new_most_recent)
