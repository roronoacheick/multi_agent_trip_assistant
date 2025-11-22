from __future__ import annotations

from typing import Dict, Any, List


class ScenarioBuilderAgent:

    def __init__(self):
        
        self.transport_estimate = {
            "Paris": 15,
            "Cergy": 20,
            "default": 15
        }

    def estimate_transport_cost(self, city: str) -> int:
        city_lower = city.lower()
        if "paris" in city_lower:
            return self.transport_estimate["Paris"]
        if "cergy" in city_lower:
            return self.transport_estimate["Cergy"]
        return self.transport_estimate["default"]

    def build_scenarios(
        self,
        activities: List[Dict[str, Any]],
        lodging_options: Dict[str, List[Dict[str, Any]]],
        budget_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:

        scenarios = []

        for activity in activities:
            activity_name = activity["name"]
            activity_city = activity["city"]
            activity_price = activity["price_estimate"]

            # Transport
            transport_cost = self.estimate_transport_cost(activity_city)

            # Logements associés à cette activité
            lodgings = lodging_options.get(activity_name, [])

            for lodging in lodgings:
                lodging_total = lodging["total_price"]

                total_cost = activity_price + lodging_total + transport_cost

                # Respect du budget total
                if total_cost > budget_data["budget_total"]:
                    continue

                scenarios.append({
                    "label": f"Option - {activity_name}",
                    "total_cost_estimate": total_cost,
                    "details": {
                        "activity": {
                            "name": activity_name,
                            "price": activity_price,
                            "type": activity["type"],
                            "city": activity_city
                        },
                        "lodging": lodging,
                        "transport_estimate": transport_cost
                    }
                })

        # Trier du moins cher au plus cher
        scenarios.sort(key=lambda x: x["total_cost_estimate"])

        return scenarios[:3]
