# coding:utf-8
"""
Report 相关操作, 具体参数请参见 对应的json配置文件
"""

from base import MainBaseApi


class Report(MainBaseApi):
    def create_report(self, report_type, params):
        '''按照报告类型创建报告'''
        self.uri_path = '/v2/sp/{recordType}/report'.format(recordType=report_type)
        self.method = 'post'
        self.data = params
        return self.make_call()
    def download_report(self, report_id):
        """根据报告id请求获取json报告的地址"""
        self.uri_path = '/v2/reports/{reportId}'.format(reportId=report_id)
        self.method = 'get'
        return self.make_call()
    def create_asins_report(self, params):
        """请求为具有要报告的性能数据的asins创建一个性能报告"""
        self.uri_path = '/v2/asins/report'
        self.method = 'post'
        self.data = params
        return self.make_call()
    def get_asins_report(self, report_id):
        """通过指定来检索先前请求的asins效果报告的状态，元数据和位置"""
        self.uri_path = '/v2/reports/{reportId}'.format(reportId=report_id)
        self.method = 'get'
        return self.make_call()
    def download(self, loc_path):
        """获取下载json报告的地址"""
        return self.public_call(loc_path)