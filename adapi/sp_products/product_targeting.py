

from ..adapi import Client


class ProductTargeting(Client):

    def create_targets(self, params):
        self.uri_path = "/v2/sp/targets"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_targets(self, params):
        self.uri_path = "/v2/sp/targets"
        self.method = "put"
        self.data = params
        return self.execute()

    def get_targets(self, params):
        self.uri_path = "/v2/sp/targets"
        self.method = "get"
        self.data = params
        return self.execute()

    def get_target_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/v2/sp/targets/{}".format(target_id)
        return self.execute()

    def delete_target_by_id(self, target_id):
        self.uri_path = "/v2/sp/targets/{}".format(target_id)
        self.method = "delete"
        return self.execute()

    def get_targets_extended(self, params):
        self.uri_path = "/v2/sp/targets/extended"
        self.method = "get"
        self.data = params
        return self.execute()

    def get_targets_extended_by_id(self, target_id):
        self.method = "get"
        self.uri_path = "/v2/sp/targets/extended/{}".format(target_id)
        return self.execute()

    def get_product_recommendations_targets(self, params):
        self.uri_path = "/v2/sp/targets/productRecommendations"
        self.data = params
        self.method = "post"
        return self.execute()

    def get_list_categories_targets(self, asins):
        self.method = "get"
        self.uri_path = "/v2/sp/targets/categories"
        self.data = {
            "asins": asins
        }
        return self.execute()

    def get_categories_refinements_targets(self, category_id):
        self.method = "get"
        self.uri_path = "/v2/sp/targets/categories/refinements"
        self.data = {
            "categoryId": category_id
        }
        return self.execute()

    def get_brands_targets(self, params):
        self.method = "get"
        self.uri_path = "/v2/sp/targets/brands"
        self.data = params
        return self.execute()

