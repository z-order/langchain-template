"""
Conditional edge for the Maistro chatbot
"""

from typing import Literal
from langgraph.graph import END
from langgraph.graph.message import MessagesState
from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore
from ..debug_langgraph import debug_conditional_edge


def route_message(state: MessagesState, config: RunnableConfig, store: BaseStore) -> Literal[END, "update_todos", "update_instructions", "update_profile"]:
    """Reflect on the memories and chat history to decide whether to update the memory collection."""
    message = state['messages'][-1]
    if len(message.tool_calls) == 0:
        return END
    else:
        tool_call = message.tool_calls[0]
        if tool_call['args']['update_type'] == "user":
            debug_conditional_edge("route_message", "update_profile", message)
            return "update_profile"
        elif tool_call['args']['update_type'] == "todo":
            debug_conditional_edge("route_message", "update_todos", message)
            return "update_todos"
        elif tool_call['args']['update_type'] == "instructions":
            debug_conditional_edge(
                "route_message", "update_instructions", message)
            return "update_instructions"
        else:
            debug_conditional_edge("route_message", "END",
                                   "Unknown update type -> raise ValueError")
            raise ValueError
