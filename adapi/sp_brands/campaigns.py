

from ..adapi import Client


class Campaigns(Client):

    def create_campaigns(self, params):
        self.uri_path = "/sb/campaigns"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_campaigns(self, params):
        self.uri_path = "/sb/campaigns"
        self.method = "put"
        self.data = params
        return self.execute()

    def get_campaigns(self, params):
        self.uri_path = "/sb/campaigns"
        self.data = params
        return self.execute()

    def get_campaigns_by_id(self, campaign_id):
        self.uri_path = "/sb/campaigns/{}".format(campaign_id)
        return self.execute()

    def delete_campaigns_by_id(self, campaign_id):
        self.uri_path = "/sb/campaigns/{}".format(campaign_id)
        self.method = "delete"
        return self.execute()

