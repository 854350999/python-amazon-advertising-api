

from ..adapi import Client


class Reports(Client):

    def request_report(self, record_type, params):
        self.uri_path = "/sd/{}/report".format(record_type)
        self.data = params
        self.method = "post"
        return self.execute()

    def get_report_status(self, report_id):
        self.uri_path = "/v2/reports/{}".format(report_id)
        return self.execute()

    def get_report_location(self, report_id):
        self.uri_path = "/v2/reports/{}/download".format(report_id)
        return self.execute()
