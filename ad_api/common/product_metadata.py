
from ..client import Client


class ProductMetadata(Client):

    def get_product_metadata(self, data):
        self.uri_path = "/product/metadata"
        self.method = "post"
        self.data = data
        return self.execute()
