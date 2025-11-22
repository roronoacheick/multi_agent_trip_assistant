from agents.agent_analyze_request import AnalyzeRequestAgent
from agents.agent_budget_planner import BudgetPlannerAgent
from agents.agent_weather_checker import WeatherCheckerAgent
from agents.agent_activity_finder import ActivityFinderAgent
from agents.agent_lodging_finder import LodgingFinderAgent
from agents.agent_scenario_builder import ScenarioBuilderAgent
from agents.agent_presenter import PresenterAgent





def main():
    print("=== Assistant Multi-Agent – Test Étapes 1 à 4 ===\n")

    user_message = input("Entrez votre message : ")

    # --- 1) Agent 1 : Analyse de la demande ---
    analyzer = AnalyzeRequestAgent()
    parsed_constraints = analyzer.analyze(user_message)

    print("\n[Agent 1] Contraintes extraites :")
    print(parsed_constraints)

    # --- 2) Agent 2 : Calcul du budget ---
    budget_agent = BudgetPlannerAgent()
    budget_data = budget_agent.compute_budget(parsed_constraints)

    print("\n[Agent 2] Répartition du budget :")
    print(budget_data)

    # --- 3) Agent 3 : Météo réelle ---
    weather_agent = WeatherCheckerAgent()
    location = parsed_constraints["location"]
    weather_info = weather_agent.get_weather_summary(location)

    print("\n[Agent 3] Données météo :")
    print(weather_info)

    # --- 4) Agent 4 : Activités ---
    activity_agent = ActivityFinderAgent()
    activities = activity_agent.find_activities(
        location=parsed_constraints["location"],
        preferences=parsed_constraints["preferences"],
        swimming_recommendation=weather_info["swimming_recommendation"],
        max_activities_budget=budget_data["max_activities"]
    )

    print("\n[Agent 4] Activités compatibles :")
    print(activities)

    print("\n=== Fin du test (Étapes 1 → 4) ===")


    # 5) Agent 5 - Logements
    lodging_agent = LodgingFinderAgent()
    lodging_options = lodging_agent.find_all_lodgings(
        activities=activities,
        max_lodging_budget=budget_data["max_lodging"]
    )

    print("\n[Agent 5] Logements compatibles :")
    print(lodging_options)



    # --- 6) Agent 6 : Scénarios ---
    scenario_agent = ScenarioBuilderAgent()
    scenarios = scenario_agent.build_scenarios(
        activities=activities,
        lodging_options=lodging_options,
        budget_data=budget_data
    )

    print("\n[Agent 6] Scénarios proposés :")
    for s in scenarios:
        print(s)



    # --- 7) Agent 7 : Présentation Finale ---
    presenter = PresenterAgent()
    final_text = presenter.present(
        scenarios=scenarios,
        constraints=parsed_constraints,
        weather=weather_info
    )

    print("\n=== Recommandations finales ===")
    print(final_text)


if __name__ == "__main__":
    main()
