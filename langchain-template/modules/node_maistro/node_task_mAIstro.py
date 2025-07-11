"""
Node definitions for the Maistro chatbot
"""

from langgraph.graph import MessagesState
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import SystemMessage
from langgraph.store.base import BaseStore
from ..maistro_prompt import MODEL_SYSTEM_MESSAGE
from ..maistro_schema import UpdateMemory
from ..debug_langgraph import debug_messages, debug_response
from .. import configuration
from ..core_instance import get_instance


def task_mAIstro(state: MessagesState, config: RunnableConfig, store: BaseStore):
    """Load memories from the store and use them to personalize the chatbot's response."""

    # Get the user ID from the config
    configurable = configuration.Configuration.from_runnable_config(config)
    user_id = configurable.user_id
    todo_category = configurable.todo_category
    task_maistro_role = configurable.task_maistro_role

   # Retrieve profile memory from the store
    namespace = ("profile", todo_category, user_id)
    memories = store.search(namespace)
    if memories:
        user_profile = memories[0].value
    else:
        user_profile = None

    # Retrieve people memory from the store
    namespace = ("todo", todo_category, user_id)
    memories = store.search(namespace)
    todo = "\n".join(f"{mem.value}" for mem in memories)

    # Retrieve custom instructions
    namespace = ("instructions", todo_category, user_id)
    memories = store.search(namespace)
    if memories:
        instructions = memories[0].value
    else:
        instructions = ""

    system_msg = MODEL_SYSTEM_MESSAGE.format(
        task_maistro_role=task_maistro_role, user_profile=user_profile, todo=todo, instructions=instructions)

    debug_messages("task_mAIstro", {
        "system_msg": system_msg,
        "state['messages']": state["messages"],
    })

    # Respond using memory as well as the chat history
    response = get_instance("task_maistro").model.bind_tools([UpdateMemory], parallel_tool_calls=False).invoke(
        [SystemMessage(content=system_msg)]+state["messages"])

    debug_response("task_mAIstro", response)

    return {"messages": [response]}
