from ..client import Client


class Ads(Client):

    def delete_ads(self, data):
        self.method = "post"
        self.uri_path = "/sb/v4/ads/delete"
        self.data = data
        return self.execute()

    def update_ads(self, data):
        self.method = "put"
        self.uri_path = "/sb/v4/ads"
        self.data = data
        return self.execute()

    def create_product_collection_ads(self, data):
        self.method = "post"
        self.uri_path = "/sb/v4/ads/productCollection"
        self.data = data
        return self.execute()

    def get_ads_list(self, data):
        self.method = "post"
        self.uri_path = "/sb/v4/ads/list"
        self.data = data
        return self.execute()

    def create_video_ads(self, data):
        self.method = "post"
        self.uri_path = "/sb/v4/ads/video"
        self.data = data
        return self.execute()

    def create_brand_video_ads(self, data):
        self.method = "post"
        self.uri_path = "/sb/v4/ads/brandVideo"
        self.data = data
        return self.execute()

    def create_store_spotlight_ads(self, data):
        self.method = "post"
        self.uri_path = "/sb/v4/ads/storeSpotlight"
        self.data = data
        return self.execute()
