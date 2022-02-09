
from ..client import Client


class Snapshots(Client):

    def create_snapshot(self, record_type: str, state_filter=None):
        if state_filter is None:
            state_filter = {}
        self.uri_path = "/v2/hsa/{}/snapshot".format(record_type)
        self.method = "post"
        self.data = {
            "stateFilter": state_filter
        }
        return self.execute()

    def get_snapshots(self, snapshot_id: str):
        self.uri_path = "/v2/hsa/snapshots/{}".format(snapshot_id)
        self.method = "get"
        return self.execute()
