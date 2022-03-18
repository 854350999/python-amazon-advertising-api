
from ..client import Client


class BidRecommendations(Client):

    def get_bid_recommendations(self, data):
        self.uri_path = "/sd/targets/bid/recommendations"
        self.method = "post"
        self.data = data
        self.headers.update(
            {"Content-Type": "application/vnd.sdtargetingrecommendations.v3.2+json"}
        )
        return self.execute()
