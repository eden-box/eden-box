#!/usr/bin/env python3.7

import time
import xmltodict
from .samples import SampleManager
from activity_analyser.activity_filter.activity_filter_config import ActivityFilterConfig  # allow access to round dispatch time config
from activity_analyser.nextcloud_api.api_component.activity.factory.creators import FileAddedActivityCreator


class Methods:

    @staticmethod
    def wait_for_dispatch(rounds):
        """
        Wait for a given number of dispatch rounds to pass
        :param rounds: number of rounds to wait for
        """
        if rounds > 0:
            wait_time = (rounds * ActivityFilterConfig.process_interval()) + 1  # acceptably strict time
            time.sleep(wait_time)

    @classmethod
    def dummy_activity(cls):
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
    def process_queue(log_filter, queue=(), entries=0):
        """
        Utility to make activity_filter process a queue
        If a queue is provided, that is the one to process, if default or high values are set,
        a queue with the requested quantity of entries will be processed.
        :param log_filter: log filter used to process queue
        :param queue: queue to process
        :param entries: number of activities to process
        """
        if entries:
            queue = Methods.dummy_queue(entries)

        for entry in queue:
            log_filter.filter(entry)

    @staticmethod
    def get_dispatched_arguments(mocked_db):
        """
        Obtain a list with all the arguments processed by a mock
        :param mocked_db: mocked database connector
        :return: list of dispatched queues, with dispatched queues being also lists
        """
        call_args_list = mocked_db.dispatch.call_args_list
        args = []
        for arg in call_args_list:
            args.append(list(arg[0][0].queue))
        return args
