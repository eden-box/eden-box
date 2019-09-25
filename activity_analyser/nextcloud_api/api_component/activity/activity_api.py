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

    async def get_activities(self, since=None, limit=None, object_type=None, object_id=None, sort=None) -> Activities:
        """
        Return the available activities, filtered based on a set of parameters
        The most recent activity received is defined by the since parameter, from there, all the available activities,
        older than that one, will be gathered until the limit value of activities is reached
        This method arguments correspond to the dict keys expected by the API, and are directly used in the requests,
        therefore, they should not be mindlessly changed.
        :param since: ID of the most recent activity to be received (default behaviour: most recent activity available)
        :param limit: number of activities to be returned (default: 50)
        :param object_type: allows to filter activities to an object type, may only appear together with object_id
        :param object_id: restricts the requested activities to an object id, may only appear together with object_type
        :param sort: order of activities, desc for most recent ones first, "asc" for the opposite (default: desc)
        :return: tuple with response body (XML) and response headers (Dict)
        """

        params = {k: v for k, v in locals().items() if k != "self" and v}  # ignore self object key, None and "" values

        body, headers, status = await self._request_manager.get(url=self._api_url, query_components=params)

        return self.__activity_factory.get_activities(xml_object=body, headers=headers)
