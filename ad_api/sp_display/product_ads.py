from ..client import Client


class ProductAds(Client):

    def get_product_ads(self, start_index: int = 0, count: int = None, state_filter: str = "enabled, paused, archived",
                        ad_id_filter: str = None, ad_group_id_filter: str = None, campaign_id_filter: str = None):
        self.uri_path = "/sd/productAds"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adIdFilter": ad_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter
        }
        return self.execute()

    def update_product_ads(self, data):
        self.uri_path = "/sd/productAds"
        self.method = "put"
        self.data = data
        return self.execute()

    def create_product_ads(self, data):
        self.uri_path = "/sd/productAds"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_product_ads_by_id(self, ad_id):
        self.uri_path = "/sd/productAds/{}".format(ad_id)
        self.method = "get"
        return self.execute()

    def delete_product_ads_by_id(self, ad_id):
        self.uri_path = "/sd/productAds/{}".format(ad_id)
        self.method = "delete"
        return self.execute()

    def get_product_ads_extended(self, start_index: int = 0, count: int = None,
                                 state_filter: str = "enabled, paused, archived",
                                 ad_id_filter: str = None, ad_group_id_filter: str = None,
                                 campaign_id_filter: str = None):
        self.uri_path = "/sd/productAds/extended"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count,
            "stateFilter": state_filter,
            "adIdFilter": ad_id_filter,
            "adGroupIdFilter": ad_group_id_filter,
            "campaignIdFilter": campaign_id_filter
        }
        return self.execute()

    def get_product_ads_extended_by_id(self, ad_id):
        self.uri_path = "/sd/productAds/extended/{}".format(ad_id)
        self.method = "get"
        return self.execute()
