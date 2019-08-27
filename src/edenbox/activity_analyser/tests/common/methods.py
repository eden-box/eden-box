#!/usr/bin/env python3.7

import time
import xmltodict

from .samples import SampleManager
from .constants import Constants
from activity_analyser.nextcloud_api.api_component.activity.factory.creators import FileAddedActivityCreator


class Methods:

    @staticmethod
    def wait_for_dispatch(rounds):
        """
        Wait for a given number of dispatch rounds to pass
        :param rounds: number of rounds to wait
        """
        if rounds > 0:
            wait_time = (rounds * Constants.dummy_process_interval()) + 1  # strict time, test value of process_time
            time.sleep(wait_time)

    @staticmethod
    def dummy_activity():
        """
        Obtain a dummy activity
        :return: added file activity
        """
        activity = SampleManager.get_added_file_activity()
        creator = FileAddedActivityCreator()
        xml_activity = xmltodict.parse(activity)["element"]
        return creator.create(xml_dict=xml_activity)[0]

    @staticmethod
    def dummy_queue(activities=0):
        """
        Obtain a list of entries
        The list contains the requested default priority entries followed by the high priority entries
        :param activities: number of dummy activities to process
        :return: list of entries
        """

        entries = []

        for i in range(activities):
            dummy = Methods.dummy_activity()
            entries.append(dummy)

        return entries

    @staticmethod
    def process_queue(activity_filter, queue=(), activities=0):
        """
        Utility to make activity_filter process a queue
        If a queue is provided, that is the one to process, if default or high values are set,
        a queue with the requested quantity of entries will be processed.
        :param activity_filter: filter used to process queue
        :param queue: queue to process
        :param activities: number of activities to process
        """
        if activities:
            queue = Methods.dummy_queue(activities)

        for activity in queue:
            activity_filter.filter(activity)

    @staticmethod
    def get_dispatched_arguments(mocked_db):
        """
        Obtain a list with all the arguments processed by a mock
        :param mocked_db: mocked database connector
        :return: list of dispatched queues, with dispatched queues being also lists
        """
        call_args_list = mocked_db.dispatch.call_args_list
        return [[arg[0][0].queue] for arg in call_args_list]
