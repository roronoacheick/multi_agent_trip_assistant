from __future__ import annotations

from typing import Dict, Any

from agents.agent_analyze_request import AnalyzeRequestAgent
from agents.agent_budget_planner import BudgetPlannerAgent
from agents.agent_weather_checker import WeatherCheckerAgent
from agents.agent_activity_finder import ActivityFinderAgent
from agents.agent_lodging_finder import LodgingFinderAgent
from agents.agent_scenario_builder import ScenarioBuilderAgent
from agents.agent_presenter import PresenterAgent


class OrchestratorAgent:

    def __init__(self):
        self.analyzer = AnalyzeRequestAgent()
        self.budget_agent = BudgetPlannerAgent()
        self.weather_agent = WeatherCheckerAgent()
        self.activity_agent = ActivityFinderAgent()
        self.lodging_agent = LodgingFinderAgent()
        self.scenario_agent = ScenarioBuilderAgent()
        self.presenter_agent = PresenterAgent()

    def run(self, user_message: str) -> str:

        # 1) Analyse de la demande
        parsed_constraints = self.analyzer.analyze(user_message)

        # 2) Calcul du budget
        budget_data = self.budget_agent.compute_budget(parsed_constraints)

        # 3) Météo
        weather_info = self.weather_agent.get_weather_summary(
            parsed_constraints["location"]
        )

        # 4) Activités compatibles
        activities = self.activity_agent.find_activities(
            location=parsed_constraints["location"],
            preferences=parsed_constraints["preferences"],
            swimming_recommendation=weather_info["swimming_recommendation"],
            max_activities_budget=budget_data["max_activities"]
        )

        # 5) Logements associés aux activités
        lodging_options = self.lodging_agent.find_all_lodgings(
            activities=activities,
            max_lodging_budget=budget_data["max_lodging"]
        )

        # 6) Scénarios complets
        scenarios = self.scenario_agent.build_scenarios(
            activities=activities,
            lodging_options=lodging_options,
            budget_data=budget_data
        )

        # 7) Présentation finale
        final_text = self.presenter_agent.present(
            scenarios=scenarios,
            constraints=parsed_constraints,
            weather=weather_info
        )

        return final_text
