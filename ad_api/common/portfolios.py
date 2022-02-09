
from ..client import Client


class Portfolios(Client):

    def get_portfolios(self):
        self.uri_path = "/v2/portfolios"
        self.method = "get"
        return self.execute()
