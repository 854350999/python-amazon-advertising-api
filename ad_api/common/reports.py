
from ..client import Client


class Reports(Client):

    def request_sb_report(self, record_type, report_date, metrics, segment=None, creative_type=None):
        self.uri_path = "/v2/hsa/{}/report".format(record_type)
        self.method = "post"
        self.data = {
            "segment": segment,
            "reportDate": report_date,
            "metrics": metrics,
            "creativeType": creative_type
        }
        return self.execute()

    def request_sd_report(self, record_type, report_date, metrics, tactic):
        self.uri_path = "/sd/{}/report".format(record_type)
        self.method = "post"
        self.data = {
            "reportDate": report_date,
            "tactic": tactic,
            "metrics": metrics
        }
        return self.execute()

    def request_sp_report(self, record_type, report_date, metrics, state_filter=None, campaign_type=None, segment=None):
        self.uri_path = "/v2/sp/{}/report".format(record_type)
        self.method = "post"
        self.data = {
            "stateFilter": state_filter,
            "campaignType": campaign_type,
            "segment": segment,
            "reportDate": report_date,
            "metrics": metrics
        }
        return self.execute()

    def get_report(self, report_id):
        self.uri_path = "/v2/reports/{}".format(report_id)
        self.method = "get"
        return self.execute()

    def get_report_download_url(self, location):
        self.method = "get"
        return self.execute_download(location)

    def get_report_download(self, report_id):
        self.uri_path = "/v2/reports/{}/download".format(report_id)
        self.method = "get"
        self.headers.pop("Content-Type")
        self.headers["Accept-encoding"] = "gzip"
        return self.execute()
