

from ..client import Client


class ProductTargeting(Client):

    def get_targets(self, next_token: str = None, max_results: int = 0, filters: list = None):
        self.uri_path = "/sb/targets/list"
        self.method = "post"

        self.data = {
            "nextToken": next_token,
            "maxResults": max_results,
            "filters": filters
        }
        return self.execute()

    def update_targets(self, data):
        self.uri_path = "/sb/targets"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_targets(self, data):
        self.uri_path = "/sb/targets"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_targets_by_id(self, target_id):
        self.uri_path = "/sb/targets/{}".format(target_id)
        self.method = "get"
        return self.execute()

    def delete_targets_by_id(self, target_id):
        self.uri_path = "/sb/targets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

