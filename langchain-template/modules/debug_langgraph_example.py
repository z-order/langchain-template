"""
Example usage of the debug_langgraph module in the context of the memory agent.

This example shows how to replace the existing debug code in the memory agent
with the new debug_langgraph module.
"""

from .debug_langgraph import (
    serialized_print,
    debug_response,
    debug_messages,
    debug_state,
    debug_result,
    set_debug_mode,
    is_debug_enabled
)

# Example: How to use the module in the task_mAIstro function


def task_mAIstro_example():
    """
    Example of how to use the debug_langgraph module in the task_mAIstro function.
    """

    state = {
        "messages": [
            {"role": "human", "content": "Hello, how are you?"},
            {"role": "ai", "content": "I'm good, thank you!"}
        ]
    }

    config = {
        "configurable": {
            "user_id": "123"
        }
    }

    # Enable debug mode (you can also set this via environment variable DEBUG_MESSAGES=true)
    set_debug_mode(True)

    # Get the user ID from the config
    user_id = config["configurable"]["user_id"]

    # Example: Debug print the state
    debug_state("task_mAIstro", state)

    # Example: Debug print messages
    debug_messages("task_mAIstro", state["messages"])

    # Simulate getting a response from the model
    response = {"content": "Hello, how can I help you?", "type": "AIMessage"}

    # Use the prototype function as specified
    serialized_print("task_mAIstro", {
        "response": response
    })

    # Or use the convenience function
    debug_response("task_mAIstro", response)

    return {"messages": [response]}


# Example: How to use in update_todos function
def update_todos_example():
    """
    Example of how to use the debug_langgraph module in the update_todos function.
    """
    # Example: Debug print the result from Trustcall
    result = {
        "responses": [{"task": "Book swim lessons", "status": "not started"}],
        "response_metadata": [{"id": "call_123"}]
    }

    # Use the prototype function
    serialized_print("update_todos", {
        "result": result
    })

    # Or use the convenience function
    debug_result("update_todos", result)

    return {"messages": [{"role": "tool", "content": "updated todos"}]}


# Example: How to check if debug is enabled
def conditional_debug_example():
    """
    Example of how to conditionally use debug logging.
    """
    if is_debug_enabled():
        print("Debug mode is enabled")
        # Do debug-specific operations
    else:
        print("Debug mode is disabled")


# Example: How to use with environment variables
def environment_debug_example():
    """
    Example showing how debug mode can be controlled via environment variables.
    """
    print(f"Debug mode from environment: {is_debug_enabled()}")

    # You can also set it programmatically
    set_debug_mode(True)
    print(f"Debug mode after setting: {is_debug_enabled()}")


if __name__ == "__main__":
    # Run examples
    print("\n\n=== Debug LangGraph Module Examples ===")

    # Example 1: Environment variable control
    print("\n\n1. Environment variable control:")
    environment_debug_example()

    # Example 2: Conditional debug
    print("\n\n2. Conditional debug:")
    conditional_debug_example()

    # Example 3: Basic usage
    print("\n\n3. Basic usage:")
    serialized_print("example_function", {"data": "test value"})

    # Example 4: Convenience functions
    print("\n\n4. Convenience functions:")
    debug_response("example_function", {"content": "test response"})

    # Example 5: Task mAIstro
    print("\n\n5. Task mAIstro:")
    task_mAIstro_example()

    # Example 6: Update todos
    print("\n\n6. Update todos:")
    update_todos_example()

    print("\n\n")
