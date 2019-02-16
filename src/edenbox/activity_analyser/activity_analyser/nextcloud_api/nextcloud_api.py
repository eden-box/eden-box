#! usr/bin/env python3.7

from urllib.parse import urlunparse
from .api_component import ActivityApi
from .request_manager import RequestManager


class NextcloudApi:
    """
    Interface of Nextcloud APIs
    Manages the available Nextcloud APIs and required external connections
    """

    def __init__(self, endpoint, user, password):
        """
        Defines the URL of the API host and establishes the required basic authentication data
        :param endpoint: base URL of the host
        :param user: application username
        :param password: application password
        """

        self._endpoint = endpoint

        self._request_manager = RequestManager(endpoint=endpoint, user=user, password=password)

        self.__api = {
            "activity": ActivityApi(self, self._request_manager)
        }

    async def stop(self):
        """
        Requests API session to be closed
        """
        await self._request_manager.stop()

    def get_full_url(self, api_url):
        """
        Provides the request URL, after appending a specific API path
        :param api_url: api url path, to use as extension to base url
        :return: complete API URL
        """
        return urlunparse(("https", self._endpoint, api_url, None, None, None))

    def __get_api(self, identifier):
        """
        Obtain the requested Nextcloud API
        :param identifier: identifier of the API
        :return: requested API
        """
        return self.__api.get(identifier)

    @property
    def activity_api(self) -> ActivityApi:
        """
        Activity API
        :return: Activity API component
        """
        return self.__get_api("activity")
