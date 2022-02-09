
from ..client import Client


class NegativeProductTargeting(Client):

    def get_negative_targets(self, next_token: str = None, max_results: int = None, filters: list = None):
        self.uri_path = "/sb/negativeTargets/list"
        self.method = "post"
        self.data = {
            "nextToken": next_token,
            "maxResults": max_results,
            "filters": filters
        }
        return self.execute()

    def update_negative_targets(self, data):
        self.uri_path = "/sb/negativeTargets"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_negative_targets(self, data):
        self.uri_path = "/sb/negativeTargets"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_negative_targets_by_id(self, negative_target_id):
        self.uri_path = "/sb/negativeTargets/{}".format(negative_target_id)
        self.method = "get"
        return self.execute()

    def delete_negative_targets_by_id(self, negative_target_id):
        self.uri_path = "/sb/negativeTargets/{}".format(negative_target_id)
        self.method = "delete"
        return self.execute()

