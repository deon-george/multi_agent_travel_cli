
def transport_agent(dest_data, budget):
    cost = dest_data["days"] * 3000

    if cost > budget:
        # Budget exceeded logic
        cost = dest_data["days"] * 2000

    return {
        "transport": "Train",
        "hotel_cost": cost
    }
