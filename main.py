from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from time import sleep

from agents.destination_agent import destination_agent
from agents.transport_agent import transport_agent
from agents.itinerary_agent import itinerary_agent

def main():
    console = Console()
    console.print(Panel.fit("Multi-Agent Travel Itinerary CLI", style="bold blue"))

    source = Prompt.ask("Enter source city")
    budget = IntPrompt.ask("Enter budget (INR)")
    days = IntPrompt.ask("Enter number of days")

    with console.status("[bold green]Agents are working...") as status:
        status.update("Destination Agent is selecting a place...")
        sleep(1.0) # Simulate thinking
        dest_data = destination_agent(source, budget, days)
        console.log(f"[green]Selected Destination:[/green] {dest_data['destination']}")

        status.update("Transport Agent is booking flights/hotels...")
        sleep(1.0)
        travel_data = transport_agent(dest_data, budget)
        console.log(f"[green]Transport Configured:[/green] {travel_data['transport']}")

        status.update("Itinerary Agent is generating plan...")
        sleep(1.0)
        itinerary_agent(dest_data, travel_data)

if __name__ == "__main__":
    main()
