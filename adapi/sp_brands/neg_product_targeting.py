

from ..adapi import Client


class NegProductTargeting(Client):

    def get_neg_targets(self, params):
        self.uri_path = "/sb/negativeTargets/list"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_neg_targets(self, params):
        self.uri_path = "/sb/negativeTargets"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_neg_targets(self, params):
        self.uri_path = "/sb/negativeTargets"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_neg_targets_by_id(self, neg_target_id):
        self.method = "get"
        self.uri_path = "/sb/negativeTargets/{}".format(neg_target_id)
        return self.execute()

    def delete_neg_targets_by_id(self, neg_target_id):
        self.uri_path = "/sb/negativeTargets/{}".format(neg_target_id)
        self.method = "delete"
        return self.execute()

