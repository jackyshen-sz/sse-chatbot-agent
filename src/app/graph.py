from langgraph_swarm import create_swarm

from app.agents.agent_factory import get_agents
from app.config import settings
from app.core.async_utils import run_async
from app.llm.sse_llm import create_llm

context = {
  "openai_type": "together",
  "api_key": settings.TOGETHER_API_KEY,
  "model": settings.DEFAULT_MODEL,
}

llm = create_llm(context.get("openai_type"), context)

agents = run_async(get_agents, llm)

agent_graphs = [
  agent.agent_graph
  for agent in agents
]

graph = create_swarm(
  agents=agent_graphs,
  default_active_agent="llm"
).compile()
