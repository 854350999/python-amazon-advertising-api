

from ..adapi import Client


class Keywords(Client):

    def get_keywords(self, params):
        self.method = "get"
        self.uri_path = "/sb/keywords"
        self.data = params
        return self.execute()

    def update_keywords(self, params):
        self.uri_path = "/sb/keywords"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_keywords(self, params):
        self.method = "post"
        self.uri_path = "/sb/keywords"
        self.data = params
        return self.execute()

    def get_keyword_by_id(self, keyword_id):
        self.method = "get"
        self.uri_path = "/sb/keywords/{}".format(keyword_id)
        return self.execute()

    def delete_keyword_by_id(self, keyword_id):
        self.method = "delete"
        self.uri_path = "/sb/keywords/{}".format(keyword_id)
        return self.execute()

