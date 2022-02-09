

from ..client import Client


class Brands(Client):

    def get_brands(self, brand_type_filter):
        self.uri_path = "/brands"
        self.method = "get"
        self.params = {
            "brandTypeFilter": brand_type_filter
        }
        return self.execute()
