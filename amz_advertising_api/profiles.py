from base import BaseApi


class Profiles(BaseApi):
    """
    profiels info
    """
    def register(self,**params):

        self.uri_path = '/v2/profiles/register'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def get_profiles(self):

        self.uri_path = '/v2/profiles'
        self.method ='get'
        return self.make_call()
    def get_profiles_by_profileId(self):
        self.uri_path = '/v2/profiles/{profileId}'
        self.method = 'get'
        return self.make_call()
    def put_profiles(self, params):
        self.uri_path = '/v2/profiles/'
        self.method = 'put'
        self.data = params
        return self.make_call()