from fastapi import FastAPI
from app.routes import plan, user
from app.models.user_model import Base
from app.services.db import engine

#Create database when app starts
Base.metadata.create_all(bind = engine)

app = FastAPI()
app.include_router(plan.router, prefix = "/api/plan")
app.include_router(user.router, prefix = "/api/user", tags = ["user"])

@app.get("/")

def root():
    return {"message": "Roamie backend is running"}

