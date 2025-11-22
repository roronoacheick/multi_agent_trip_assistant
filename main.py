from agents.agent_orchestrator import OrchestratorAgent


def main():
    print("=== Assistant Multi-Agent – Version Orchestrateur ===\n")

    user_message = input("Entrez votre message : ")

    orchestrator = OrchestratorAgent()
    final_answer = orchestrator.run(user_message)

    print("\n=== Recommandation finale ===\n")
    print(final_answer)


if __name__ == "__main__":
    main()
