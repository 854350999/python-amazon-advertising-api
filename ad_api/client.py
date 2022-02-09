import requests
from .conf import domain_dict
import json


class ProClient(object):
    def __init__(self, access_token, region, client_id):
        self.access_token = access_token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.access_token),
            "Amazon-Advertising-API-ClientId": client_id
        }
        self.domain = domain_dict[region]
        self.method = "get"
        self.data = None
        self.uri_path = None
        self.params = None

    def execute(self):
        url = self.domain + self.uri_path
        if self.method == "delete":
            response = requests.delete(url, headers=self.headers).text
            return response
        if self.data:
            self.data = json.dumps(self.data)
        response = requests.request(self.method, url, params=self.params, headers=self.headers, data=self.data)
        return response

    def execute_download(self, url):
        s = requests.Session()
        self.headers.pop("Content-Type")
        self.headers["Accept-encoding"] = "gzip"
        response = s.get(url, headers=self.headers)
        return response.__dict__


class Client(ProClient):
    def __init__(self, access_token, profile_id, region, client_id):
        self.profile_id = profile_id
        super(Client, self).__init__(access_token, region, client_id)
        self.headers["Amazon-Advertising-API-Scope"] = self.profile_id





