from agents import setup_agents
from tasks import setup_tasks
from crewai import Crew

def main():
    print("Setting up agents...")
    agents = setup_agents()

    print("Creating task flow...")
    tasks = setup_tasks(agents)

    print("Launching CrewAI multi-agent system...")
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True,
        memory=True
    )

    result = crew.run()
    print("Final result:", result)

if __name__ == "__main__":
    main()