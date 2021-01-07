

from ..adapi import Client


class Moderation(Client):

    def get_moderation_campaigns_by_id(self, campaign_id):
        self.uri_path = "/sb/moderation/campaigns/{}".format(campaign_id)
        return self.execute()

