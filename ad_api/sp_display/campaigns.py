from ..client import Client


class Campaigns(Client):

    def get_campaigns(self, start_index: int = 0, count: int = None, state_filter: str = "enabled, paused, archived",
                      name: str = None, campaign_id_filter: str = None, portfolio_id_filter: str = None):
        self.uri_path = "/sd/campaigns"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "campaignIdFilter": campaign_id_filter,
            "portfolioIdFilter": portfolio_id_filter
        }
        return self.execute()

    def update_campaigns(self, data):
        self.uri_path = "/sd/campaigns"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_campaigns(self, data):
        self.uri_path = "/sd/campaigns"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_campaign_by_id(self, campaign_id):
        self.uri_path = "/sd/campaigns/{}".format(campaign_id)
        self.method = "get"
        return self.execute()

    def delete_campaign_by_id(self, campaign_id):
        self.uri_path = "/sd/campaigns/{}".format(campaign_id)
        self.method = "delete"
        return self.execute()

    def get_campaigns_extended(self, start_index: int = 0, count: int = None,
                               state_filter: str = "enabled, paused, archived",
                               name: str = None, campaign_id_filter: str = None, portfolio_id_filter: str = None):
        self.uri_path = "/sd/campaigns/extended"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "name": name,
            "campaignIdFilter": campaign_id_filter,
            "portfolioIdFilter": portfolio_id_filter
        }
        return self.execute()

    def get_campaigns_extended_by_id(self, campaign_id):
        self.uri_path = "/sd/campaigns/extended/{}".format(campaign_id)
        self.method = "get"
        return self.execute()
