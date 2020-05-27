from base import BaseApi


class Profiles(BaseApi):
    """
    profiels info
    """
    def register(self, params):
        """注册个人资料"""

        self.uri_path = '/v2/profiles/register'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def get_profiles(self):
        """检索与授权令牌关联的所有配置文件"""

        self.uri_path = '/v2/profiles'
        self.method ='get'
        return self.make_call()
    def get_profiles_by_profileId(self):
        """检索由标识符指定的配置文件"""
        self.uri_path = '/v2/profiles/{profileId}'
        self.method = 'get'
        return self.make_call()
    def put_profiles(self, params):
        """更新一个或多个配置文件"""
        self.uri_path = '/v2/profiles/'
        self.method = 'put'
        self.data = params
        return self.make_call()