Multi-Agent Travel CLI
A CLI-based travel itinerary generator using a multi-agent system.

Team Details:
Name: DEON GEORGE
Institution: St. Joseph’s College of engineering and technology,palai

Challenge Selected:
Multi-agent travel itinerary engine

Problem Statement:
Kind it difficult to plans the days of the vacation or find difficult in getting
the best hotel for your budget and don’t know which is can be the best
mode of transportation for thr trip

Solution Overview:
The objective of this project is to design and implement a multi-agent travel
itinerary planning system that collaboratively generates a complete travel plan
based on user inputs such as budget, source location, and travel period.
The system is implemented as a command-line interface (CLI) and works offline,
without relying on external APIs.


Agentic Design:

This multi-agent has 3 agents
Agents
- **Destination Agent**: Suggests destinations based on budget.
- **Transport Agent**: Calculates transport and stay costs.
- **Itinerary Agent**: Generates a day-wise plan.
I have done this multi-agent to work in a sequential manner, the orchestrator i.e
the main.py connects to the 3 agents. the inputs and the outputs from each agents
is collected by the orchestrator and given as the output for the user.
Both the destination agent and itinerary agent is LLM based but the transport
agent is a rule-based agent which is if the trip is below certain amount it choose
train otherwise it choose plane as the mode of transport.

Features:
The user enters source city, budget(in INR), number of days the multi agent find
out the most favorable destination and the mode of transport along with itinerary
plan for the days, in addition it give the hotel cost for stay in that region.

Demo:https://drive.google.com/file/d/1uDhlGLxAQ2_dyMu8QZ9Zhy7D6O3fPTCs/view?usp=sharing

System Architecture:
<img width="2240" height="1400" alt="Screenshot From 2026-01-05 23-06-14" src="https://github.com/user-attachments/assets/cefe34f4-0ad0-4b1c-afca-579ea09b9b7b" />

How to Run the Project:
1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```
3. **Configure Environment**:
- Open `.env` and add your API keys (if applicable in future updates).
## Usage
Run the main script:
```bash
python main.py
```
Tech Stack:
Python 3
Core language used to implement all agents and system logic
Command Line Interface (CLI)
Rich (Python Library)
Used for:
Styled terminal output
Panels, tables, and colored text
Improved readability and user experience in the terminal.

Limitations & Future Work:
Limitations:-
The system currently operates only as a Command Line Interface (CLI), which
limits accessibility for non-technical users.
Travel data such as destinations, transport options, and costs are static and
rule-based, not real-time.
The system does not support live booking, ticket reservations, or payment
integration.
Future Work:-
The system can be extended into a web application or website using modern web
frameworks to improve usability and reach a wider audience.
A graphical user interface (GUI) can be developed to replace the CLI, making the
system more user-friendly.
Real-time travel data APIs can be integrated for live flight, hotel, and pricing
information.

Ethics, Safety & Responsible AI:
The system provides advisory recommendations only, keeping
full decision control with the user.
No personal data is stored, shared, or transmitted; all
processing is done locally.
The application performs no real-world actions such as
bookings or payments, ensuring safety.
The system uses transparent, rule-based logic, avoiding biased
or unpredictable AI behavior.
Any future AI integration will follow responsible and ethical
usage principles.

Made with ❤️ by Deon George
