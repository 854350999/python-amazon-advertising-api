
from ..client import Client


class BidRecommendations(Client):

    def get_bid_by_ad_group_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}/bidRecommendations".format(ad_group_id)
        return self.execute()

    def get_bid_by_keyword_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/{}/bidRecommendations".format(keyword_id)
        return self.execute()

    def get_bid_by_keywords(self, data):
        self.uri_path = "/v2/sp/keywords/bidRecommendations"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_bid_by_targets(self, data):
        self.uri_path = "/v2/sp/targets/bidRecommendations"
        self.method = "post"
        self.data = data
        return self.execute()
