

from ..adapi import Client


class CampNegKeywords(Client):

    def get_camp_neg_keywords_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/campaignNegativeKeywords/{}".format(keyword_id)
        return self.execute()

    def delete_camp_neg_keywords_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/campaignNegativeKeywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()

    def get_camp_neg_keywords_extended_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/campaignNegativeKeywords/extended/{}".format(keyword_id)
        return self.execute()

    def get_camp_neg_keywords_extended(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/campaignNegativeKeywords/extended"
        self.data = params
        return self.execute()

    def get_camp_neg_keywords(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/campaignNegativeKeywords"
        self.data = params
        return self.execute()

    def create_camp_neg_keywords(self, params):
        self.uri_path = "/v2/sp/campaignNegativeKeywords"
        self.data = params
        self.method = "post"
        return self.execute()

    def update_camp_neg_keywords(self, params):
        self.uri_path = "/v2/sp/campaignNegativeKeywords"
        self.data = params
        self.method = "put"
        return self.execute()
