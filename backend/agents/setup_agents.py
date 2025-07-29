from .procurement_agent import ProcurementAgent
from .forecasting_agent import ForecastingAgent
from .logistics_agent import LogisticsAgent
from .site_manager_agent import SiteManagerAgent

def setup_agents():
    return {
        "ProcurementAgent": ProcurementAgent,
        "ForecastingAgent": ForecastingAgent,
        "LogisticsAgent": LogisticsAgent,
        "SiteManagerAgent": SiteManagerAgent
    }