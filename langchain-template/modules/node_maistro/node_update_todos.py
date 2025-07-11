"""
Node definitions for the Maistro chatbot
"""

import uuid
from datetime import datetime
from langgraph.graph import MessagesState
from langgraph.store.base import BaseStore
from trustcall import create_extractor
from langchain_core.messages import SystemMessage, merge_message_runs
from langchain_core.runnables import RunnableConfig
from .. import configuration
from ..debug_langgraph import debug_messages, debug_response, debug_result
from ..maistro_prompt import TRUSTCALL_INSTRUCTION
from ..maistro_schema import ToDo
from ..utils_spy import Spy
from ..utils_tool import extract_tool_info
from ..core_instance import get_instance


def update_todos(state: MessagesState, config: RunnableConfig, store: BaseStore):
    """Reflect on the chat history and update the memory collection."""

    # Get the user ID from the config
    configurable = configuration.Configuration.from_runnable_config(config)
    user_id = configurable.user_id
    todo_category = configurable.todo_category

    # Define the namespace for the memories
    namespace = ("todo", todo_category, user_id)

    # Retrieve the most recent memories for context
    existing_items = store.search(namespace)

    # Format the existing memories for the Trustcall extractor
    tool_name = "ToDo"
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

    # Initialize the spy for visibility into the tool calls made by Trustcall
    spy = Spy()

    # Create the Trustcall extractor for updating the ToDo list
    todo_extractor = create_extractor(
        get_instance("task_maistro").model,
        tools=[ToDo],
        tool_choice=tool_name,
        enable_inserts=True
    ).with_listeners(on_end=spy)

    debug_messages("update_todos", {
        "updated_messages": updated_messages,
        "existing_memories": existing_memories,
    })

    # Invoke the extractor
    result = todo_extractor.invoke({"messages": updated_messages,
                                    "existing": existing_memories})

    debug_result("update_todos", "todo_extractor.invoke", result)

    # Save save the memories from Trustcall to the store
    for r, rmeta in zip(result["responses"], result["response_metadata"]):
        store.put(namespace,
                  rmeta.get("json_doc_id", str(uuid.uuid4())),
                  r.model_dump(mode="json"),
                  )

    # Respond to the tool call made in task_mAIstro, confirming the update
    tool_calls = state['messages'][-1].tool_calls

    # Extract the changes made by Trustcall and add the the ToolMessage returned to task_mAIstro
    todo_update_msg = extract_tool_info(spy.called_tools, tool_name)

    return_msg = {"messages": [
        {"role": "tool", "content": todo_update_msg, "tool_call_id": tool_calls[0]['id']}]}
    debug_response("update_todos", return_msg)
    return return_msg
