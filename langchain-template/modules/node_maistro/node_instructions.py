"""
Node definitions for the Maistro chatbot
"""
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import MessagesState
from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore
from .. import configuration
from ..maistro_prompt import CREATE_INSTRUCTIONS
from ..debug_langgraph import debug_messages, debug_response
from ..core_instance import get_instance


def update_instructions(state: MessagesState, config: RunnableConfig, store: BaseStore):
    """Reflect on the chat history and update the memory collection."""

    # Get the user ID from the config
    configurable = configuration.Configuration.from_runnable_config(config)
    user_id = configurable.user_id
    todo_category = configurable.todo_category

    namespace = ("instructions", todo_category, user_id)

    existing_memory = store.get(namespace, "user_instructions")

    debug_messages("update_instructions", {
        "existing_memory": existing_memory,
    })

    # Format the memory in the system prompt
    system_msg = CREATE_INSTRUCTIONS.format(
        current_instructions=existing_memory.value if existing_memory else None)
    new_memory = get_instance("task_maistro").model.invoke([SystemMessage(content=system_msg)]+state['messages'][:-1] + [
        HumanMessage(content="Please update the instructions based on the conversation")])

    debug_messages("update_instructions", {
        "new_memory": new_memory,
    })

    # Overwrite the existing memory in the store
    key = "user_instructions"
    store.put(namespace, key, {"memory": new_memory.content})
    tool_calls = state['messages'][-1].tool_calls

    # Return tool message with update verification
    return_msg = {"messages": [
        {"role": "tool", "content": "updated instructions", "tool_call_id": tool_calls[0]['id']}]}
    debug_response("update_instructions", return_msg)
    return return_msg
