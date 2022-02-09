

from ..client import Client


class Drafts(Client):

    def get_drafts_campaign(self, start_index: int = 0, count: int = None, name: str = None,
                            draft_campaign_id_filter: str = None, portfolio_id_filter: str = None,
                            ad_format_filter: str = None):
        self.method = "get"
        self.uri_path = "/sb/drafts/campaigns"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "name": name,
            "draftCampaignIdFilter": draft_campaign_id_filter,
            "portfolioIdFilter": portfolio_id_filter,
            "adFormatFilter": ad_format_filter
        }
        return self.execute()

    def create_drafts_campaign(self, data):
        self.uri_path = "/sb/drafts/campaigns"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_drafts_campaign(self, data):
        self.uri_path = "/sb/drafts/campaigns"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_drafts_campaign_by_id(self, draft_campaign_id):
        self.method = "get"
        self.uri_path = "/sb/drafts/campaigns/{}".format(draft_campaign_id)
        return self.execute()

    def delete_drafts_campaign_by_id(self, draft_campaign_id):
        self.uri_path = "/sb/drafts/campaigns/{}".format(draft_campaign_id)
        self.method = "delete"
        return self.execute()

    def submit_drafts_campaign(self, data):
        self.uri_path = "/sb/drafts/campaigns/submit"
        self.method = "post"
        self.data = data
        return self.execute()
