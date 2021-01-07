
from ..adapi import Client


class Reports(Client):

    def create_report(self, record_type, params):
        self.uri_path = "/v2/sp/{}/report".format(record_type)
        self.method = "post"
        self.data = params
        return self.execute()

    def get_report_status(self, report_id):
        self.uri_path = "/v2/reports/{}".format(report_id)
        return self.execute()

    def get_report_location(self, location_url):
        return self.execute_download(location_url)
