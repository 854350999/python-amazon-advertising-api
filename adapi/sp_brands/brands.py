

from ..adapi import Client


class Brands(Client):

    def get_brands(self):
        self.uri_path = "/brands"
        return self.execute()
