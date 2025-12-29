
def transport_agent(dest_data, budget):
    cost = dest_data["days"] * 3000

    if cost > budget:
        # Budget exceeded logic
        cost = dest_data["days"] * 2000

    # Transport Selection Logic
    # Thresholds for decision
    HIGH_BUDGET_THRESHOLD = 20000
    SHORT_TRIP_DAYS = 5

    transport_mode = "Train"  # Default

    if budget >= HIGH_BUDGET_THRESHOLD and dest_data["days"] < SHORT_TRIP_DAYS:
        transport_mode = "Plane"
    
    return {
        "transport": transport_mode,
        "hotel_cost": cost
    }
