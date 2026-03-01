from typing import TypedDict, Dict
from langgraph.graph import StateGraph

print("Loading agent2.py")

class AgentState(TypedDict):
    message: str