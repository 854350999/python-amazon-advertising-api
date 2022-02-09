

from ..client import Client


class TargetingRecommendations(Client):

    def get_recommendations_targets(self, next_token: str = None, max_results: int = None, filters: list = None):
        self.uri_path = "/sb/recommendations/targets/product/list"
        self.method = "post"
        self.data = {
            "nextToken": next_token,
            "maxResults": max_results,
            "filters": filters
        }
        return self.execute()

    def get_recommendations_targets_category(self, asins):
        self.uri_path = "/sb/recommendations/targets/category"
        self.method = "post"
        self.data = {
            "asins": asins
        }
        return self.execute()

    def get_recommendations_targets_brand(self, category_id: int = None, keyword: str = None):
        self.uri_path = "/sb/recommendations/targets/brand"
        self.method = "post"
        self.data = {
            "categoryId": category_id,
            "keyword": keyword
        }
        return self.execute()

