"""
Maistro Chatbot Modules

This package contains the core modules for the Maistro task management chatbot system.
The system is built on LangGraph and provides intelligent task management with memory persistence.

Main Components:
- TaskMaistro: The main chatbot class that orchestrates task management
- Core instance registry for dependency injection
- Node-based workflow system for processing user interactions
- Memory management for user profiles, todos, and instructions
- Schema definitions for structured data handling

Key Features:
- Long-term memory for user profiles and task history
- Intelligent task extraction and management
- Configurable workflow nodes
- Debug and logging capabilities
- Modular architecture with clear separation of concerns
"""

# Core Classes and Instances
from .task_maistro import TaskMaistro, task_maistro, graph, model
from .maistro_abstract import AbstractMaistro
from .core_instance import (
    InstanceRegistry,
    register_instance,
    get_instance,
    has_instance,
    safe_get_instance
)

# Schema Definitions
from .maistro_schema import Profile, ToDo, UpdateMemory

# Configuration
from .configuration import Configuration

# Prompts
from .maistro_prompt import (
    MODEL_SYSTEM_MESSAGE,
    TRUSTCALL_INSTRUCTION,
    CREATE_INSTRUCTIONS
)

# Utility Functions
from .utils_tool import extract_tool_info
from .utils_spy import Spy

# Debug and Development
from .debug_langgraph import set_debug_mode

# Node Components (from node_maistro subpackage)
from .node_maistro.node_task_mAIstro import task_mAIstro
from .node_maistro.node_update_todos import update_todos
from .node_maistro.node_update_profile import update_profile
from .node_maistro.node_instructions import update_instructions
from .node_maistro.cedge_route_message import route_message

__all__ = [
    # Main Classes
    'TaskMaistro',
    'AbstractMaistro',

    # Instances
    'task_maistro',
    'graph',
    'model',

    # Core Registry
    'InstanceRegistry',
    'register_instance',
    'get_instance',
    'has_instance',
    'safe_get_instance',

    # Schemas
    'Profile',
    'ToDo',
    'UpdateMemory',

    # Configuration
    'Configuration',

    # Prompts
    'MODEL_SYSTEM_MESSAGE',
    'TRUSTCALL_INSTRUCTION',
    'CREATE_INSTRUCTIONS',

    # Utilities
    'extract_tool_info',
    'Spy',

    # Debug
    'set_debug_mode',

    # Nodes
    'task_mAIstro',
    'update_todos',
    'update_profile',
    'update_instructions',
    'route_message',
]

# Module Descriptions
__module_descriptions__ = {
    'task_maistro': 'Main TaskMaistro class that orchestrates the chatbot workflow',
    'maistro_abstract': 'Abstract base classes defining the Maistro interface',
    'core_instance': 'Instance registry for dependency injection and service management',
    'maistro_schema': 'Pydantic models for structured data (Profile, ToDo, UpdateMemory)',
    'configuration': 'Configuration management for customizable chatbot behavior',
    'maistro_prompt': 'System prompts and instructions for the chatbot',
    'utils_tool': 'Utility functions for extracting information from tool calls',
    'utils_spy': 'Debug utilities for function monitoring',
    'debug_langgraph': 'Debug utilities for LangGraph workflow inspection',
    'debug_langgraph_example': 'Example debug implementations',
    'node_maistro': 'LangGraph nodes for processing user interactions and updating memory',
}

# Quick Start Guide
__quick_start__ = """
Quick Start:
    from modules import task_maistro, graph
    
    # Use the pre-configured instance
    response = graph.invoke({"messages": [user_message]})
    
    # Or create a custom instance
    from modules import TaskMaistro
    custom_maistro = TaskMaistro(model="gpt-4o", temperature=0)
    response = custom_maistro.graph.invoke({"messages": [user_message]})
"""

# Version and Metadata
__version__ = "1.0.0"
__author__ = "HiveMind Development Team by Steve"
__description__ = "Intelligent task management chatbot with memory persistence"
