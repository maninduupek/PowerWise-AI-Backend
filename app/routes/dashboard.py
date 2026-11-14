
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard():
    return {
        "today_consumption": 12.5,
        "monthly_consumption": 245,
        "estimated_cost": 4500,
        "unit": "kWh",
        "currency": "LKR"
    }
