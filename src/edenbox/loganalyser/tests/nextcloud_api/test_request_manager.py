#! usr/bin/env python3.7

import pytest
from log_analyser.nextcloud_api import NextcloudApi


@pytest.mark.manual
class TestNextcloudApi:

    @pytest.mark.asyncio
    async def test_api_request(self):
        endpoint = "<host>"
        user = "<user>"
        password = "<password>"
        limit = 100
        since = 1000

        api = NextcloudApi(endpoint=endpoint, user=user, password=password)

        res = await api.activity_api.get_activities(limit=limit, since=since)

        for entry in res.activities:
            print(entry.activity_id)
            print(entry.file)

        assert True
