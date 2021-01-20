

from ..adapi import Client


class NegKeywords(Client):

    def get_neg_keywords_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeKeywords/{}".format(keyword_id)
        return self.execute()

    def delete_neg_keywords_by_id(self, keyword_id):
        self.uri_path = "/v2/sp/negativeKeywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()

    def get_neg_keywords_extended_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeKeywords/extended/{}".format(keyword_id)
        return self.execute()

    def get_neg_keywords_extended(self, params):
        self.uri_path = "/v2/sp/negativeKeywords/extended"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_neg_keywords(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/negativeKeywords"
        self.data = params
        return self.execute()

    def create_neg_keywords(self, params):
        self.uri_path = "/v2/sp/negativeKeywords"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_neg_keywords(self, params):
        self.uri_path = "/v2/sp/negativeKeywords"
        self.method = "put"
        self.data = params
        return self.execute()

