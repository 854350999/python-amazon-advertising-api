

from ..client import Client


class TargetingRecommendations(Client):

    def get_targets_recommendations(self, tactic: str, products: list, type_filter: list):
        self.uri_path = "/sd/targets/recommendations"
        self.method = "post"
        self.data = {
            "tactic": tactic,
            "products": products,
            "typeFilter": type_filter
        }
        return self.execute()
