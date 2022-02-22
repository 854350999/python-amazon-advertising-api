
from ..client import Client


class BudgetRulesRecommendation(Client):

    def get_campaigns_budget_rules_recommendations(self, data):
        self.uri_path = "/sp/campaigns/budgetRules/recommendations"
        self.method = "post"
        self.data = data
        return self.execute()
