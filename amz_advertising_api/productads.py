from base import MainBaseApi


class ProductAads(MainBaseApi):
    """
    ProductAads  info
    """

    def create(self, params):
        """
        # data = json.dumps([{
        "name": "The name of the ad group",
        "campaignId": 164121332960233,
        "defaultBid": 0.5,
        "state": "enabled"
        }
        ])
        """

        self.uri_path = '/v2/sp/productAds'
        self.data = params
        self.method = 'post'
        return self.make_call()

    def get(self, ad_id):

        self.uri_path = '/v2/sp/productAds/{adId}'.format(
            adId=ad_id)
        self.method = 'get'
        return self.make_call()

    def put(self, params):
        """
        更新信息
        """
        self.uri_path = '/v2/sp/productAds'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def delete(self, ad_id):
        """
        删除group
        """
        self.uri_path = '/v2/sp/productAds/{adId}'.format(
            adId=ad_id)
        self.method = 'delete'
        return self.make_call()

    def list(self, **params):
        """
        列出 adgroups
        """

        self.uri_path = '/v2/sp/productAds'
        self.data = params
        self.method = 'get'
        return self.make_call()

    def list_extended(self, params):
        """
        详细信息
        """
        self.uri_path = '/v2/sp/productAds/extended'
        self.data = params
        self.method = 'get'
        return self.make_call()