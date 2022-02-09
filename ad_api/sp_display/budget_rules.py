
from ..client import Client


class BudgetRules(Client):

    def get_budget_rules_history_by_campaign_id(self, campaign_id, page_size: int, start_date: str, end_date: str,
                                          next_token: str = None):
        self.uri_path = "/sd/campaigns/{}/budgetRules/budgetHistory".format(campaign_id)
        self.method = "get"
        self.params = {
            "pageSize": page_size,
            "startDate": start_date,
            "endDate": end_date,
            "nextToken": next_token
        }
        return self.execute()

    def get_budget_rules_by_id(self, budget_rule_id):
        self.uri_path = "/sd/budgetRules/{}".format(budget_rule_id)
        self.method = "get"
        return self.execute()

    def create_budget_rules(self, data):
        self.uri_path = "/sd/budgetRules"
        self.method = "post"
        self.data = data
        return self.execute()

    def get_budget_rules(self, page_size: int, next_token: str = None):
        self.uri_path = "/sd/budgetRules"
        self.method = "get"
        self.params = {
            "pageSize": page_size,
            "nextToken": next_token
        }
        return self.execute()

    def update_budget_rules(self, data):
        self.uri_path = "/sd/budgetRules"
        self.method = "put"
        self.data = data
        return self.execute()

    def get_campaign_budget_rules_by_id(self, budget_rule_id, page_size: int, next_token: str = None):
        self.uri_path = "/sd/budgetRules/{}/campaigns".format(budget_rule_id)
        self.method = "get"
        self.params = {
            "pageSize": page_size,
            "nextToken": next_token
        }
        return self.execute()

    def delete_campaign_budget_rules(self, campaign_id, budget_rule_id):
        self.uri_path = "/sd/campaigns/{}/budgetRules/{}".format(campaign_id, budget_rule_id)
        self.method = "delete"
        return self.execute()

    def associate_campaign_by_id(self, campaign_id, budget_rule_ids: list):
        self.uri_path = "/sd/campaigns/{}/budgetRules".format(campaign_id)
        self.method = "post"
        self.data = {
            "budgetRuleIds": budget_rule_ids
        }
        return self.execute()

    def get_campaign_budget_rules_by_campaign_id(self, campaign_id):
        self.uri_path = "/sd/campaigns/{}/budgetRules".format(campaign_id)
        self.method = "get"
        return self.execute()


