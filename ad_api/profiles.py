from .client import ProClient


class Profiles(ProClient):

    def register(self, **params):
        self.uri_path = "/v2/profiles/register"
        self.data = params
        self.method = "put"
        return self.execute()

    def get_profiles(self):
        self.uri_path = "/v2/profiles"
        self.method = "get"
        return self.execute()
