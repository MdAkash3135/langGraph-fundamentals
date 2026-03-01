from typing import TypedDict, Dict
from langgraph.graph import StateGraph

print("Loading agent1.py")

class AgentState(TypedDict):
    message: str

def greetings_node(state: AgentState) -> AgentState:
    state["message"] = state.get("message", "") + " Hello from Agent 1!"
    return {"message": f"Hello! You said: {state['message']}"}

graph = StateGraph(AgentState)
graph.add_node("greet", greetings_node)

graph.set_entry_point("greet")
graph.set_finish_point("greet")

app = graph.compile()

result = app.invoke({"message": "kire vai "})
print(result)