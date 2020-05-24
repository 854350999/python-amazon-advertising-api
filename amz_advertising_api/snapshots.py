# coding:utf-8
"""
Snapshots 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class Snapshots(MainBaseApi):
    """
    按类型的广告报告
    """

    def get(self, snapshots_id):
        """
        根据report获取信息
        """
        self.uri_path = '/v2/sp/snapshots/{snapshotId}'.format(snapshotId=snapshots_id)
        self.data = None
        self.method = 'get'
        return self.make_call()

    def create(self, recordType, params):
        """
        report type
        oneof:campaigns, adGroups, keywords, negativeKeywords, campaignNegativeKeywords,or productAds
        {“campaignType”: “sponsoredProducts”,
         "stateFilter": "one of enabled, paused, archived. Default behavior is to include enabledand paused"
        }
        """
        self.uri_path = '/v2/sp/{recordType}/snapshot'.format(recordType=recordType)
        self.method = 'post'
        self.data = params
        return self.make_call()

    def download(self, loc_path):
        """
        下载
        """
        return self.public_call(loc_path)