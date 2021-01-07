

from ..adapi import Client


class Reports(Client):

    def request_report(self, record_type, params):
        self.uri_path = "/v2/hsa/{}/report".format(record_type)
        self.method = "post"
        self.data = params
        return self.execute()

    def get_report(self, report_id):
        self.uri_path = "/v2/reports/{}".format(report_id)
        return self.execute()

    def get_report_download_url(self, report_id):
        self.uri_path = "/v2/reports/{}/download"
        return self.execute()

