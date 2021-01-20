

from ..adapi import Client


class AdGroups(Client):

    def get_ad_groups(self, params):
        self.method = "get"
        self.uri_path = "/sd/adGroups"
        self.data = params
        return self.execute()

    def update_ad_groups(self, params):
        self.uri_path = "/sd/adGroups"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_ad_groups(self, params):
        self.uri_path = "/sd/adGroups"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/sd/adGroups/{}".format(ad_group_id)
        return self.execute()

    def delete_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/sd/adGroups/{}".format(ad_group_id)
        self.method = "delete"
        return self.execute()

    def get_ad_group_extended(self, params):
        self.method = "get"
        self.uri_path = "/sd/adGroups/extended"
        self.data = params
        return self.execute()

    def get_ad_group_extended_by_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/sd/adGroups/extended/{}".format(ad_group_id)
        return self.execute()
