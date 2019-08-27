#!/usr/bin/env python3.7

from pkg_resources import resource_filename


class SampleManager:

    @staticmethod
    def __get_activity(file_path):

        file_path = resource_filename(__name__, file_path)

        with open(file_path, 'r') as f:
            return f.read()

    @staticmethod
    def get_access_file_activity():
        return SampleManager.__get_activity("file_access.xml")

    @staticmethod
    def get_added_file_activity():
        return SampleManager.__get_activity("file_added.xml")

    @staticmethod
    def get_changed_file_activity():
        return SampleManager.__get_activity("file_changed.xml")

    @staticmethod
    def get_deleted_file_activity():
        return SampleManager.__get_activity("file_deleted.xml")

    @staticmethod
    def get_moved_file_activity():
        return SampleManager.__get_activity("file_moved.xml")

    @staticmethod
    def get_renamed_file_activity():
        return SampleManager.__get_activity("file_renamed.xml")

    @staticmethod
    def get_restored_file_activity():
        return SampleManager.__get_activity("file_restored.xml")
