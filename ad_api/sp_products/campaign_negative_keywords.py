from ..client import Client


class CampaignNegativeKeywords(Client):

    def get_campaign_negative_keywords(self, start_index: int = 0, count: int = 0, match_type_filter: str = None,
                                       keyword_text: str = None, campaign_id_filter: str = None,
                                       keyword_id_filter: str = None):
        self.uri_path = "/v2/sp/campaignNegativeKeywords"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "campaignIdFilter": campaign_id_filter,
            "keywordIdFilter": keyword_id_filter
        }
        return self.execute()

    def create_campaign_negative_keywords(self, data):
        self.uri_path = "/v2/sp/campaignNegativeKeywords"
        self.method = "post"
        self.data = data
        return self.execute()

    def update_campaign_negative_keywords(self, data):
        self.uri_path = "/v2/sp/campaignNegativeKeywords"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_campaign_negative_keywords_extend(self, start_index: int = 0, count: int = 0, match_type_filter: str = None,
                                              keyword_text: str = None, campaign_id_filter: str = None,
                                              keyword_id_filter: str = None):
        self.uri_path = "/v2/sp/campaignNegativeKeywords/extended"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "matchTypeFilter": match_type_filter,
            "keywordText": keyword_text,
            "campaignIdFilter": campaign_id_filter,
            "keywordIdFilter": keyword_id_filter
        }
        return self.execute()

    def get_campaign_negative_keywords_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/campaignNegativeKeywords/{}".format(keyword_id)
        self.method = "get"
        return self.execute()

    def delete_campaign_negative_keywords_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/campaignNegativeKeywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()

    def get_campaign_negative_keywords_extend_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/campaignNegativeKeywords/extended/{}".format(keyword_id)
        self.method = "get"
        return self.execute()
