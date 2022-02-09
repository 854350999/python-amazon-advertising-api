

from ..client import Client


class BidRecommendations(Client):

    def get_bid_recommendations(self, data):
        self.uri_path = "/sb/recommendations/bids"
        self.method = "post"
        self.data = data
        return self.execute()
