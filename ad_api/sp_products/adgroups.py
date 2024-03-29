from ..client import Client


class AdGroups(Client):

    def create_ad_group(self, data):
        self.uri_path = "/v2/sp/adGroups"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_ad_group(self, data):
        self.uri_path = "/v2/sp/adGroups"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_ad_group(self, start_index: int = 0, count: int = None, campaign_type: str = None, state_filter: str = None,
                     name: str = None, campaign_id_filter: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups"
        queries = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "campaignType": campaign_type,
            "campaignIdFilter": campaign_id_filter,
        }
        self.params = queries
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}".format(ad_group_id)
        return self.execute()

    def delete_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/v2/sp/adGroups/{}".format(ad_group_id)
        self.method = "delete"
        return self.execute()

    def get_ad_group_extended(self, start_index: int = 0, count: int = None, campaign_type: str = None,
                              state_filter: str = None,
                              name: str = None, campaign_id_filter: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/extended"
        queries = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "campaignType": campaign_type,
            "campaignIdFilter": campaign_id_filter,
        }
        self.params = queries
        return self.execute()

    def get_ad_group_extended_by_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/extended/{}".format(ad_group_id)
        return self.execute()


class AdGroupsV3(Client):

    def create_ad_groups(self, data):
        self.method = "post"
        self.uri_path = "/sp/adGroups"
        self.data = data
        return self.execute()

    def get_ad_groups_list(self, data):
        self.method = "post"
        self.uri_path = "/sp/campaigns/list"
        self.data = data
        return self.execute()

    def update_ad_groups(self, data):
        self.method = "put"
        self.uri_path = "/sp/adGroups"
        self.data = data
        return self.execute()

    def delete_ad_groups(self, data):
        self.method = "post"
        self.uri_path = "/sp/adGroups/delete"
        self.data = data
        return self.execute()
