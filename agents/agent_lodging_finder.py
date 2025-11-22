from __future__ import annotations

from typing import Dict, Any, List


class LodgingFinderAgent:

    def __init__(self):
        # Base simulée de logements
        self.lodging_database = [
            {
                "lodging_name": "Hôtel simple Porte de Versailles",
                "city": "Paris",
                "platform": "Booking",
                "price_per_night": 80,
                "type": "hôtel"
            },
            {
                "lodging_name": "Studio Airbnb près de la Gare de Lyon",
                "city": "Paris",
                "platform": "Airbnb",
                "price_per_night": 65,
                "type": "airbnb"
            },
            {
                "lodging_name": "Auberge Le Parisien",
                "city": "Paris",
                "platform": "HostelWorld",
                "price_per_night": 35,
                "type": "auberge"
            },
            {
                "lodging_name": "Studio Airbnb proche RER",
                "city": "Cergy",
                "platform": "Airbnb",
                "price_per_night": 55,
                "type": "airbnb"
            }
        ]

    def find_lodgings_for_activity(
        self,
        activity: Dict[str, Any],
        max_lodging_budget: int
    ) -> List[Dict[str, Any]]:

        city = activity["city"].lower()

        matches = []

        for lodging in self.lodging_database:
            # même ville
            if lodging["city"].lower() != city:
                continue

            # budget respecté
            if lodging["price_per_night"] > max_lodging_budget:
                continue

            matches.append({
                "for_activity": activity["name"],
                "lodging_name": lodging["lodging_name"],
                "platform": lodging["platform"],
                "price_per_night": lodging["price_per_night"],
                "nights": 1,
                "total_price": lodging["price_per_night"],
                "type": lodging["type"],
                "city": lodging["city"]
            })

        # On limite à 2 logements maximum
        return matches[:2]

    def find_all_lodgings(
        self,
        activities: List[Dict[str, Any]],
        max_lodging_budget: int
    ) -> Dict[str, List[Dict[str, Any]]]:

        results = {}

        for activity in activities:
            lodgings = self.find_lodgings_for_activity(activity, max_lodging_budget)
            results[activity["name"]] = lodgings

        return results
