

from ..client import Client


class KeywordRecommendations(Client):

    def get_keyword_recommendations(self, params):
        self.uri_path = "/sb/recommendations/keyword"
        self.data = params
        self.method = "post"
        return self.execute()


