
from ..client import Client


class BudgetRecommendations(Client):

    def get_campaigns_budget_recommendations(self, campaign_ids: list):
        self.uri_path = "/sp/campaigns/budgetRecommendations"
        self.method = "post"
        self.data = {
            "campaignIds": campaign_ids
        }
        return self.execute()
