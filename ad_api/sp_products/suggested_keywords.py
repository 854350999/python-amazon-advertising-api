

from ..client import Client


class SuggestedKeywords(Client):

    def get_suggested_keywords_by_ad_group_id(self, ad_group_id, max_num_suggestions: int = 100,
                                              ad_state_filter: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}/suggested/keywords".format(ad_group_id)
        self.params = {
            "maxNumSuggestions": max_num_suggestions,
            "adStateFilter": ad_state_filter
        }
        return self.execute()

    def get_suggested_keywords_extended_by_ad_group_id(self, ad_group_id, max_num_suggestions: int = 100,
                                                       suggest_bids: str = "no", ad_state_filter: str = None):
        self.method = "get"
        self.uri_path = "/v2/sp/adGroups/{}/suggested/keywords/extended".format(ad_group_id)
        self.params = {
            "maxNumSuggestions": max_num_suggestions,
            "suggestBids": suggest_bids,
            "adStateFilter": ad_state_filter
        }
        return self.execute()

    def get_suggest_keywords_by_asin(self, asin, max_num_suggestions: int = 100):
        self.method = "get"
        self.uri_path = "/v2/sp/asins/{}/suggested/keywords".format(asin)
        self.params = {
            "maxNumSuggestions": max_num_suggestions
        }
        return self.execute()

    def get_suggest_keywords_by_asins(self, asins: list = None, max_num_suggestions: int = 100):
        self.method = "post"
        self.uri_path = "/v2/sp/asins/suggested/keywords"
        self.data = {
            "asins": asins,
            "maxNumSuggestions": max_num_suggestions
        }
        return self.execute()



