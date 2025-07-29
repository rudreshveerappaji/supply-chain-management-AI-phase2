from .forecast_task import get_forecast_task
from .procure_task import get_procure_task
from .logistics_task import get_logistics_task
from .site_task import get_site_task

def setup_tasks(agents):
    forecast_task = get_forecast_task(agents["ForecastingAgent"])
    procure_task = get_procure_task(agents["ProcurementAgent"], forecast_task)
    logistics_task = get_logistics_task(agents["LogisticsAgent"], procure_task)
    site_task = get_site_task(agents["SiteManagerAgent"], logistics_task)
    return [forecast_task, procure_task, logistics_task, site_task]