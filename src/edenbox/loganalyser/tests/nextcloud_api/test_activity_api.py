#! usr/bin/env python3.7

import pytest
from log_analyser.nextcloud_api import NextcloudApi


@pytest.mark.manual
class TestActivityApi:

    @pytest.mark.asyncio
    async def test_api_request(self):
        endpoint = "<host>"
        user = "<user>"
        password = "<password>"
        limit = 100
        since = 1000

        api = NextcloudApi(endpoint=endpoint, user=user, password=password)

        res = await api.activity_api.get_activities(limit=limit, since=since)

        for activity in res.activities:
            msg = "\nID: {} \n File: {} \n Timestamp: {}".format(activity.activity_id, activity.file, activity.time)
            print(msg)

        assert True
