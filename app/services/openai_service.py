from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def generate_plan_gpt(tags, location, budget, date, weather):
    prompt = f"""
    Create a travel plan with the following details.
    Tags: {', '.join(tags)}
    Location: {location}
    Budget: {budget}원
    Date: {date}
    Weather: {weather}
    Please provide a detailed itinerary including places to visit, activities, and any other relevant information in Korean.
    """
    try:
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print("GPT API Error:", e)
        raise
