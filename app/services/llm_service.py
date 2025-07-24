from app.services.openai_service import generate_plan_gpt

def generate_plan_llm(tags, location, budget, date, weather, model = "gpt"):
    if model == "gpt":
        return generate_plan_gpt(tags, location, budget, date, weather)
    
    #add else if conditions for other models

    raise ValueError("Unsupported model type provided.")
