
from ..client import Client


class Snapshots(Client):

    def create_snapshots(self, record_type, data):
        self.uri_path = "/sd/{}/snapshot".format(record_type)
        self.method = "post"
        self.data = data
        return self.execute()

    def get_snapshots(self, snapshot_id):
        self.uri_path = "/sd/snapshots/{}".format(snapshot_id)
        self.method = "get"
        return self.execute()

    def get_snapshots_download(self, snapshot_id):
        self.uri_path = "/sd/snapshots/{}/download".format(snapshot_id)
        self.method = "get"
        return self.execute()
