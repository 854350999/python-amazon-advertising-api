

from ..client import Client


class Snapshots(Client):

    def request_snapshots(self, record_type, params):
        self.uri_path = "/v2/sp/{}/snapshot".format(record_type)
        self.method = "post"
        self.data = params
        return self.execute()

    def get_snapshots_status(self, snapshot_id):
        self.method = "get"
        self.uri_path = "/v2/sp/snapshots/{}".format(snapshot_id)
        return self.execute()

