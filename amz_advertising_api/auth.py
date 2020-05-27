import requests
from config import client_id,client_secret,refresh_token,region,host_url_list,redirect_uri,token_url_list


class BaseAuth:
    scope = 'cpc_advertising:campaign_management'
    response_type = 'code'
    host = host_url_list[region]
    token_url = token_url_list[region]
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    def get_grant_url(self):
        """获取授权网址"""
        return '{host_grant}?client_id={client_id}&scope={scope}&response_type={response_type}&redirect_uri={redirect_uri}'.format(
            host_grant=self.host,
            client_id=client_id,
            scope=self.scope,
            response_type=self.response_type,
            redirect_uri=redirect_uri)
    def get_refresh_token(self, code):
        """根据获得的code获取refresh_token"""
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret
        }
        res = requests.post(self.token_url, data, headers=self.headers)
        info = res.json()
        print(info)
        access_token, refresh_token = info['access_token'], info['refresh_token']
        return access_token, refresh_token
    def get_new_access_token(self, refresh_token):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret
        }
        res = requests.post(self.token_url, data, headers=self.headers)
        info = res.json()
        access_token = info['access_token']
        return access_token

