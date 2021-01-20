

from ..adapi import Client


class Targeting(Client):

    def get_targets(self, params):
        self.method = "get"
        self.uri_path = "/sd/targets"
        self.data = params
        return self.execute()

    def update_targets(self, params):
        self.uri_path = "/sd/targets"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_targets(self, params):
        self.uri_path = "/sd/targets"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_targets_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/sd/targets/{}".format(target_id)
        return self.execute()

    def delete_targets_by_id(self, target_id):
        self.uri_path = "/sd/targets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

    def get_targets_extended(self, params):
        self.method = "get"
        self.uri_path = "/sd/targets/extended"
        self.data = params
        return self.execute()

    def get_targets_extended_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/sd/targets/extended/{}".format(target_id)
        return self.execute()


