#!/usr/bin/env python3.7

import xmltodict
from multiprocessing.pool import ThreadPool
from log_analyser.common import Singleton
from .activities import Activities
from .creators import *


class ActivityFactory(metaclass=Singleton):
    """
    Transforms XML to the correspondent object type

    Converts XML activities to usable objects, depending on the available set of activity creators
    """

    def __init__(self):

        self._activity_creators = {}

        # Initialize available activity creators

        self.__default_entry_creator = DefaultActivityCreator()  # used if no matching creator is found

        for creator in (
                FileAddedActivityCreator(),
                FileRemovedActivityCreator(),
                FileModifiedActivityCreator(),
                FileAccessActivityCreator()
        ):
            creator.register(self)

    def register(self, creator_id, creator):
        """
        Register a creator to the factory
        :param creator_id: id of the added creator
        :param creator: creator to add
        """
        self._activity_creators[creator_id] = creator

    def get_activities(self, headers, xml_object) -> Activities:
        """
        Convert xml to correspondent objects
        :param headers: API request headers
        :param xml_object: xml activity dict
        :return: list of created activity objects
        """

        first = None

        if "X-Activity-First-Known" in headers:
            first = headers["X-Activity-First-Known"]

        last = headers["X-Activity-Last-Given"]

        activities = []

        pool = ThreadPool(processes=4)

        def __add_to_pool(_, activity):
            """
            Add job to Thread Pool
            :param _: unhelpful argument, required for parser callback to work properly
            :param activity: activity converted from XML to a dict
            :return: True, required for parser callback to work properly
            """
            pool.apply_async(func=__process_activity, args=(activity,))
            return True

        def __process_activity(activity):
            """
            If it is an activity, obtain the necessary attributes and create an object
            :param activity: activity converted from xml to dict
            """

            if "activity_id" in activity:  # easy way to make sure that activity is not a xml metadata object

                identifier = activity["type"]

                activities.extend(
                    self._activity_creators.get(identifier, self.__default_entry_creator).create(activity)
                )

        xmltodict.parse(xml_object, item_depth=3, item_callback=__add_to_pool)

        pool.close()
        pool.join()

        activities.sort(key=lambda activity: int(activity.activity_id))  # assure ordered activities, after pool

        return Activities(activities=activities, last=last, first=first)
