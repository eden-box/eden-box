#! usr/bin/env python3.7

import aiohttp
from urllib.parse import urlunparse


class RequestManager:
    """
    Request Manager of external API connections
    Defines the default connection behaviour to communicate with the external API and manages
    all the active connections
    """

    def __init__(self, endpoint, user, password):

        self.endpoint = endpoint

        # enforce https to protect the authentication data
        self.base_url = urlunparse(("https", endpoint, "", None, None, None))

        self.h_default = {"OCS-APIRequest": "true", "Content-Type": "application/json"}

        self.h_post = {"Content-Type": "application/x-www-form-urlencoded"}

        self.auth_pk = aiohttp.BasicAuth(login=user, password=password)

        self._session = aiohttp.ClientSession(auth=self.auth_pk, headers=self.h_default)

    async def get(self, url, query_components=()):
        async with self._session.get(url, params=query_components) as resp:
            res = await resp.text()
        return res, resp.headers

    async def post(self, url, query_components=(), data=None):
        async with self._session.post(url, params=query_components, headers=self.h_post, data=data) as resp:
            res = await resp.text()
        return res, resp.headers

    async def put(self, url, query_components=(), data=None):
        async with self._session.put(url, params=query_components, headers=self.h_post, data=data) as resp:
            res = await resp.text()
        return res, resp.headers

    async def delete(self, url, query_components=(), data=None):
        async with self._session.delete(url, params=query_components, headers=self.h_post, data=data) as resp:
            res = await resp.text()
        return res, resp.headers
