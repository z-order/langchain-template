"""
Node definitions for the Maistro chatbot
"""

import uuid
from datetime import datetime
from langgraph.graph import MessagesState
from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore
from langchain_core.messages import SystemMessage, merge_message_runs
from ..debug_langgraph import debug_messages, debug_response, debug_result
from ..maistro_prompt import TRUSTCALL_INSTRUCTION
from ..core_instance import get_instance
from .. import configuration


def update_profile(state: MessagesState, config: RunnableConfig, store: BaseStore):
    """Reflect on the chat history and update the memory collection."""

    # Get the user ID from the config
    configurable = configuration.Configuration.from_runnable_config(config)
    user_id = configurable.user_id
    todo_category = configurable.todo_category

    # Define the namespace for the memories
    namespace = ("profile", todo_category, user_id)

    # Retrieve the most recent memories for context
    existing_items = store.search(namespace)

    # Format the existing memories for the Trustcall extractor
    tool_name = "Profile"
    existing_memories = ([(existing_item.key, tool_name, existing_item.value)
                          for existing_item in existing_items]
                         if existing_items
                         else None
                         )

    # Merge the chat history and the instruction
    TRUSTCALL_INSTRUCTION_FORMATTED = TRUSTCALL_INSTRUCTION.format(
        time=datetime.now().isoformat())
    updated_messages = list(merge_message_runs(messages=[SystemMessage(
        content=TRUSTCALL_INSTRUCTION_FORMATTED)] + state["messages"][:-1]))

    debug_messages("update_profile", {
        "state['messages']": state["messages"],
        "updated_messages": updated_messages,
        "existing_memories": existing_memories,
    })

    # Invoke the extractor
    result = get_instance("task_maistro").profile_extractor.invoke({"messages": updated_messages,
                                                                    "existing": existing_memories})

    debug_result("update_profile", "profile_extractor.invoke", result)

    # Save save the memories from Trustcall to the store
    for r, rmeta in zip(result["responses"], result["response_metadata"]):
        store.put(namespace,
                  rmeta.get("json_doc_id", str(uuid.uuid4())),
                  r.model_dump(mode="json"),
                  )
    tool_calls = state['messages'][-1].tool_calls

    # Return tool message with update verification
    return_msg = {"messages": [
        {"role": "tool", "content": "updated profile", "tool_call_id": tool_calls[0]['id']}]}
    debug_response("update_profile", return_msg)
    return return_msg
