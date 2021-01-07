

from ..adapi import Client


class TargetingRecommendations(Client):

    def get_targets_recommendations(self, params):
        self.uri_path = "/sd/targets/recommendations"
        self.method = "post"
        self.data = params
        return self.execute()
