#!/usr/bin/env python3.7


class ActivityProcessor:
    """
    Requests activity creation to a factory
    Helper required to allow pool processing capabilities for Activity Factory
    """

    @staticmethod
    def create_activity(factory, activity):
        """
        Create an activity using a factory
        :param factory: factory able to process the activity
        :param activity: activity to process
        :return: processed activity list
        """

        activities = []

        if "activity_id" in activity:  # make sure that activity is not a xml metadata object

            activities = factory.create_activity(activity["type"], activity)

        return activities
