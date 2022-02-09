

from ..client import Client


class Keywords(Client):

    def get_keywords(self, start_index: int = 0, count: int = None, match_type_filter: str = None,
                     keyword_text: str = None, state_filter: str = None, campaign_id_filter: str = None,
                     ad_group_id_filter: str = None, keyword_id_filter: str = None, creative_type: str = None,
                     locale: str = None):
        self.uri_path = "/sb/keywords"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "keywordIdFilter": keyword_id_filter,
            "creativeType": creative_type,
            "locale": locale
        }
        return self.execute()

    def update_keywords(self, data):
        self.uri_path = "/sb/keywords"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_keywords(self, data):
        self.uri_path = "/sb/keywords"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_keyword_by_id(self, keyword_id):
        self.uri_path = "/sb/keywords/{}".format(keyword_id)
        self.method = "get"
        return self.execute()

    def delete_keyword_by_id(self, keyword_id):
        self.uri_path = "/sb/keywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()

