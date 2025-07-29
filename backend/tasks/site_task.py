from crewai import Task

def get_site_task(agent, delivery_context):
    return Task(
        agent=agent,
        description="Monitor delivery arrivals and update the system with confirmation and usage data.",
        context=[delivery_context],
        expected_output="On-site delivery confirmation report.",
        output_file="data/site_usage_log.csv"
    )