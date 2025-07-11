"""
Debug Logger Module

This module provides utilities for safely serializing and logging LangChain objects
and other complex data structures for debugging purposes.
"""

import json
import os
from typing import Any, Dict, Optional

# Handle common LangChain message types
try:
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
except ImportError:
    AIMessage = HumanMessage = SystemMessage = BaseMessage = None

# Global flag to enable/disable logging
DEBUG_LANGGRAPH_MESSAGES = os.environ.get(
    "DEBUG_LANGGRAPH_MESSAGES", "False").lower() == "true"


def safe_serialize_message(msg: Any) -> Any:
    """
    Safely serialize messages and objects for JSON printing.

    This function handles various types of objects including:
    - Pydantic models (v1 and v2)
    - LangChain message objects
    - Lists and dictionaries
    - Exceptions
    - Objects with __dict__ attribute

    Args:
        msg: The message or object to serialize

    Returns:
        Serialized representation of the message
    """

    # Handle Pydantic v2 and v1 models
    if hasattr(msg, "model_dump"):
        return msg.model_dump()
    elif hasattr(msg, "dict"):
        return msg.dict()
    # Handle list of messages recursively
    elif isinstance(msg, list):
        return [safe_serialize_message(m) for m in msg]
    # Handle dicts, but recursively serialize values
    elif isinstance(msg, dict):
        return {k: safe_serialize_message(v) for k, v in msg.items()}
    # Handle common error types
    elif isinstance(msg, Exception):
        return {"error_type": type(msg).__name__, "error_message": str(msg)}
    # Handle objects with __dict__ attribute
    elif hasattr(msg, "__dict__"):
        return {k: safe_serialize_message(v) for k, v in msg.__dict__.items()}
    # Handle LangChain message objects
    if AIMessage and isinstance(msg, AIMessage):
        return {"type": "AIMessage", "content": msg.content}
    elif HumanMessage and isinstance(msg, HumanMessage):
        return {"type": "HumanMessage", "content": msg.content}
    elif SystemMessage and isinstance(msg, SystemMessage):
        return {"type": "SystemMessage", "content": msg.content}
    elif BaseMessage and isinstance(msg, BaseMessage):
        # fallback for other message types
        return {"type": msg.__class__.__name__, "content": getattr(msg, "content", str(msg))}
    # Fallback to string
    return str(msg)


def serialized_print(label: str, data: Dict[str, Any], indent: int = 2, ensure_ascii: bool = False) -> None:
    """
    Print serialized data with function name prefix for debugging.

    Args:
        label: Label of the data being debugged
        data: Dictionary of data to serialize and print
        indent: JSON indentation level (default: 2)
        ensure_ascii: Whether to ensure ASCII output (default: False)
    """
    if not DEBUG_LANGGRAPH_MESSAGES:
        return

    # Serialize the data
    serialized_data = safe_serialize_message(data)

    # Print with function name prefix
    print(f'\n\n---- {label} ----\n\n')
    # print(serialized_data, '\n\n', sep='')
    print(json.dumps(serialized_data, indent=indent,
                     ensure_ascii=ensure_ascii), '\n\n', sep='')


def set_debug_mode(enabled: bool) -> None:
    """
    Set the debug mode globally.

    Args:
        enabled: Whether to enable debug logging
    """
    global DEBUG_LANGGRAPH_MESSAGES
    DEBUG_LANGGRAPH_MESSAGES = enabled


def is_debug_enabled() -> bool:
    """
    Check if debug mode is enabled.

    Returns:
        True if debug mode is enabled, False otherwise
    """
    return DEBUG_LANGGRAPH_MESSAGES


# Convenience functions for common debug patterns
def debug_response(fn_name: str, response: Any) -> None:
    """
    Debug print a response object.

    Args:
        fn_name: Name of the function/routine
        response: Response object to debug
    """
    serialized_print(f"{fn_name}() response", safe_serialize_message(response))


def debug_messages(fn_name: str, messages: Any) -> None:
    """
    Debug print messages.

    Args:
        fn_name: Name of the function/routine
        messages: Messages to debug
    """
    serialized_print(f"{fn_name}() messages", safe_serialize_message(messages))


def debug_state(fn_name: str, state: Any) -> None:
    """
    Debug print state.

    Args:
        fn_name: Name of the function/routine
        state: State to debug
    """
    serialized_print(f"{fn_name}() state", safe_serialize_message(state))


def debug_result(fn_name: str, fn_sub_name: str, result: Any) -> None:
    """
    Debug print a result object.

    Args:
        fn_name: Name of the function/routine
        fn_sub_name: Name of the sub-function/routine
        result: Result object to debug
    """
    serialized_print(f"{fn_name}() -> {fn_sub_name}() result",
                     safe_serialize_message(result))


def debug_conditional_edge(fn_name: str, next_node: str, message: Any) -> None:
    """
    Debug print a conditional edge object.

    Args:
        fn_name: Name of the function/routine
        next_node: Name of the next node
        message: Message object to debug
    """
    serialized_print(f"Conditional edge: {fn_name}() -> next_node: {next_node}()",
                     safe_serialize_message(message))
