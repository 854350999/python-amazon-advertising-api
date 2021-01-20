

from ..adapi import Client


class ProductAds(Client):

    def get_product_ads(self, params):
        self.method = "get"
        self.uri_path = "/sd/productAds"
        self.data = params
        return self.execute()

    def update_product_ads(self, params):
        self.uri_path = "/sd/productAds"
        self.method = "put"
        self.data = params
        return self.execute()

    def create_product_ads(self, params):
        self.uri_path = "/sd/productAds"
        self.method = "post"
        self.data = params
        return self.execute()

    def get_product_ads_by_id(self, ad_id):
        self.method = "get"
        self.uri_path = "/sd/productAds/{}".format(ad_id)
        return self.execute()

    def delete_product_ads_by_id(self, ad_id):
        self.uri_path = "/sd/productAds/{}".format(ad_id)
        self.method = "delete"
        return self.execute()

    def get_product_ads_extended(self, params):
        self.method = "get"
        self.uri_path = "/sd/productAds/extended"
        self.data = params
        return self.execute()

    def get_product_ads_extended_by_id(self, ad_id):
        self.method = "get"
        self.uri_path = "/sd/productAds/extended/{}".format(ad_id)
        return self.execute()


