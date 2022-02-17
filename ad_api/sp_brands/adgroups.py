

from ..client import Client


class AdGroups(Client):

    def get_ad_groups(self, start_index: int = 0, count: int = None, name: str = None, ad_group_id_filter: str = None,
                      campaign_id_filter: str = None, creative_type: str = None):
        """
        Gets an array of ad groups associated with the client identifier passed in the authorization header,
        filtered by specified criteria.
        :param start_index: Sets a zero-based offset into the requested set of ad groups. Use in conjunction with
        the count parameter to control pagination of the returned array. default:0
        :param count: Sets the number of ad groups in the returned array. Use in conjunction with the startIndex
        parameter to control pagination. For example, to return the first ten ad groups set startIndex=0 and
        count=10. To return the next ten ad groups, set startIndex=10 and count=10, and so on. default: max
        :param name:The returned array includes only ad groups with the specified name.
        :param ad_group_id_filter:The returned array includes only ad groups with identifiers matching those
        specified in the comma-delimited string.
        :param campaign_id_filter:The returned array includes only ad groups associated with campaign identifiers
        matching those specified in the comma-delimited string.
        :param creative_type:Filter by the type of creative the campaign is associated with. To get ad groups
        associated with non-video campaigns specify 'productCollection'. To get ad groups associated with video
        campaigns, this must be set to 'video'. Returns all ad groups if not specified.
        :return:
        """
        self.uri_path = "/sb/adGroups"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "name": name,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
            "creativeType": creative_type
        }
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        """
        Gets an ad group specified by identifier.
        :param ad_group_id: The identifier of an existing ad group.
        :return:
        """
        self.uri_path = "/sb/adGroups/{}".format(ad_group_id)
        self.method = "get"
        return self.execute()

