

from ..adapi import Client


class Drafts(Client):

    def get_drafts_campaign(self, params):
        self.method = "get"
        self.uri_path = "/sb/drafts/campaigns"
        self.data = params
        return self.execute()

    def create_drafts_campaign(self, params):
        self.uri_path = "/sb/drafts/campaigns"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_drafts_campaign(self, params):
        self.uri_path = "/sb/drafts/campaigns"
        self.method = "put"
        self.data = params
        return self.execute()

    def get_drafts_campaign_by_id(self, draft_campaign_id):
        self.method = "get"
        self.uri_path = "/sb/drafts/campaigns/{}".format(draft_campaign_id)
        return self.execute()

    def delete_drafts_campaign_by_id(self, draft_campaign_id):
        self.uri_path = "/sb/drafts/campaigns/{}".format(draft_campaign_id)
        self.method = "delete"
        return self.execute()

    def submit_drafts_campaign(self, params):
        self.uri_path = "/sb/drafts/campaigns/submit"
        self.method = "post"
        self.data = params
        return self.execute()
