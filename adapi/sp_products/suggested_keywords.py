

from ..adapi import Client


class SuggestKeywords(Client):

    def get_suggest_keywords_by_ad_group_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}/suggested/keywords".format(ad_group_id)
        return self.execute()

    def get_suggest_keywords_extended_by_ad_group_id(self, ad_group_id):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}//suggested/keywords/extended".format(ad_group_id)
        return self.execute()

    def get_suggest_keywords_by_asin(self, asin):
        self.method = "get"
        self.uri_path = "/v2/sp/asin/{}/suggested/keywords".format(asin)
        return self.execute()

    def get_suggest_keywords_by_asins(self, asins, max_num_suggestions=None):
        self.method = "get"
        self.uri_path = "/v2/sp/asin/suggested/keywords"
        self.data = {
            "asins": asins,
            "maxNumSuggestions": max_num_suggestions
        }
        return self.execute()



