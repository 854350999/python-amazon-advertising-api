

from ..adapi import Client


class Media(Client):

    def create_media_upload(self, params):
        self.uri_path = "/media/upload"
        self.method = "post"
        self.data = params
        return self.execute()

    def update_media_upload(self, params):
        self.uri_path = "/media/complete"
        self.method = "put"
        self.data = params
        return self.execute()

    def get_media_describe(self, media_id):
        self.method = "get"
        self.uri_path = "/media/describe"
        self.headers["mediaId"] = media_id
        return self.execute()
