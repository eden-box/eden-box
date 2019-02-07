#!/usr/bin/env python3.7

import xmltodict
from multiprocessing import Pool
from .creators import *
from .activities import Activities
from log_analyser.common import Singleton
from .activity_processor import ActivityProcessor


class ActivityFactory(metaclass=Singleton):
    """
    Transforms XML to the correspondent object type

    Converts XML activities to objects, depending on the available set of activity creators
    """

    def __init__(self):

        self.__activity_creators = {}

        # Initialize available activity creators

        self.__default_entry_creator = DefaultActivityCreator()  # used if no matching creator is found

        for creator in (
                FileAddedActivityCreator(),
                FileRemovedActivityCreator(),
                FileModifiedActivityCreator(),
                FileAccessActivityCreator()
        ):
            creator.register(self)

    def __get_creator(self, creator_id):
        """
        Return a creator identifiable by the provided parameter
        :param creator_id: id of the creator
        :return: returns the creator identified by creator_id, otherwise an innocuous creator is returned
        """
        return self.__activity_creators.get(creator_id, self.__default_entry_creator)

    def register(self, creator_id, creator):
        """
        Register a creator to the factory
        :param creator_id: id of the added creator
        :param creator: creator to add
        """
        self.__activity_creators[creator_id] = creator

    def create_activity(self, creator_id, activity):
        """
        Create an activity using and appropriate creator
        :param creator_id: identifier of the type of object
        :param activity: unprocessed activity
        :return: activity object
        """
        return self.__get_creator(creator_id).create(activity)

    @staticmethod
    def __get_activity_id(activity):
        """
        Helper method to obtain activity id
        Used as key for activity list sorting
        :param activity: activity
        :return: activity id
        """
        return activity.activity_id

    def get_activities(self, headers, xml_object) -> Activities:
        """
        Convert xml to correspondent objects
        :param headers: API request headers, a CIMultiDict
        :param xml_object: xml activity dict
        :return: list of created activity objects
        """

        # defaults to None, if key does not exist
        first = headers.get("X-Activity-First-Known")

        last = headers.get("X-Activity-Last-Given")

        activities = []

        pool = Pool(processes=4)

        def __add_activities(activity):
            """
            Add processed activity object to activities list
            :param activity: processed activity
            """
            activities.extend(activity)

        def __add_to_pool(_, activity):
            """
            Add job to process Pool
            :param _: unhelpful argument, required for parser callback to work properly
            :param activity: activity converted from XML to a dict
            :return: True, required for parser callback to work properly
            """
            pool.apply_async(func=ActivityProcessor.create_activity, args=(self, activity), callback=__add_activities)
            return True

        xmltodict.parse(xml_object, item_depth=3, item_callback=__add_to_pool)

        pool.close()
        pool.join()

        activities.sort(key=self.__get_activity_id)  # assure ordered activities, after pool

        return Activities(activities=activities, last=last, first=first)
