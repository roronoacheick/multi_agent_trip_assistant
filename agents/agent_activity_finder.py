# agents/agent_activity_finder.py

from __future__ import annotations

from typing import Dict, Any, List


class ActivityFinderAgent:

    def __init__(self):
        # Base d'activités (simulée mais réaliste)
        self.activity_database = [
            {
                "name": "Aquaboulevard",
                "city": "Paris",
                "type": "piscine / parc aquatique",
                "price_estimate": 35,
                "suitable_weather": ["OK", "Moyen"],
                "tags": ["baignade", "fun"]
            },
            {
                "name": "Piscine Joséphine Baker",
                "city": "Paris",
                "type": "piscine en plein air",
                "price_estimate": 5,
                "suitable_weather": ["OK"],
                "tags": ["baignade"]
            },
            {
                "name": "Base de loisirs de Cergy",
                "city": "Cergy",
                "type": "base de loisirs",
                "price_estimate": 25,
                "suitable_weather": ["OK"],
                "tags": ["baignade", "nature"]
            },
            {
                "name": "Escape Game – HintHunt",
                "city": "Paris",
                "type": "jeu intérieur",
                "price_estimate": 30,
                "suitable_weather": ["Pluie", "Moyen"],
                "tags": ["fun", "intérieur"]
            },
            {
                "name": "Bowling Front de Seine",
                "city": "Paris",
                "type": "activité intérieure",
                "price_estimate": 15,
                "suitable_weather": ["Pluie", "Moyen"],
                "tags": ["fun"]
            }
        ]

    def _preferences_match_tags(
        self,
        preferences: List[str],
        activity_tags: List[str]
    ) -> bool:

        pref_lower_list = [pref.lower() for pref in preferences]
        tag_lower_list = [tag.lower() for tag in activity_tags]

        for pref in pref_lower_list:
            for tag in tag_lower_list:
                if pref in tag or tag in pref:
                    return True

        return False

    def find_activities(
        self,
        location: str,
        preferences: List[str],
        swimming_recommendation: str,
        max_activities_budget: int
    ) -> List[Dict[str, Any]]:

        matched: List[Dict[str, Any]] = []

        # --- 1) Filtrage principal : ville + météo + préférences + budget ---
        for activity in self.activity_database:
            # Ville : on garde simple (même ville)
            if activity["city"].lower() not in location.lower():
                continue

            # Météo : si non compatible, on saute
            if swimming_recommendation not in activity["suitable_weather"]:
                continue

            # Préférences : si la liste n'est pas vide, on filtre
            if preferences:
                if not self._preferences_match_tags(preferences, activity["tags"]):
                    continue

            # Budget
            if activity["price_estimate"] > max_activities_budget:
                continue

            matched.append(activity)

        # --- 2) Fallback : si rien trouvé, élargir un peu les critères ---
        if not matched:
            for activity in self.activity_database:
                # même ville
                if activity["city"].lower() not in location.lower():
                    continue

                # budget respecté
                if activity["price_estimate"] > max_activities_budget:
                    continue

                # météo compatible
                if swimming_recommendation not in activity["suitable_weather"]:
                    continue

                matched.append(activity)

        return matched
