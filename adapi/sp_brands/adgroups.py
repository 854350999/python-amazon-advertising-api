

from ..adapi import Client


class AdGroups(Client):

    def get_ad_groups(self, params):
        self.uri_path = "/sb/adGroups"
        self.data = params
        return self.execute()

    def get_ad_group_by_id(self, ad_group_id):
        self.uri_path = "/sb/adGroups/{}".format(ad_group_id)
        return self.execute()

