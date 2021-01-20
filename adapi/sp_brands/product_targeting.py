

from ..adapi import Client


class ProductTargeting(Client):

    def get_targets_list(self, params):
        self.uri_path = "/sb/targets/list"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_targets(self, params):
        self.uri_path = "/sb/targets"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_targets(self, params):
        self.uri_path = "/sb/targets"
        self.data = params
        self.method = "post"
        return self.execute()

    def get_targets_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/sb/targets/{}".format(target_id)
        return self.execute()

    def delete_targets_by_id(self, target_id):
        self.uri_path = "/sb/targets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

