#! usr/bin/env python3.7

from threading import Timer
from .activity_fetcher_config import ActivityFetcherConfig as Config
from ..nextcloud_api import NextcloudApi


class ActivityFetcher:

    """most recent activity already processed"""
    __last_activity = None

    """default limit of activities received per request"""
    __limit = None

    def __init__(self, activity_filter):

        self.__limit = Config.max_activities()

        self.__get_most_recent_activity()

        self.__activity_filter = activity_filter

        self.__api = NextcloudApi(
            endpoint=Config.endpoint(),
            user=Config.username(),
            password=Config.password()
        ).activity_api

        self.__process_timer = Timer(interval=Config.process_interval(), function=self.__process_activities)
        self.__process_timer.daemon = True

    def __get_most_recent_activity(self):
        """
        TODO Load the ID of the last processed activity
        """
        return -1

    def __set_last_activity(self, activity_id):
        """
        Define most recent activity processed, maintaining persistent support
        The new activity_id should and be written to a file, to allow coherent system restart
        :param activity_id: new activity id
        """
        # TODO save id into a file, or similar persistent option
        self.__last_activity = activity_id

    def run(self):
        """
        Initiate periodic requests to external API
        """
        self.__process_timer.start()

    def stop(self):
        """
        Stop periodic requests to external API
        """
        self.__process_timer.cancel()

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

            for activity in iter(stocked_activities):
                self.__activity_filter.filter(activity)

            self.__set_last_activity(new_most_recent)
