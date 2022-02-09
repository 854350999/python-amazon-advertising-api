

from ..client import Client


class Stores(Client):

    def get_store_assets(self, brand_entity_id: str = None, media_type: str = None):
        self.method = "get"
        self.uri_path = "/stores/assets"
        self.params = {
            "brandEntityId": brand_entity_id,
            "mediaType": media_type
        }
        return self.execute()

    def create_store_assets(self, content_disposition: str, content_type: str, data=None):
        self.uri_path = "/store/assets"
        self.headers["Content-Type"] = content_type
        self.headers["Content-Disposition"] = content_disposition
        self.method = "post"
        self.data = data
        return self.execute()
