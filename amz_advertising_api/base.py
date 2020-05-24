import requests
from config import domain,region

class BaseApi(object):
    """
    基础类, 配置参数和调用方式
    """

    def __init__(self, access_token):

        self.access_token = access_token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.access_token)
        }
        self.api_domain = domain[region]
        self.method = 'get'
        self.data = None
        self.uri_path = ''

    def make_call(self):

        rq_url = self.api_domain + self.uri_path
        if self.method == 'delete':
            return requests.delete(rq_url, headers=self.headers).text
        return getattr(requests, self.method)(
            rq_url, self.data, headers=self.headers).json()

    def public_call(self, url):

        s = requests.Session()
        print(self.headers)
        self.headers.pop('Content-Type')
        self.headers['Accept-encoding'] = 'gzip'
        ret = s.get(url, headers=self.headers)
        print(ret.__dict__)
        return ret.content


class MainBaseApi(BaseApi):
    """
    除了 profiles 通用的
    """

    def __init__(self, profile_id, access_token):
        """
        都需要添加profile_id
        """
        self.profile_id = profile_id
        super(MainBaseApi, self).__init__(access_token)
        self.headers['Amazon-Advertising-API-Scope'] = self.profile_id