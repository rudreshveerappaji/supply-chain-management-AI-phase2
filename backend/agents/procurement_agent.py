from crewai import Agent

ProcurementAgent = Agent(
    role='Procurement Manager',
    goal='Secure quality materials at optimal prices on time',
    backstory="""You are responsible for sourcing materials based on forecasts, verifying vendor quality,
    negotiating pricing, and coordinating purchase orders with the finance team.""",
    allow_delegation=True,
    verbose=True
)