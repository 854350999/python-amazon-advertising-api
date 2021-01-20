

from ..adapi import Client


class Stores(Client):

    def get_store_assets(self, params):
        self.method = "get"
        self.uri_path = "/stores/assets"
        self.data = params
        return self.execute()

    def create_store_assets(self, params):
        self.uri_path = "/store/assets"
        self.method = "post"
        self.data = params
        return self.execute()
