# coding:utf-8
"""
Report 相关操作, 具体参数请参见 对应的json配置文件
"""

from base import MainBaseApi


class Report(MainBaseApi):
    def create_report(self, report_type, params):
        self.uri_path = '/v2/sp/{recordType}/report'.format(recordType=report_type)
        self.method = 'post'
        self.data = params
        return self.make_call()
    def download_report(self, report_id):
        self.uri_path = '/v2/reports/{reportId}/download'.format(reportId=report_id)
        self.method = 'get'
        return self.make_call()
    def create_asins_report(self, params):
        self.uri_path = '/v2/asins/report'
        self.method = 'post'
        self.data = params
        return self.make_call()
    def get_asins_report(self, report_id):
        self.uri_path = '/v2/reports/{reportId}'.format(reportId=report_id)
        self.method = 'get'
        return self.make_call()
    def download(self, loc_path):
        """
        下载
        """
        return self.public_call(loc_path)