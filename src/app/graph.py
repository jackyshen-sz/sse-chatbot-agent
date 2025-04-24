from langchain_together import ChatTogether
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

TOGETHER_API_KEY = "fb2dbf62bf0bc04bcebd0211dced579561f8b90fbfc27de4f40675c43a468635"
model = ChatTogether(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  temperature=0.7,
  api_key=TOGETHER_API_KEY
)


def book_hotel(hotel_name: str):
  """Book a hotel"""
  return f"Successfully booked a stay at {hotel_name}."


def book_flight(from_airport: str, to_airport: str):
  """Book a flight"""
  return f"Successfully booked a flight from {from_airport} to {to_airport}."


flight_assistant = create_react_agent(
  model=model,
  tools=[book_flight],
  prompt="You are a flight booking assistant",
  name="flight_assistant"
)

hotel_assistant = create_react_agent(
  model=model,
  tools=[book_hotel],
  prompt="You are a hotel booking assistant",
  name="hotel_assistant"
)

graph = create_supervisor(
  agents=[flight_assistant, hotel_assistant],
  model=model,
  prompt=(
    "You manage a hotel booking assistant and a"
    "flight booking assistant. Assign work to them."
  )
).compile()
