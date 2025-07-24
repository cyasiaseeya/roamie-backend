from fastapi import APIRouter
from app.models.plan_model import PlanRequest, PlanResponse
from app.services.llm_service import generate_plan_llm

router = APIRouter()

@router.post("/generate_plan", response_model = PlanResponse)
def create_plan(request: PlanRequest):
    print("Incoming request:", request.model_dump())
    result = generate_plan_llm(
        tags = request.tags,
        location = request.location,
        budget = request.budget,
        date = request.date,
        weather = request.weather
    )

    return PlanResponse(plan = result)
