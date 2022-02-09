from ..client import Client


class NegativeKeywords(Client):

    def get_negative_keywords_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeKeywords/{}".format(keyword_id)
        return self.execute()

    def delete_negative_keywords_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/negativeKeywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()

    def get_negative_keywords_extended_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeKeywords/extended/{}".format(keyword_id)
        return self.execute()

    def get_negative_keywords_extended(self, start_index: int = 0, count: int = 0, match_type_filter: str = None,
                                       keyword_text: str = None, state_filter: str = None,
                                       campaign_id_filter: str = None,
                                       ad_group_id_filter: str = None, keyword_id_filter: str = None):
        self.uri_path = "/v2/sp/negativeKeywords/extended"
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
        }
        return self.execute()

    def get_negative_keywords(self, start_index: int = 0, count: int = 0, match_type_filter: str = None,
                              keyword_text: str = None, state_filter: str = None, campaign_id_filter: str = None,
                              ad_group_id_filter: str = None, keyword_id_filter: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeKeywords"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "keywordIdFilter": keyword_id_filter,
        }
        return self.execute()

    def create_negative_keywords(self, data):
        self.uri_path = "/v2/sp/negativeKeywords"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_negative_keywords(self, data):
        self.uri_path = "/v2/sp/negativeKeywords"
        self.method = "put"
        self.data = data
        return self.execute()
