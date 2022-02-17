from ..client import Client


class BidRecommendations(Client):

    def get_bid_recommendations(self, data):
        """
        Get a list of bid recommendation objects for a specified list of keywords or products.
        :param data: A list of keywords or targeting expressions for which to generate bid recommendations.
        Note that if a value is specified for the campaignId field, the past performance data for the
        campaign may be use to create bid recommendations.
        ExampleValue: {
        "campaignId": 0,
        "targets": [
        [
        {
        "type": "asinCategorySameAs",
        "value": "string"
        }
        ]
        ],
        "keywords": [
        {
        "matchType": "broad",
        "keywordText": "string"
        }
        ],
        "adFormat": "productCollection"
        }
        :return:
        """
        self.uri_path = "/sb/recommendations/bids"
        self.method = "post"
        self.data = data
        return self.execute()
