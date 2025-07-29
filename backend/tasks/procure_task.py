from crewai import Task

def get_procure_task(agent, forecast_context):
    return Task(
        agent=agent,
        description="Using forecast data, create purchase orders and select the best suppliers for cement, steel, and tiles.",
        context=[forecast_context],
        expected_output="Purchase orders with vendor, quantity, price, and delivery date.",
        output_file="data/purchase_orders.csv"
    )