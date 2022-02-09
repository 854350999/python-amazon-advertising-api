from ..client import Client


class Targeting(Client):

    def get_targets(self, start_index: int = 0, count: int = None, state_filter: str = "enabled, paused, archived",
                    ad_group_id_filter: str = None, campaign_id_filter: str = None):
        self.uri_path = "/sd/targets"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter
        }
        return self.execute()

    def update_targets(self, data):
        self.uri_path = "/sd/targets"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_targets(self, data):
        self.uri_path = "/sd/targets"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_targets_by_id(self, target_id):
        self.uri_path = "/sd/targets/{}".format(target_id)
        self.method = "get"
        return self.execute()

    def delete_targets_by_id(self, target_id):
        self.uri_path = "/sd/targets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

    def get_targets_extended(self, start_index: int = 0, count: int = None,
                             state_filter: str = "enabled, paused, archived",
                             ad_group_id_filter: str = None, campaign_id_filter: str = None):
        self.uri_path = "/sd/targets/extended"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter
        }
        return self.execute()

    def get_targets_extended_by_id(self, target_id):
        self.uri_path = "/sd/targets/extended/{}".format(target_id)
        self.method = "get"
        return self.execute()
