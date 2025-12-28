import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
from rich.table import Table
from rich.markdown import Markdown

def itinerary_agent(dest_data, travel_data):
    console = Console()
    days = dest_data["days"]
    destination = dest_data["destination"]
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        console.print("[bold red]Error: GEMINI_API_KEY not found. Using fallback.[/bold red]")
        activities = [f"Explore {destination} attractions" for _ in range(days)]
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-flash-latest')
            
            prompt = f"""
            Create a day-by-day itinerary for a {days}-day trip to {destination}.
            
            Return ONLY a JSON object with a key "activities" containing a list of strings.
            Each string should be a brief summary of activities for that day (e.g., "Visit the City Palace and take a boat ride on Lake Pichola").
            The list must have exactly {days} items.
            
            Example JSON:
            {{
                "activities": ["Day 1 activities...", "Day 2 activities..."]
            }}
            """
            
            response = model.generate_content(prompt)
            text = response.text.strip()
            
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
                
            data = json.loads(text)
            activities = data.get("activities", [])
            
            # Fill with generic text if AI returns fewer days
            while len(activities) < days:
                activities.append(f"Explore more of {destination}")
                
        except Exception as e:
            console.print(f"[red]AI Error generating itinerary: {e}[/red]")
            activities = [f"Explore {destination} attractions" for _ in range(days)]

    table = Table(title=f"Itinerary for {destination}")
    table.add_column("Day", justify="center", style="cyan", no_wrap=True)
    table.add_column("Activity", style="magenta")

    for i, activity in enumerate(activities):
        table.add_row(f"Day {i+1}", activity)

    console.print(table)

    summary_md = f"""
# Trip Summary
- **Destination:** {destination}
- **Duration:** {days} days
- **Transport:** {travel_data['transport']}
- **Hotel Cost:** INR {travel_data['hotel_cost']}
    """
    console.print(Markdown(summary_md))
