from pydantic import BaseModel
from typing import List

class PlanRequest(BaseModel):
    tags: List[str]
    location: str
    budget: int
    date: str
    weather: str

class PlanResponse(BaseModel):
    plan: str