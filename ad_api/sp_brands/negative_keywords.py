
from ..client import Client


class NegativeKeywords(Client):

    def get_negative_keywords(self, start_index: int = 0, count: int = None, match_type_filter: str = None,
                              keyword_text: str = None, state_filter: str = None, campaign_id_filter: str = None,
                              ad_group_id_filter: str = None, keyword_id_filter: str = None, creative_type: str = None):
        self.uri_path = "/sb/negativeKeywords"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter
        }
        return self.execute()

    def update_negative_keywords(self, data):
        self.uri_path = "/sb/negativeKeywords"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_negative_keywords(self, data):
        self.uri_path = "/sb/negativeKeywords"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_negative_keywords_by_id(self, keyword_id):
        self.uri_path = "/sb/negativeKeywords/{}".format(keyword_id)
        self.method = "get"
        return self.execute()

    def delete_negative_keywords_by_id(self, keyword_id):
        self.uri_path = "/sb/negativeKeywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()
