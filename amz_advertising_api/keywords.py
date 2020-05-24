
from base import MainBaseApi




class Keywords(MainBaseApi):
    """
    Adgroups  info
    """

    def create(self, params):
        """
        pass
        """

        self.uri_path = '/v2/sp/keywords'
        self.data = params
        self.method = 'post'
        return self.make_call()

    def get(self, keyword_id):

        self.uri_path = '/v2/sp/keywords/{keywordId}'.format(
            keywordId=keyword_id)
        self.method = 'get'
        return self.make_call()

    def get_extended(self, keyword_id):

        self.uri_path = '/v2/sp/keywords/extended/{keywordId}'.format(
            keywordId=keyword_id)
        self.method = 'get'
        return self.make_call()

    def put(self, params):
        """
        更新信息
        """
        self.uri_path = '/v2/sp/keywords'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def delete(self, keyword_id):
        """
        删除group
        """
        self.uri_path = '/v2/sp/keywords/{keywordId}'.format(
            keywordId=keyword_id)
        self.method = 'delete'
        return self.make_call()

    def list(self, **params):
        """
        列出 adgroups
        """

        self.uri_path = '/v2/sp/keywords'
        self.data = params
        self.method = 'get'
        return self.make_call()

    def list_extended(self, params):
        """
        详细信息
        """
        self.uri_path = '/v2/sp/keywords'
        self.data = params
        self.method = 'get'
        return self.make_call()