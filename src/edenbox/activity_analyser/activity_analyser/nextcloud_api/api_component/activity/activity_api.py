#! usr/bin/env python3.7

from ..api_component import _ApiComponent
from .factory import ActivityFactory, Activities


class ActivityApi(_ApiComponent):
    """
    Activity API
    Requests activity information to an external API, processes the response and converts it to Activities
    """

    """Path to reach the API, appended to the base URL"""
    _endpoint_url = "/ocs/v2.php/apps/activity/api/v2/activity"

    """Factory able to convert XML dicts to Activities"""
    __activity_factory = ActivityFactory()

    async def get_activities(self, since="", limit="", object_type="", object_id="", sort="") -> Activities:
        """
        Return the available activities, filtered based on a set of parameters
        The most recent activity received is defined by the since parameter, from there, all the available activities,
        older than that one, will be gathered until the limit value of activities is reached
        :param since: ID of the most recent activity to be received (default behaviour: most recent activity available)
        :param limit: number of activities to be returned (default: 50)
        :param object_type: allows to filter activities to an object type, may only appear together with object_id
        :param object_id: restricts the requested activities to an object id, may only appear together with object_type
        :param sort: order of activities, desc for most recent ones first, "asc" for the opposite (default: desc)
        :return: (response body (XML), response headers (Dict))
        """

        params = {
            "since": since,
            "limit": limit,
            "object_type": object_type,
            "object_id": object_id,
            "sort": sort
        }

        body, headers, status = await self._request_manager.get(url=self._api_url, query_components=params)

        return self.__activity_factory.get_activities(xml_object=body, headers=headers)
