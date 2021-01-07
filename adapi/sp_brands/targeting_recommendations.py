

from ..adapi import Client


class TargetingRecommendations(Client):

    def get_recommendations_targets(self, params):
        self.uri_path = "/sb/recommendations/targets/product/list"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_recommendations_targets_category(self, params):
        self.uri_path = "/sb/recommendations/targets/category"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_recommendations_targets_brand(self, params):
        self.uri_path = "/sb/recommendations/targets/brand"
        self.method = "post"
        self.data = params
        return self.execute()

