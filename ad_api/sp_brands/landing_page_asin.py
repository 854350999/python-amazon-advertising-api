

from ..client import Client


class LandingPageAsin(Client):

    def get_page_asin(self, page_url):
        self.method = "get"
        self.uri_path = "/pageAsins"
        self.headers["pageUrl"] = page_url
        return self.execute()

