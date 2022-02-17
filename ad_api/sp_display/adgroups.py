from ..client import Client


class AdGroups(Client):

    def get_ad_groups(self, start_index: int = 0, count: int = None, state_filter: str = "enabled, paused, archived",
                      campaign_id_filter: str = None, ad_group_id_filter: str = None, name: str = None):
        self.uri_path = "/sd/adGroups"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "name": name
        }
        return self.execute()

    def update_ad_groups(self, data):
        self.uri_path = "/sd/adGroups"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_ad_groups(self, data):
        self.uri_path = "/sd/adGroups"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/sd/adGroups/{}".format(ad_group_id)
        self.method = "get"
        return self.execute()

    def delete_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/sd/adGroups/{}".format(ad_group_id)
        self.method = "delete"
        return self.execute()

    def get_ad_group_extended(self, start_index: int = 0, count: int = None,
                              state_filter: str = "enabled, paused, archived",
                              campaign_id_filter: str = None, ad_group_id_filter: str = None, name: str = None):
        self.uri_path = "/sd/adGroups/extended"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "name": name
        }
        return self.execute()

    def get_ad_group_extended_by_id(self, ad_group_id):
        self.uri_path = "/sd/adGroups/extended/{}".format(ad_group_id)
        self.method = "get"
        return self.execute()
