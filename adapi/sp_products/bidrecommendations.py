
from ..adapi import Client


class BidRecommendations(Client):

    def get_bid_by_ad_group_id(self, ad_group_id):
        self.uri_path = "/v2/sp/adGroups/{}/bidRecommendations".format(ad_group_id)
        return self.execute()

    def get_bid_by_keyword_id(self, keyword_id):
        self.uri_path = "/v2/sp/keywords/{}/bidRecommendations".format(keyword_id)
        return self.execute()

    def get_bid_by_keywords(self, params):
        self.uri_path = "/v2/sp/keywords/bidRecommendations"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_bid_by_targets(self, params):
        self.uri_path = "/v2/sp/targets/bidRecommendations"
        self.method = "post"
        self.data = params
        return self.execute()
