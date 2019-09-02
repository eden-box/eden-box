#! usr/bin/env python3.7

import aiohttp
from urllib.parse import urlunparse


class RequestManager:
    """
    Request Manager of external API connections
    Defines the default connection behaviour to communicate with the external API and also manages
    all the active connections
    """

    def __init__(self, endpoint, user, password):

        self.endpoint = endpoint

        # enforce https to protect authentication data
        self.base_url = urlunparse(("https", endpoint, "", None, None, None))

        self.h_default = {"OCS-APIRequest": "true", "Content-Type": "application/json"}

        self.h_post = {"Content-Type": "application/x-www-form-urlencoded"}

        self.auth_pk = aiohttp.BasicAuth(login=user, password=password)

        self._session = aiohttp.ClientSession(
            auth=self.auth_pk,
            headers=self.h_default,
            timeout=aiohttp.ClientTimeout(total=250)
        )

    async def stop(self):
        """
        Close active session
        """
        await self._session.close()

    async def get(self, url, query_components=()):
        """
        HTTP GET
        :param url: url to contact
        :param query_components: dict with the query parameters
        :return: tuple with response body, headers and request status
        """
        async with self._session.get(url, params=query_components) as resp:
            res = await resp.text()
        return res, resp.headers, resp.status

    async def post(self, url, query_components=(), data=None):
        """
        HTTP POST
        :param url: url to contact
        :param query_components: dict with the query parameters
        :param data: data payload to send
        :return: tuple with response body, headers and request status
        """
        async with self._session.post(url, params=query_components, headers=self.h_post, data=data) as resp:
            res = await resp.text()
        return res, resp.headers, resp.status

    async def put(self, url, query_components=(), data=None):
        """
        HTTP PUT
        :param url: url to contact
        :param query_components: dict with the query parameters
        :param data: data payload to send
        :return: tuple with response body, headers and request status
        """
        async with self._session.put(url, params=query_components, headers=self.h_post, data=data) as resp:
            res = await resp.text()
        return res, resp.headers, resp.status

    async def delete(self, url, query_components=(), data=None):
        """
        HTTP DELETE
        :param url: url to contact
        :param query_components: dict with the query parameters
        :param data: data payload to send
        :return: tuple with response body, headers and request status
        """
        async with self._session.delete(url, params=query_components, headers=self.h_post, data=data) as resp:
            res = await resp.text()
        return res, resp.headers, resp.status
