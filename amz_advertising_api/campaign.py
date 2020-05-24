from base import MainBaseApi


class Campaigns(MainBaseApi):
    """
    campaigns  info
    """

    def create(self, params):
        """
        data = json.dumps([
            {
            "name": "Hello World Campaign",
            "state": "enabled",
            "startDate": "20290101",
            "campaignType": "sponsoredProducts",
            "targetingType": "auto",
            "dailyBudget": 1.00
        }
        ])
        """

        self.uri_path = '/v2/sp/campaigns'
        self.data = params
        self.method = 'post'
        return self.make_call()

    def get_campaign(self, campaign_id):

        self.uri_path = '/v2/sp/campaigns/{campaignId}'.format(
            campaignId=campaign_id)
        self.method = 'get'
        return self.make_call()

    def get_extended_campaign(self, campaign_id):

        self.uri_path = '/v2/sp/campaigns/extended/{campaignId}'.format(
            campaignId=campaign_id)
        self.method = 'get'
        return self.make_call()
    def put_campaign(self, params):
        self.uri_path = '/v2/sp/campaigns'
        self.method = 'post'
        self.data = params
        return self.make_call()

    def list(self, params=None):

        self.uri_path = '/v2/sp/campaigns'
        self.method = 'get'
        self.data = params
        return self.make_call()

    def list_extended(self, params=None):

        self.uri_path = '/v2/sp/campaigns/extended'
        self.method = 'get'
        self.data = params
        return self.make_call()