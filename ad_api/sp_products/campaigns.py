from ..client import Client


class Campaigns(Client):

    def create_campaigns(self, data):
        self.uri_path = "/v2/sp/campaigns"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_campaigns(self, data):
        self.uri_path = "/v2/sp/campaigns"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_campaigns(self, start_index: int = 0, count: int = None, state_filter: str = None,
                      name: str = None, portfolio_id_filter: str = None, campaign_id_filter: str = None):
        queries = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "portfolioIdFilter": portfolio_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        self.params = queries
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns"
        return self.execute()

    def get_campaign_by_id(self, campaign_id):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns/{}".format(campaign_id)
        return self.execute()

    def delete_campaign_by_id(self, campaign_id):
        self.uri_path = "/v2/sp/campaigns/{}".format(campaign_id)
        self.method = "delete"
        return self.execute()

    def get_campaign_extended(self, start_index: int = 0, count: int = None, state_filter: str = None,
                              name: str = None, portfolio_id_filter: str = None, campaign_id_filter: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns/extended"
        queries = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "portfolioIdFilter": portfolio_id_filter,
            "campaignIdFilter": campaign_id_filter,
        }
        self.params = queries
        return self.execute()

    def get_campaign_extended_by_id(self, campaign_id):
        self.method = "get"
        self.uri_path = "/v2/sp/campaigns/{}".format(campaign_id)
        return self.execute()
