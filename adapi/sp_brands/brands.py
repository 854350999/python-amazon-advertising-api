

from ..adapi import Client


class Brands(Client):

    def get_brands(self):
        self.method = "get"
        self.uri_path = "/brands"
        return self.execute()
