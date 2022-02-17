

from ..client import Client


class AdGroups(Client):

    def get_ad_groups(self, start_index: int = 0, count: int = None, name: str = None, ad_group_id_filter: str = None,
                      campaign_id_filter: str = None, creative_type: str = None):
        self.uri_path = "/sb/adGroups"
        self.method = "get"
        self.data = {
            "startIndex": start_index,
            "count": count,
            "name": name,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter,
            "creativeType": creative_type
        }
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/sb/adGroups/{}".format(ad_group_id)
        self.method = "get"
        return self.execute()

