from agents.agent_analyze_request import AnalyzeRequestAgent
from agents.agent_budget_planner import BudgetPlannerAgent
from agents.agent_weather_checker import WeatherCheckerAgent


def main():
    print("Assistant multi-agent - Test Analyse + Budget + Météo")
    user_message = input("Entrez votre message : ")

    # 1) Analyse
    analyzer = AnalyzeRequestAgent()
    parsed_constraints = analyzer.analyze(user_message)
    print("\n[Agent 1] Contraintes extraites :")
    print(parsed_constraints)

    # 2) Budget
    budget_agent = BudgetPlannerAgent()
    budget_data = budget_agent.compute_budget(parsed_constraints)
    print("\n[Agent 2] Budget calculé :")
    print(budget_data)

    # 3) Météo
    weather_agent = WeatherCheckerAgent()
    weather_info = weather_agent.get_weather_summary(parsed_constraints["location"])
    print("\n[Agent 3] Météo :")
    print(weather_info)


if __name__ == "__main__":
    main()
