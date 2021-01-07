

from ..adapi import Client


class NegTargeting(Client):

    def get_neg_targets(self, params):
        self.uri_path = "/sd/negativeTargets"
        self.data = params
        return self.execute()

    def update_neg_targets(self, params):
        self.uri_path = "/sd/negativeTargets"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_net_targets(self, params):
        self.uri_path = "/sd/negativeTargets"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_neg_targets_by_id(self, target_id):
        self.uri_path = "/sd/negativeTargets/{}".format(target_id)
        return self.execute()

    def delete_neg_targets_by_id(self, target_id):
        self.uri_path = "/sd/negativeTargets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

    def get_neg_targets_extended(self, params):
        self.uri_path = "/sd/negativeTargets/extended"
        self.data = params
        return self.execute()

    def get_neg_targets_extended_by_id(self, target_id):
        self.uri_path = "/sd/negativeTargets/extended/{}".format(target_id)
        return self.execute()


