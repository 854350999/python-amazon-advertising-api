

from ..adapi import Client


class BidRecommendations(Client):

    def get_bid_recommendations(self, params):
        self.uri_path = "/sb/recommendations/bids"
        self.method = "post"
        self.data = params
        return self.execute()
