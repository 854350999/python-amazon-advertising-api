

from ..client import Client


class Campaigns(Client):

    def create_campaigns(self, data):
        self.uri_path = "/sb/campaigns"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_campaigns(self, data):
        self.uri_path = "/sb/campaigns"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_campaigns(self, start_index: int = 0, count: int = None, state_filter: str = None,
                      name: str = None, portfolio_id_filter: str = None, campaign_id_filter: str = None,
                      ad_format_filter: str = None, creative_type: str = None):
        self.uri_path = "/sb/campaigns"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "portfolioIdFilter": portfolio_id_filter,
            "campaignIdFilter": campaign_id_filter,
            "adFormatFilter": ad_format_filter,
            "creativeType": creative_type
        }
        return self.execute()

    def get_campaigns_by_id(self, campaign_id):
        self.uri_path = "/sb/campaigns/{}".format(campaign_id)
        self.method = "get"
        return self.execute()

    def delete_campaigns_by_id(self, campaign_id):
        self.uri_path = "/sb/campaigns/{}".format(campaign_id)
        self.method = "delete"
        return self.execute()

