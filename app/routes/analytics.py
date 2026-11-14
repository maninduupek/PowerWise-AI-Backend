
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/analytics",
    tags=["Energy Analytics"]
)


@router.get("/daily")
def get_daily_analytics():
    return {
        "period": "daily",
        "unit": "kWh",
        "consumption": [
            {"day": "Monday", "usage": 1.8},
            {"day": "Tuesday", "usage": 2.4},
            {"day": "Wednesday", "usage": 1.5},
            {"day": "Thursday", "usage": 2.8},
            {"day": "Friday", "usage": 2.1},
            {"day": "Saturday", "usage": 1.9},
            {"day": "Sunday", "usage": 2.5}
        ],
        "total": 15.0
    }


@router.get("/weekly")
def get_weekly_analytics():
    return {
        "period": "weekly",
        "unit": "kWh",
        "consumption": [
            {"week": "Week 1", "usage": 42},
            {"week": "Week 2", "usage": 55},
            {"week": "Week 3", "usage": 48},
            {"week": "Week 4", "usage": 63}
        ],
        "total": 208
    }


@router.get("/monthly")
def get_monthly_analytics():
    return {
        "period": "monthly",
        "unit": "kWh",
        "consumption": [
            {"month": "January", "usage": 180},
            {"month": "February", "usage": 195},
            {"month": "March", "usage": 210},
            {"month": "April", "usage": 245}
        ],
        "total": 830
    }
