import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def destination_agent(source, budget, days):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[bold red]Error: GEMINI_API_KEY not found.[/bold red]") 
        return {
            "source": source,
            "destination": "Default City",
            "days": days,
            "reason": "API Key Missing"
        }

    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-flash-latest')

    prompt = f"""
    Suggest a travel destination based on the following constraints:
    - Source City: {source}
    - Budget: {budget} INR
    - Trip Duration: {days} days

    Return ONLY a JSON object with the following keys:
    - "destination": Name of the city/place
    - "days": The same trip duration as input ({days})
    - "reason": A short reason for the choice

    Ensure the output is valid JSON. Do not include markdown formatting like ```json ... ```.
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        
        result = json.loads(text)

        return {
            "source": source,
            "destination": result.get("destination", "Unknown"),
            "days": result.get("days", days),
            "reason": result.get("reason", "No reason provided")
        }
    except Exception as e:
        print(f"AI Agent Error: {e}")
        return {
            "source": source,
            "destination": "Goa (Fallback)",
            "days": days,
            "reason": "AI Error"
        }
