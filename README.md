# Multi-Agent Travel CLI

A CLI-based travel itinerary generator using a multi-agent system.

## Setup

1.  **Clone the repository** and navigate to the project directory.
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Environment**:
    - Open `.env` and add your API keys (if applicable in future updates).

## Usage

Run the main script:

```bash
python main.py
```

Follow the on-screen prompts to enter your source city, budget, and travel details.

## Agents

- **Destination Agent**: Suggests destinations based on budget.
- **Transport Agent**: Calculates transport and stay costs.
- **Itinerary Agent**: Generates a day-wise plan.


### Architecture Diagram

┌──────────────────────────┐
│          User            │
│  (CLI Input: City,       │
│   Budget, Days)          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│   Travel CLI Interface   │
│  (Input Handling & UX)   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────────────────────┐
│        Multi-Agent Orchestrator           │
│  (Controls agent execution flow)         │
└────────────┬─────────────┬───────────────┘
             │             │
             │             │
             ▼             ▼
┌──────────────────┐   ┌──────────────────┐
│ Destination Agent│   │ Transport Agent  │
│ • Selects region │   │ • Chooses travel │
│ • Picks circuit  │   │   mode (Train)  │
│ • Filters by     │   │ • Budget aware  │
│   budget/days    │   └──────────────────┘
└────────────┬─────┘
             │
             ▼
┌──────────────────────────┐
│     Itinerary Agent      │
│ • Day-wise planning      │
│ • City sequencing        │
│ • Activity generation    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│     Output Formatter     │
│ • Table layout           │
│ • Trip summary           │
│ • CLI rendering          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Final Itinerary     │
│ (10-day plan + summary)  │
└──────────────────────────┘
