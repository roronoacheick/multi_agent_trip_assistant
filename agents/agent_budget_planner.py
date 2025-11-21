from __future__ import annotations

from typing import Dict, Any


class BudgetPlannerAgent:

    def __init__(self):
        # Ratios de répartition du budget
        self.ratio_lodging = 0.60     
        self.ratio_activities = 0.30  
        self.ratio_transport = 0.10   

        self.minimal_budget = 50

    def compute_budget(self, parsed_constraints: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prend le JSON de l'agent d'analyse et renvoie un budget structuré.
        """

        total_budget = parsed_constraints.get("budget_total")

        if total_budget is None:
            raise ValueError(
                "Aucun budget n'a été précisé par l'utilisateur. "
                "Impossible de construire un plan de sortie."
            )

        if total_budget < self.minimal_budget:
            raise ValueError(
                f"Le budget total ({total_budget}€) est trop faible. "
                f"Il faut au moins {self.minimal_budget}€."
            )

        # Calculs de répartition
        lodging_max = int(total_budget * self.ratio_lodging)
        activities_max = int(total_budget * self.ratio_activities)
        transport_max = int(total_budget * self.ratio_transport)

        return {
            "budget_total": total_budget,
            "max_lodging": lodging_max,
            "max_activities": activities_max,
            "max_transport": transport_max
        }
