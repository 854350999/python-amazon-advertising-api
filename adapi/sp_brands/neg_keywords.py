

from ..adapi import Client


class NegKeywords(Client):

    def get_neg_keywords(self, params):
        self.uri_path = "/sb/negativeKeywords"
        self.data = params
        return self.execute()

    def update_neg_keywords(self, params):
        self.uri_path = "/sb/negativeKeywords"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_neg_keywords(self, params):
        self.uri_path = "/sb/negativeKeywords"
        self.data = params
        self.method = "post"
        return self.execute()

    def get_neg_keywords_by_id(self, keyword_id):
        self.uri_path = "/sb/negativeKeywords/{}".format(keyword_id)
        return self.execute()

    def delete_neg_keywords_by_id(self, keyword_id):
        self.uri_path = "/sb/negativeKeywords/{}".format(keyword_id)
        self.method = "delete"
        return self.execute()
