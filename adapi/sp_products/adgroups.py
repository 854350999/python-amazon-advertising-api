
from ..adapi import Client


class AdGroup(Client):

    def create_ad_group(self, params):
        self.uri_path = "/v2/sp/adGroups"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_ad_group(self, params):
        self.uri_path = "/v2/sp/adGroups"
        self.method = "put"
        self.data = params
        return self.execute()

    def get_ad_group(self, params):
        self.uri_path = "/v2/sp/adGroups"
        self.data = params
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/v2/sp/adGroups/{}".format(ad_group_id)
        return self.execute()

    def delete_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/v2/sp/adGroups/{}".format(ad_group_id)
        self.method = "delete"
        return self.execute()

    def get_ad_group_extended(self, params):
        self.uri_path = "/v2/sp/adGroups/extended"
        self.data = params
        return self.execute()

    def get_ad_group_extended_by_id(self, ad_group_id):
        self.uri_path = "/v2/sp/adGroups/extended/{}".format(ad_group_id)
        return self.execute()

