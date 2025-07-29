from crewai import Task

def get_logistics_task(agent, procurement_context):
    return Task(
        agent=agent,
        description="Coordinate delivery logistics for all approved purchase orders including vehicle scheduling and estimated delivery times.",
        context=[procurement_context],
        expected_output="Delivery schedule with shipment tracking details.",
        output_file="data/delivery_schedule.csv"
    )