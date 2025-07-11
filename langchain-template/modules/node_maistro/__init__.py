"""
Node Maistro - LangGraph Workflow Nodes

This package contains the core LangGraph workflow nodes for the Maistro task management chatbot.
These nodes implement the intelligent workflow that processes user interactions, extracts information,
and maintains persistent memory for user profiles, todos, and instructions.

Workflow Overview:
- task_mAIstro: Main conversation node that processes user input and decides what to update
- route_message: Conditional edge router that directs workflow based on update type
- update_todos: Extracts and stores task information using Trustcall
- update_profile: Extracts and stores user profile information using Trustcall
- update_instructions: Updates user preferences for task management

Key Features:
- Intelligent information extraction using Trustcall
- Persistent memory storage with SQLite backend
- Conditional workflow routing based on content analysis
- Debug and logging capabilities for workflow inspection
- Modular node design for easy testing and maintenance
"""

# Import all workflow nodes
from .node_task_mAIstro import task_mAIstro
from .node_update_todos import update_todos
from .node_update_profile import update_profile
from .node_instructions import update_instructions
from .cedge_route_message import route_message

# Main exports
__all__ = [
    'task_mAIstro',
    'update_todos',
    'update_profile',
    'update_instructions',
    'route_message'
]

# Node Descriptions
__node_descriptions__ = {
    'task_mAIstro': {
        'description': 'Main conversation processing node that handles user input and decides what memory to update',
        'purpose': 'Analyzes user messages and determines whether to update user profile, todos, or instructions',
        'inputs': 'MessagesState with user input, RunnableConfig with user settings, BaseStore for memory access',
        'outputs': 'MessagesState with AI response and tool calls for memory updates',
        'key_features': [
            'Loads existing user profile, todos, and instructions from memory',
            'Uses system prompts to guide AI decision making',
            'Generates tool calls to trigger memory updates',
            'Provides personalized responses based on stored information'
        ]
    },

    'route_message': {
        'description': 'Conditional edge router that directs workflow based on the type of memory update needed',
        'purpose': 'Routes the workflow to the appropriate update node based on tool call analysis',
        'inputs': 'MessagesState with tool calls, RunnableConfig, BaseStore',
        'outputs': 'Literal routing decision (END, update_todos, update_profile, update_instructions)',
        'key_features': [
            'Analyzes tool calls to determine update type',
            'Routes to specific update nodes or ends workflow',
            'Provides debug logging for workflow decisions',
            'Handles unknown update types with error handling'
        ]
    },

    'update_todos': {
        'description': 'Task extraction and storage node using Trustcall for intelligent todo management',
        'purpose': 'Extracts task information from conversations and stores it in persistent memory',
        'inputs': 'MessagesState with conversation history, RunnableConfig, BaseStore',
        'outputs': 'MessagesState with tool response confirming todo updates',
        'key_features': [
            'Uses Trustcall extractor with ToDo schema for structured extraction',
            'Supports both new todo creation and existing todo updates',
            'Includes spy monitoring for tool call visibility',
            'Provides detailed update feedback in tool responses',
            'Stores todos with metadata (deadlines, time estimates, solutions)'
        ]
    },

    'update_profile': {
        'description': 'User profile extraction and storage node using Trustcall for profile learning',
        'purpose': 'Extracts personal information about users and maintains persistent profile memory',
        'inputs': 'MessagesState with conversation history, RunnableConfig, BaseStore',
        'outputs': 'MessagesState with tool response confirming profile updates',
        'key_features': [
            'Uses Trustcall extractor with Profile schema for structured extraction',
            'Learns user details (name, location, job, connections, interests)',
            'Supports incremental profile updates',
            'Maintains profile context across conversations',
            'Provides personalized responses based on stored profile'
        ]
    },

    'update_instructions': {
        'description': 'User preference learning node for task management instructions',
        'purpose': 'Learns and updates user preferences for how tasks should be managed',
        'inputs': 'MessagesState with conversation history, RunnableConfig, BaseStore',
        'outputs': 'MessagesState with tool response confirming instruction updates',
        'key_features': [
            'Reflects on conversation history to learn preferences',
            'Updates instructions for future task management',
            'Uses system prompts to guide instruction generation',
            'Overwrites existing instructions with new preferences',
            'Improves task management based on user feedback'
        ]
    }
}

# Workflow Architecture
__workflow_architecture__ = {
    'flow': [
        'START → task_mAIstro → route_message → [update_todos|update_profile|update_instructions] → task_mAIstro',
        'Each update node returns to task_mAIstro for continued conversation'
    ],
    'memory_types': {
        'profile': 'User personal information (name, location, job, connections, interests)',
        'todo': 'Task list with details (task, deadline, time estimate, solutions, status)',
        'instructions': 'User preferences for task management behavior'
    },
    'storage': {
        'backend': 'SQLite via LangGraph checkpoint store',
        'namespacing': 'Organized by (memory_type, todo_category, user_id)',
        'persistence': 'Long-term memory across conversation sessions'
    }
}

# Node Dependencies
__node_dependencies__ = {
    'core': [
        'langgraph - Workflow orchestration',
        'langchain_core - Message handling and runnables',
        'trustcall - Information extraction framework'
    ],
    'models': [
        'maistro_schema - Pydantic models for structured data',
        'maistro_prompt - System prompts and instructions'
    ],
    'utilities': [
        'debug_langgraph - Debug and logging utilities',
        'utils_tool - Tool call extraction helpers',
        'utils_spy - Monitoring and visibility tools'
    ],
    'configuration': [
        'configuration - User and system configuration management',
        'core_instance - Instance registry for dependency injection'
    ]
}

# Usage Examples
__usage_examples__ = {
    'basic_workflow': """
    # The workflow is automatically orchestrated by LangGraph
    from modules.node_maistro import task_mAIstro, route_message, update_todos
    
    # Nodes are connected in the main TaskMaistro class
    builder = StateGraph(MessagesState)
    builder.add_node("task_mAIstro", task_mAIstro)
    builder.add_node("update_todos", update_todos)
    builder.add_conditional_edges("task_mAIstro", route_message)
    """,

    'memory_access': """
    # Each node accesses memory through the store parameter
    def example_node(state, config, store):
        user_id = config["configurable"]["user_id"]
        namespace = ("todo", "general", user_id)
        todos = store.search(namespace)
        # Process todos...
    """,

    'debug_mode': """
    # Enable debug logging for workflow inspection
    from modules import set_debug_mode
    set_debug_mode(True)
    
    # Debug information is automatically logged by each node
    """
}

# Testing and Development
__testing_info__ = {
    'unit_testing': 'Each node can be tested independently with mock state and store',
    'integration_testing': 'Full workflow testing through LangGraph Studio',
    'debug_tools': 'Built-in debug logging for workflow inspection and troubleshooting',
    'development': 'Nodes are designed for easy modification and extension'
}

# Version and Metadata
__version__ = "1.0.0"
__author__ = "HiveMind Development Team by Steve"
__description__ = "LangGraph workflow nodes for Maistro task management chatbot"
