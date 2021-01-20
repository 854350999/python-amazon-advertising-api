

from ..adapi import Client


class NegProductTargets(Client):

    def create_neg_targets(self, params):
        self.uri_path = "/v2/sp/negativeTargets"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_neg_targets(self, params):
        self.uri_path = "/v2/sp/negativeTargets"
        self.method = "put"
        self.data = params
        return self.execute()

    def get_neg_targets(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeTargets"
        self.data = params
        return self.execute()

    def get_neg_targets_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeTargets/{}".format(target_id)
        return self.execute()

    def delete_neg_targets_by_id(self, target_id):
        self.uri_path = "/v2/sp/negativeTargets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

    def get_neg_targets_extended(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeTargets/extended"
        self.data = params
        return self.execute()

    def get_neg_targets_extended_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeTargets/extended/{}".format(target_id)
        return self.execute()
