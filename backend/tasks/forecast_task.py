from crewai import Task

def get_forecast_task(agent):
    return Task(
        agent=agent,
        description="Analyze current usage trends and generate a 2-week forecast for key materials like cement, steel, and tiles.",
        expected_output="CSV file with material forecasts including item name, quantity, and projected date of use.",
        output_file="data/material_forecast.csv"
    )