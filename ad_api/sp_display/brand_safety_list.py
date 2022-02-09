
from ..client import Client


class BrandSafetyList(Client):

    def get_brand_safety_deny(self, start_index: int = 0, count: int = 1000):
        self.uri_path = "/sd/brandSafety/deny"
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count
        }
        return self.execute()

    def create_brand_safety_deny(self, data):
        self.uri_path = "/sd/brandSafety/deny"
        self.method = "post"
        self.data = data
        return self.execute()

    def delete_brand_safety_deny(self):
        self.uri_path = "/sd/brandSafety/deny"
        self.method = "delete"
        return self.execute()

    def get_brand_safety_results_by_id(self, request_id: str, start_index: int = 0, count: int = 1000):
        self.uri_path = "/sd/brandSafety/{}/results".format(request_id)
        self.method = "get"
        self.params = {
            "startIndex": start_index,
            "count": count
        }
        return self.execute()

    def get_brand_safety_status_by_id(self, request_id):
        self.uri_path = "/sd/brandSafety/{}/status".format(request_id)
        self.method = "get"
        return self.execute()

    def get_brand_safety_statuses(self):
        self.uri_path = "/sd/brandSafety/status"
        self.method = "get"
        return self.execute()

