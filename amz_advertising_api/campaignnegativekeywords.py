

from base import MainBaseApi




class negativeKeywords(MainBaseApi):

    def get_negative_keywords_by_id(self, keyword_id):
        """按ID检索广告组级否定关键字"""

        self.uri_path = '/v2/sp/campaignNegativeKeywords/{keywordId}'.format(keywordId=keyword_id)
        self.method = 'get'
        return self.make_call()

    def get_negative_keywords_extended_by_id(self, keyword_id):
        """按ID检索广告组级否定关键字以及其他属性"""
        self.uri_path = '/v2/sp/campaignNegativeKeywords/{keywordId}'.format(keywordId=keyword_id)
        self.method = 'get'
        return self.make_call()

    def create_negative_keywords(self, params):
        """创建一个或多个否定广告组一级的关键字"""
        self.uri_path = '/v2/sp/campaignNegativeKeywords'
        self.method = 'post'
        self.data = params
        return self.make_call()

    def put_negative_keywords(self, params):
        """更新一个或多个否定广告组一级的关键字"""
        self.uri_path = '/v2/sp/campaignNegativeKeywords'
        self.method = 'put'
        self.data = params
        return self.make_call()

    def delete_negative_keywords_by_id(self, keyword_id):
        """存档单个否定广告组级关键字"""
        self.uri_path = '/v2/sp/campaignNegativeKeywords/{keywordId}'.format(keywordId=keyword_id)
        self.method = 'delete'
        return self.make_call()

    def list_negative_keywords(self, params):
        """根据指定条件返回否定广告组级关键字的列表"""
        self.uri_path = '/v2/sp/campaignNegativeKeywords'
        self.data = params
        self.method = 'get'
        return self.make_call()

    def list_negative_keywords_extended(self, params):
        """根据指定条件返回带有附加属性的广告组级否定关键字列表"""
        self.uri_path = '/v2/sp/campaignNegativeKeywords/extended'
        self.data = params
        self.method = 'get'