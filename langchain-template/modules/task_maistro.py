from trustcall import create_extractor
from langchain_openai import ChatOpenAI
from langchain_core.runnables import Runnable
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.graph.state import CompiledStateGraph
from .core_instance import register_instance, get_instance
from .debug_langgraph import set_debug_mode
from . import configuration
from .node_maistro.cedge_route_message import route_message
from .node_maistro.node_task_mAIstro import task_mAIstro
from .node_maistro.node_update_todos import update_todos
from .node_maistro.node_update_profile import update_profile
from .node_maistro.node_instructions import update_instructions
from .maistro_abstract import AbstractMaistro
from .maistro_schema import Profile


# Task Maistro class
class TaskMaistro(AbstractMaistro):
    """Task Maistro"""

    # In Python, a single underscore prefix (e.g., _model) is a convention for a "protected" property,
    # while a double underscore prefix (e.g., __model) is for "private" name-mangled properties.
    # The following are "protected" by convention, not truly private:
    _model: ChatOpenAI
    _profile_extractor: Runnable
    _graph: CompiledStateGraph
    _enable_debug: bool = True

    def __init__(self, model: str, temperature: float = 0):
        # Initialize the model
        self._model = ChatOpenAI(model=model, temperature=temperature)
        # Create the Trustcall extractors for updating the user profile and ToDo list
        self._profile_extractor = create_extractor(
            self._model,
            tools=[Profile],
            tool_choice="Profile",
        )

        # Enable debug mode
        set_debug_mode(self._enable_debug)

        # Create the graph + all nodes
        builder = StateGraph(
            MessagesState, config_schema=configuration.Configuration)

        # Define the flow of the memory extraction process
        builder.add_node(task_mAIstro)
        builder.add_node(update_todos)
        builder.add_node(update_profile)
        builder.add_node(update_instructions)

        # Define the flow
        builder.add_edge(START, "task_mAIstro")
        builder.add_conditional_edges("task_mAIstro", route_message)
        builder.add_edge("update_todos", "task_mAIstro")
        builder.add_edge("update_profile", "task_mAIstro")
        builder.add_edge("update_instructions", "task_mAIstro")

        # Compile the graph
        self._graph = builder.compile()

    @property
    def graph(self):
        return self._graph

    @property
    def model(self):
        return self._model

    @property
    def profile_extractor(self):
        return self._profile_extractor


# Register the instance
register_instance("task_maistro", TaskMaistro(model="gpt-4o", temperature=0))

# Get the instance
task_maistro = get_instance("task_maistro")
graph = task_maistro.graph
model = task_maistro.model
