

from ..adapi import Client


class LandingPageAsin(Client):

    def get_page_asin(self, page_url):
        self.uri_path = "/pageAsins"
        self.headers["pageUrl"] = page_url
        return self.execute()

