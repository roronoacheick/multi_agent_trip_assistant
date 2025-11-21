from agents.agent_analyze_request import AnalyzeRequestAgent
from agents.agent_budget_planner import BudgetPlannerAgent

def main():
    print("Assistant multi-agent - Test Analyse + Budget")
    user_message = input("Entrez votre message : ")

    # 1) Agent 1 - Analyse
    analyzer = AnalyzeRequestAgent()
    parsed_constraints = analyzer.analyze(user_message)

    print("\nJSON extrait (Agent 1) :")
    print(parsed_constraints)

    # 2) Agent 2 - Budget
    budget_agent = BudgetPlannerAgent()
    budget_data = budget_agent.compute_budget(parsed_constraints)

    print("\nRépartition du budget (Agent 2) :")
    print(budget_data)


if __name__ == "__main__":
    main()
