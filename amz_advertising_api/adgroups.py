from base import MainBaseApi
import json
class Adgroups(MainBaseApi):
    def get(self, adgroupId):
        """通过ID检索广告组"""
        self.uri_path = '/v2/sp/adGroups/{adGroupId}'.format(adGroupId=adgroupId)
        self.method = 'get'
        return self.make_call()
    def get_extended(self, adgroupId):
        """通过ID检索广告组以及其他属性"""
        self.uri_path = '/v2/sp/adGroups/extended/{adGroupId}'.format(adGroupId=adgroupId)
        self.method = 'post'
        return self.make_call()
    def create_adgroup(self, params):
        """制作一个或多个广告组
        data = json.dumps(
            [
                {
                    "name": "",
                    "campaginId": "",
                    "defaultBid": "",
                    "state": "",
                }
            ]
        )
        """
        self.uri_path = '/v2/sp/adGroups'
        self.method = 'post'
        self.data = params
        return self.make_call()
    def update_adgroup(self, params):
        """更新一个或多个广告组"""
        self.uri_path = '/v2/sp/adGroups'
        self.method = 'put'
        self.data = params
        return self.make_call()
    def delete_adgroup(self, adgroupId):
        """删除、存档一个广告组"""
        self.uri_path = '/v2/sp/adGroups/{adGroupId}'.format(adGroupId=adgroupId)
        self.method = 'delete'
        return self.make_call()
    def list(self, params):
        """根据指定条件返回广告组列表
        data = {startIndex={startIndex}
        &count={count}
        &campaignType={campaignType}
        &stateFilter={stateFilter}
        &campaignIdFilter={campaignIdFilter}
        &adGroupIdFilter={adGroupIdFilter}
        &name={name}}
        """
        self.uri_path = '/v2/sp/adGroups'
        self.data = params
        self.method = 'get'
        return self.make_call()
    def list_extended(self, params):
        """根据指定条件返回具有其他属性的广告组列表"""
        self.uri_path = '/v2/sp/adGroups/extended'
        self.method = 'get'
        self.data = params
        return self.make_call()