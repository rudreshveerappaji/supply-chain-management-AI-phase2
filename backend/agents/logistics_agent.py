from crewai import Agent

LogisticsAgent = Agent(
    role='Logistics Coordinator',
    goal='Ensure timely delivery of materials to worksite with optimal transport routes',
    backstory="""You coordinate with vendors, manage ETAs, update delivery schedules, and reroute shipments
    based on delays or emergencies.""",
    allow_delegation=True,
    verbose=True
)