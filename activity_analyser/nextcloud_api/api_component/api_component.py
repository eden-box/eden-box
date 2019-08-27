#! usr/bin/env python3.7

import abc


class _ApiComponent:
    """
    API component
    Defines the external API url and uses a request manager to handle the connection with it
    """

    """URL to where requests will be sent"""
    _api_url = None

    """Manages generic API requests"""
    _request_manager = None

    def __init__(self, master_api, request_manager):
        self._api_url = master_api.get_full_url(self._endpoint_url)

        self._request_manager = request_manager

    @property
    @abc.abstractmethod
    def _endpoint_url(self):
        """
        API URL, extension of the base URL
        """
        raise NotImplementedError
