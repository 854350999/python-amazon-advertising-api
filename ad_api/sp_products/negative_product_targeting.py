from ..client import Client


class NegativeProductTargeting(Client):

    def create_negative_targets(self, data):
        self.uri_path = "/v2/sp/negativeTargets"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_negative_targets(self, data):
        self.uri_path = "/v2/sp/negativeTargets"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_negative_targets(self, start_index: int = 0, count: int = None, state_filter: str = None,
                             campaign_id_filter: str = None, ad_group_id_filter: str = None,
                             target_id_filter: str = None):
        self.uri_path = "/v2/sp/negativeTargets"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "targetIdFilter": target_id_filter
        }
        self.method = "get"
        return self.execute()

    def get_negative_targets_by_id(self, target_id):
        self.uri_path = "/v2/sp/negativeTargets/{}".format(target_id)
        self.method = "get"
        return self.execute()

    def delete_negative_targets_by_id(self, target_id):
        self.uri_path = "/v2/sp/negativeTargets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

    def get_negative_targets_extended(self, start_index: int = 0, count: int = None, state_filter: str = None,
                                      campaign_id_filter: str = None, ad_group_id_filter: str = None,
                                      target_id_filter: str = None):
        self.uri_path = "/v2/sp/negativeTargets/extended"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "targetIdFilter": target_id_filter
        }
        return self.execute()

    def get_negative_targets_extended_by_id(self, target_id):
        self.uri_path = "/v2/sp/negativeTargets/extended/{}".format(target_id)
        self.method = "get"
        return self.execute()
