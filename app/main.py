from fastapi import FastAPI
from app.routes import plan

app = FastAPI()
app.include_router(plan.router, prefix = "/api/plan")

@app.get("/")

def root():
    return {"message": "Roamie backend is running"}

