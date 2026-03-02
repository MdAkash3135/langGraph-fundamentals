from typing import TypedDict, Dict
from langgraph.graph import StateGraph

print("Loading agent1.py")

class AgentState(TypedDict):
    message: str

def greetings_node(state: AgentState) -> AgentState:
    '''A node that takes a message and appends a greeting to it.'''
    state["message"] = state.get("message", "") + " You are doing an greate job by learning langgraph!"
    return {"message": f"{state['message']}"}

graph = StateGraph(AgentState)
graph.add_node("greet", greetings_node)

graph.set_entry_point("greet")
graph.set_finish_point("greet")

app = graph.compile()

result = app.invoke({"message": "Bob"})
print(result)