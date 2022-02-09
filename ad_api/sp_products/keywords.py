from ..client import Client


class Keywords(Client):

    def get_keywords_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/{}".format(keyword_id)
        return self.execute()

    def delete_keywords_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/keywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()

    def get_keywords_extended(self, start_index: int = 0, count: int = None, match_type_filter: str = None,
                              keyword_text: str = None, state_filter: str = None, campaign_id_filter: str = None,
                              ad_group_id_filter: str = None, keyword_id_filter: str = None, locale: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/extended"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "keywordIdFilter": keyword_id_filter,
            "locale": locale
        }
        return self.execute()

    def get_keywords_extended_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords/extended/{}".format(keyword_id)
        return self.execute()

    def get_keywords(self, start_index: int = 0, count: int = None, match_type_filter: str = None,
                     keyword_text: str = None, state_filter: str = None, campaign_id_filter: str = None,
                     ad_group_id_filter: str = None, keyword_id_filter: str = None, locale: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/keywords"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "stateFilter": state_filter,
            "campaignIdFilter": campaign_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "keywordIdFilter": keyword_id_filter,
            "locale": locale
        }
        return self.execute()

    def create_keywords(self, data):
        self.uri_path = "/v2/sp/keywords"
        self.data = data
        self.method = "post"
        return self.execute()

    def update_keywords(self, data):
        self.uri_path = "/v2/sp/keywords"
        self.data = data
        self.method = "put"
        return self.execute()
