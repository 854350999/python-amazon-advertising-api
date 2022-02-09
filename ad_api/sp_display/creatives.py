from ..client import Client


class Creatives(Client):

    def get_creatives(self, start_index: int = 0, count: int = 100, ad_group_id_filter: str = None,
                      creative_id_filter: str = None):
        self.uri_path = "/sd/creatives"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter
        }
        return self.execute()

    def update_creatives(self, data):
        self.uri_path = "/sd/creatives"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_creatives(self, data):
        self.uri_path = "/sd/creatives"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_creative_preview(self, data):
        self.uri_path = "/sd/creatives/preview"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_creative_moderation(self, language: str = "en-US", start_index: int = 0, count: int = 100,
                                ad_group_id_filter: str = None, creative_id_filter: str = None):
        self.uri_path = "/sd/moderation/creatives"
        self.method = "get"
        self.params = {
            "language": language,
            "startIndex": start_index,
            "count": count,
            "adGroupIdFilter": ad_group_id_filter,
            "creativeIdFilter": creative_id_filter
        }
        return self.execute()
