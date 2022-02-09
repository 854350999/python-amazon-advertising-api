

from ..client import Client


class SuggestProducts(Client):

    def get_suggest_products(self, params):
        self.method = "get"
        self.uri_path = "/sd/suggestedProducts"
        self.data = params
        return self.execute()

    def get_suggest_products_by_status(self, params):
        self.uri_path = "/sd/suggestedProducts/productReadinessStatus"
        self.method = "post"
        self.data = params
        return self.execute()


