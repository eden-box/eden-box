#!/usr/bin/env python3.7

import abc
from dateutil import parser


class _ActivityCreator(metaclass=abc.ABCMeta):
    """
    Creates activity objects depending on the provided xml dict
    """

    @property
    @abc.abstractmethod
    def _identifier(self):
        """
        Identifies the create objects, correspondent to json entry representation
        """
        raise NotImplementedError

    def register(self, activity_factory):
        """
        Register this creator in a factory
        :param activity_factory: activity factory
        """
        activity_factory.register(self._identifier, self)

    def create(self, xml_dict):
        """
        Create activity objects
        :param xml_dict: xml activity dict
        :return: list of activity objects
        """
        return self._parse_activity(xml_dict)

    def _parse_activity(self, xml_dict):
        """
        Returns activity objects of a specific type
        :param xml_dict: xml activity dict
        :return: activity objects
        """
        activity_id = xml_dict["activity_id"]
        time = xml_dict["datetime"]

        activities = []

        elements = xml_dict["objects"]["element"]

        if not isinstance(elements, list):
            elements = [elements]

        for file in elements:
            activity = self._return_activity(
                activity_id=int(activity_id),
                timestamp=parser.parse(time),
                file=file,
                xml_dict=xml_dict
            )
            if activity:
                activities.append(activity)

        return activities

    @abc.abstractmethod
    def _return_activity(self, activity_id, timestamp, file, xml_dict):
        """
        Returns activity objects of a specific type
        :param activity_id: activity id
        :param timestamp: activity timestamp
        :param file: file which the activity refers to
        :param xml_dict: xml activity dict
        :return: activity objects
        """
        pass
