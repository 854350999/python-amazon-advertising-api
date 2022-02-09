

from ..client import Client


class Media(Client):

    def create_media_upload(self, program_type: str = "SponsoredBrands", creative_type: str = "Video"):
        self.uri_path = "/media/upload"
        self.method = "post"
        self.data = {
            "programType": program_type,
            "creativeType": creative_type
        }
        return self.execute()

    def update_media_upload(self, upload_location: str, version: str = None):
        self.uri_path = "/media/complete"
        self.method = "put"
        self.data = {
            "uploadLocation": upload_location,
            "version": version
        }
        return self.execute()

    def get_media_describe(self, media_id):
        self.method = "get"
        self.uri_path = "/media/describe"
        self.headers["mediaId"] = media_id
        return self.execute()
