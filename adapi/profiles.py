from adapi.adapi import ProClient


class Profiles(ProClient):

    def register(self, **params):
        self.uri_path = "/v2/profiles/register"
        self.data = params
        self.method = "put"
        return self.make_call()

    def get_profiles(self):
        self.uri_path = "/v2/profiles"
        self.method = "get"
        return self.make_call()

    
