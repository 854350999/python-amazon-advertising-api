

from base import MainBaseApi


class suggested(MainBaseApi):
    def get_adgroup_suggest_by_id(self):
        """请求指定广告组的建议关键字"""
        self.uri_path = '/v2/sp/adGroups/{adGroupId}/suggested/keywords'
        self.method = 'get'
        return self.make_call()

    def get_adgroup_suggest_extended_by_id(self):
        """提供广告组的建议关键字。返回带有每个建议关键字的其他字段：，和（广告的）campaignIdadGroupIdstate"""
        self.uri_path = '/v2/sp/adGroups/{adGroupId}/suggested/keywords/extended'
        self.method = 'get'
        return self.make_call()
    
    def getAsinSuggestedKeywords(self, asin_value):
        """	提供指定ASIN的建议关键字"""
        self.uri_path = '/v2/sp/asins/{asinValue}/suggested/keywords'.format(asinValue=asin_value)
        self.method = 'get'
        return self.make_call()

    def bulkGetAsinSuggestedKeywords(self, params):
        """为指定的ASIN列表提供建议的关键字"""

        """
        :param params: {'asins':asin_list, 'maxNumSuggestions': 最大返回数量}
        :return:
        """

        self.uri_path = '/v2/sp/asins/suggested/keywords'
        self.method = 'post'
        self.data = params
        return self.make_call()