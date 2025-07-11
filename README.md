# LangGraph Learning Projects

This repository contains three comprehensive LangGraph projects designed to help you learn and master LangGraph concepts, from basic understanding to advanced deployment.

## 📚 Project Overview

### 1. **coursera-ai-agents-langgraph** - Intuition & Insight Learning

**Course Link:** [https://www.coursera.org/learn/ai-agents-in-langgraph](https://www.coursera.org/learn/ai-agents-in-langgraph)

This project focuses on understanding the intuition and insights behind LangGraph. It's designed to help you grasp the fundamental concepts and thought processes that make LangGraph powerful for building AI agents.

**Contents:**

- Lesson 1: Build an Agent from Scratch
- Lesson 2: LangGraph Components
- Lesson 3: Agentic Search Tools
- Lesson 4: Persistence and Streaming
- Lesson 5: Human in the Loop
- Lesson 6: Essay Writer

### 2. **langchain-academy** - Step-by-Step Detailed Learning

**Course Link:** [https://academy.langchain.com/courses/intro-to-langgraph](https://academy.langchain.com/courses/intro-to-langgraph)  
**Source Code:** [https://github.com/langchain-ai/langchain-academy.git](https://github.com/langchain-ai/langchain-academy.git)

This is the official LangChain Academy course that provides comprehensive, step-by-step lessons covering all aspects of LangGraph development.

**Contents:**

- Module 0: Basic Setup
- Module 1: Simple Graphs, Chains, Routers, Agents, Memory, Deployment
- Module 2: State Schema, State Reducers, Multiple Schemas, Message Filtering
- Module 3: Streaming, Interruption, Breakpoints, Human Feedback, Time Travel
- Module 4: Parallelization, Sub-graphs, Map-Reduce, Research Assistant
- Module 5: Memory Store, Memory Schema, Memory Agents
- Module 6: Creating, Connecting, Double Texting, Assistant

### 3. **langchain-template** - Real-World Project Template

**Created by:** Steve from HiveMind  
**Template README:** [langchain-template/README.md](langchain-template/README.md)  
**Deployment Guide (Very Important):** [langchain-template/deployment/langgraph.ipynb](langchain-template/deployment/langgraph.ipynb)

This is a production-ready template for building realistic, useful LangGraph applications with comprehensive development, deployment, and hosting solutions. The template implements a **Task Maistro** - an intelligent task management system that can understand user requests, extract tasks, update user profiles, and manage ToDo lists through natural language interaction.

**Core Features:**

- **Task Maistro System**: Intelligent task extraction and management
- **User Profile Management**: Dynamic profile updates based on conversations
- **ToDo List Integration**: Automatic task creation and management
- **Memory Persistence**: State management across conversations
- **Modular Architecture**: Reusable components and nodes
- **Production Deployment**: Docker, Redis, PostgreSQL stack
- **Debug & Monitoring**: Comprehensive logging and tracing
- **LangGraph Development Server**: Local development with hot reloading
- **Container Deployment**: Production-ready Docker containers
- **SDK Integration**: Client-side interaction via langgraph_sdk

**Key Components:**

- `TaskMaistro` class: Main application orchestrator
- `AbstractMaistro`: Base class for extensible Maistro systems
- Node system: Modular processing nodes for different tasks
- Trustcall integration: Structured data extraction
- LangGraph Studio integration: Visual development and testing
- `core_instance.py`: Custom module management by Steve (HiveMind)

## 🧠 Core Concepts

### LangChain

LangChain is a framework for developing applications powered by language models. It provides:

- **Components**: Modular building blocks for LLM applications
- **Chains**: Sequences of components for complex workflows
- **Agents**: Autonomous systems that can use tools and make decisions
- **Memory**: Systems for storing and retrieving conversation history
- **Tools**: External integrations for web search, databases, APIs, etc.

### LangGraph

LangGraph is a library for building stateful, multi-actor applications with LLMs. Key features:

- **State Management**: Persistent state across conversation turns
- **Multi-Actor Systems**: Multiple agents working together
- **Conditional Logic**: Dynamic routing based on state and context
- **Streaming**: Real-time responses and updates
- **Human-in-the-Loop**: Interactive systems with human feedback
- **Parallelization**: Concurrent execution of multiple tasks

### LangSmith

LangSmith is a developer platform for debugging, testing, evaluating, and monitoring LLM applications:

- **Tracing**: Track the execution of your LLM chains and agents
- **Debugging**: Inspect intermediate steps and variables
- **Testing**: Create and run test suites for your applications
- **Evaluation**: Measure performance and quality of your systems
- **Monitoring**: Production monitoring and alerting

## 🚀 Setup Instructions

### Prerequisites

- Python 3.11+ (required for optimal LangGraph compatibility)
- Git
- Docker (for template deployment)
- VS Code with Dev Containers extension (recommended for development)

## 🐳 VS Code Development Containers

This repository includes VS Code development container configurations for consistent development environments across different platforms. The `.devcontainer` directories provide isolated, reproducible development environments with all necessary dependencies pre-installed.

### Development Container Features

**Available in:**

- `langchain-academy/.devcontainer/` - For LangChain Academy modules
- `langchain-template/.devcontainer/` - For the production template

**Container Configuration:**

```json
{
  "name": "Python 3",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.11-bookworm",
  "postCreateCommand": "pip install jupyterlab && pip3 install --user -r requirements.txt"
}
```

**What's Included:**

- **Python 3.11**: Optimized for LangGraph compatibility
- **JupyterLab**: Pre-installed for notebook development
- **Dependencies**: All project requirements automatically installed
- **Isolated Environment**: Clean, reproducible development setup
- **Cross-Platform**: Works on Windows, macOS, and Linux

### Setting Up Development Containers

#### 1. Install VS Code Extensions

```bash
# Install the Dev Containers extension
code --install-extension ms-vscode-remote.remote-containers
```

#### 2. Open Project in Container

**Using VS Code GUI (Recommended):**

1. **Open VS Code** and navigate to your project folder
2. **Click the bottom-left corner icon** `><` (Remote Development indicator)
3. **Select "Reopen in Container"** from the popup menu
4. **Wait for container build** - VS Code will automatically:
   - Download the Python 3.11 container image
   - Install all dependencies from `requirements.txt`
   - Set up JupyterLab
   - Configure the development environment

**Alternative Methods:**

- **Command Palette**: `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
- **Status Bar**: Click the remote indicator in the bottom-left corner
- **Welcome Screen**: "Open Folder in Container" option

#### 3. Container-Specific Setup

**For LangChain Academy:**

```bash
# Container automatically installs:
# - Python 3.11
# - JupyterLab
# - All requirements from requirements.txt

# Start Jupyter
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Or just use Jupyter Notebook
jupyter notebook

# Access Jupyter at: http://localhost:8888
```

**For LangChain Template:**

```bash
# Container includes:
# - Python 3.11
# - JupyterLab
# - All template dependencies

# Set up environment variables
cp .env.local.sh.sample .env.local.sh
# Edit .env.local.sh with your API keys

# Start development
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Or just use Jupyter Notebook
jupyter notebook

# Access Jupyter at: http://localhost:8888
```

### Port Forwarding

The development containers automatically forward these ports:

- **8888**: JupyterLab
- **8123**: LangGraph Development Server (when running)
- **2024**: LangGraph Studio (when running)

### Environment Variables in Containers

**Setting API Keys:**

```bash
# Inside the container, create .env file
echo "OPENAI_API_KEY=your_key_here" > .env
echo "LANGCHAIN_API_KEY=your_key_here" >> .env
echo "LANGCHAIN_TRACING_V2=true" >> .env
echo "TAVILY_API_KEY=your_key_here" >> .env

# Or use the template's environment setup
source .env.local.sh
```

### Container Management

**Rebuilding Containers:**

```bash
# If you modify devcontainer.json
# 1. Command Palette: "Dev Containers: Rebuild Container"
# 2. Or: "Dev Containers: Rebuild and Reopen in Container"
```

**Accessing Container Terminal:**

```bash
# In VS Code:
# Terminal > New Terminal (automatically opens in container)

# Or use integrated terminal:
# View > Terminal
```

### Benefits of Development Containers

1. **Consistency**: Same environment across all developers
2. **Isolation**: No conflicts with local Python installations
3. **Reproducibility**: Exact same setup every time
4. **Cross-Platform**: Works identically on any OS
5. **Pre-configured**: All dependencies and tools ready to use
6. **Version Control**: Container configs are versioned with code

### Troubleshooting Containers

**Container Won't Start:**

```bash
# Check Docker is running
docker --version

# Check VS Code Dev Containers extension
code --list-extensions | grep remote-containers
```

**Port Conflicts:**

```bash
# Check if ports are in use
lsof -i :8888
lsof -i :8123

# Modify devcontainer.json to use different ports
"forwardPorts": [8889, 8124]
```

**Permission Issues:**

```bash
# If you need root access, uncomment in devcontainer.json:
"remoteUser": "root"
```

### Environment Setup

#### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd langchain
```

#### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv langgraph-env

# Activate on Mac/Linux
source langgraph-env/bin/activate

# Activate on Windows PowerShell
langgraph-env\scripts\activate
```

#### 3. Environment Variables Setup

Create a `.env` file in each project directory with the following variables:

**Required API Keys:**

```bash
# OpenAI API Key (required for all projects)
OPENAI_API_KEY=your_openai_api_key_here

# LangSmith API Key (required for tracing and debugging)
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_TRACING_V2=true

# Tavily API Key (required for web search functionality)
TAVILY_API_KEY=your_tavily_api_key_here
```

**Optional Configuration:**

```bash
# OpenAI Base URL (if using custom endpoint)
OPENAI_BASE_URL=https://api.openai.com/v1

# LangSmith Project (for organizing traces)
LANGCHAIN_PROJECT=your_project_name
```

#### 4. API Key Setup Instructions

**OpenAI API Key:**

1. Sign up at [https://openai.com/index/openai-api/](https://openai.com/index/openai-api/)
2. Create an API key in your dashboard
3. Set `OPENAI_API_KEY` in your environment

**LangSmith API Key:**

1. Sign up at [https://smith.langchain.com/](https://smith.langchain.com/)
2. Create an API key in your dashboard
3. Set `LANGCHAIN_API_KEY` and `LANGCHAIN_TRACING_V2=true`

**Tavily API Key:**

1. Sign up at [https://tavily.com/](https://tavily.com/)
2. Create an API key (generous free tier available)
3. Set `TAVILY_API_KEY` in your environment

## 📖 Project-Specific Setup

### 1. Coursera AI Agents in LangGraph

```bash
cd coursera-ai-agents-langgraph

# Install dependencies
pip install -r requirements.txt

# For conda users (alternative setup)
conda create -n langgraph python=3.11
conda activate langgraph
pip install -r requirements-conda.txt
conda install -c conda-forge pygraphviz
```

**System Dependencies (Ubuntu/Debian):**

```bash
sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
```

**Running Notebooks:**

```bash
jupyter notebook
```

**Available Lessons:**

- `Lesson_1_Student (Build an Agent from Scratch)/` - Basic agent construction
- `Lesson_2_Student (LangGraph Components)/` - Core LangGraph components
- `Lesson_3_Student (Agentic Search Tools)/` - Web search integration
- `Lesson_4_Student (Persistence and Streaming)/` - State management and streaming
- `Lesson_5_Student (Human in the loop)/` - Interactive systems
- `Lesson_6_Student (Essay Writer)/` - Complete application example

### 2. LangChain Academy

```bash
cd langchain-academy

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

**Module Structure:**

- **Module 0:** Basic setup and environment configuration
- **Module 1:** Simple graphs, chains, routers, agents, memory, deployment
- **Module 2:** State schema, reducers, multiple schemas, message filtering
- **Module 3:** Streaming, interruption, breakpoints, human feedback
- **Module 4:** Parallelization, sub-graphs, map-reduce, research assistant
- **Module 5:** Memory store, memory schema, memory agents
- **Module 6:** Creating, connecting, double texting, assistant

**LangGraph Studio Setup:**
Each module contains a `studio/` directory with LangGraph Studio configurations.

```bash
# Navigate to any module's studio directory
cd module-1/studio

# Start LangGraph Studio
langgraph dev
```

Studio will be available at:

- API: http://127.0.0.1:2024
- UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- Docs: http://127.0.0.1:2024/docs

**Studio Environment Setup:**

```bash
# Create .env files for all modules
for i in {1..6}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```

**Node.js Client (Module 6):**
Module 6 includes a Node.js client for interacting with LangGraph applications.

```bash
cd module-6/nodejs-client

# Install dependencies using pnpm
pnpm install

# Run the Node.js client
node nodejs-client.js
```

**Node.js Client Features:**

- **Multi-threaded Interaction**: Demonstrates concurrent task processing
- **LangGraph SDK Integration**: Uses `@langchain/langgraph-sdk` for API communication
- **Task Management**: Interacts with the Task Maistro system
- **Configurable User Context**: Supports user-specific configurations
- **Streaming Support**: Handles real-time responses from LangGraph

**Client Configuration:**

```javascript
// Connect to LangGraph server
const client = new Client({ apiUrl: "http://localhost:8123" });

// Create thread for persistent state
const thread = await client.threads.create();

// Configure user context
const config = { configurable: { user_id: "Test-Double-Texting-JS" } };

// Submit tasks to Task Maistro
const run = await client.runs.create(thread.thread_id, "task_maistro", {
  input: { messages: [{ role: "user", content: "Add a ToDo to follow-up with DI Repairs." }] },
  config,
  multitaskStrategy: "enqueue",
  onCompletion: "continue",
  onDisconnect: "continue",
});
```

**Prerequisites:**

- Node.js 18+ with ES modules support
- pnpm package manager
- Running LangGraph server (see deployment instructions)

### 3. LangChain Template

```bash
cd langchain-template

# Install dependencies
pip install -r requirements.txt

# Copy the .env.local.sh.sample file to .env.local.sh and set your API keys here
cp .env.local.sh.sample .env.local.sh

# Set the environment variables
source .env.local.sh

# Run the main testing notebook
jupyter notebook 1.module-testing.ipynb
```

**Project Structure:**

```
langchain-template/
├── modules/                    # Core application modules
│   ├── node_maistro/          # LangGraph nodes for task processing
│   ├── task_maistro.py        # Main TaskMaistro application class
│   ├── core_instance.py       # Instance management and registration
│   ├── maistro_abstract.py    # Abstract base class for Maistro systems
│   ├── maistro_schema.py      # Data schemas for profiles and tasks
│   ├── maistro_prompt.py      # Prompt templates and configurations
│   ├── configuration.py       # Configuration settings
│   ├── debug_langgraph.py     # Debug utilities and logging
│   └── utils_tool.py          # Utility functions and tools
├── deployment/                # Deployment configurations
│   ├── docker-compose.yml     # Full stack with Redis, PostgreSQL, API
│   ├── langgraph.json         # LangGraph deployment configuration
│   ├── langgraph-build.sh     # Build script for deployment
│   └── requirements.txt       # Deployment dependencies
└── 1.module-testing.ipynb     # Interactive testing and development
```

**Task Maistro System:**
The template implements an intelligent task management system that:

- Extracts tasks from natural language input
- Manages user profiles and preferences
- Creates and updates ToDo lists
- Maintains conversation context and memory
- Provides structured data extraction using Trustcall

**Local Development:**

```bash
# Run the testing notebook to interact with Task Maistro
jupyter notebook 1.module-testing.ipynb

# Example interaction:
# "Add a ToDo to finish booking travel to Hong Kong by end of next week"
# The system will extract the task, create a structured ToDo item,
# and update the user's task list with deadlines and suggested solutions
```

**LangGraph Development Mode in Local:**

```bash
# Set up environment variables
cd langchain-template
source .env.local.sh

# Start development server (custom port)
cd deployment
langgraph dev --port 8123 --config langgraph-development.json

# Or use default settings
langgraph dev
```

**Container Deployment:**

```bash
cd deployment

# Configure API Keys in docker-compose.yml BEFORE building
# Edit the environment section in docker-compose.yml:
```

**API Key Configuration in Docker:**

```yaml
# In langchain-template/deployment/docker-compose.yml
services:
  langgraph-api:
    environment:
      OPENAI_API_KEY: "your_openai_api_key_here"
      LANGSMITH_API_KEY: "your_langsmith_api_key_here"
      # Other environment variables are pre-configured
```

**Setting Up API Keys (Required Before Build):**

```bash
# Method 1: Edit docker-compose.yml directly
cd langchain-template/deployment
vim docker-compose.yml
# Replace the placeholder values with your actual API keys

# Method 2: Use environment variables (recommended for production)
export OPENAI_API_KEY="your_openai_api_key_here"
export LANGSMITH_API_KEY="your_langsmith_api_key_here"
```

**Production Security Best Practices:**

```bash
# Create a .env file for Docker Compose
cd langchain-template/deployment
cat > .env << EOF
OPENAI_API_KEY=your_openai_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
POSTGRES_PASSWORD=your_secure_postgres_password
EOF

# Update docker-compose.yml to use .env file
# Add this to the langgraph-api service:
environment:
  OPENAI_API_KEY: ${OPENAI_API_KEY}
  LANGSMITH_API_KEY: ${LANGSMITH_API_KEY}
  POSTGRES_URI: postgres://postgres:${POSTGRES_PASSWORD}@langgraph-postgres:5432/postgres?sslmode=disable
```

```bash
# NOW build the deployment container (after API keys are configured)
./langgraph-build.sh
# This script:
# 1. Copies modules to deployment directory
# 2. Builds container with langgraph build
# 3. Cleans up temporary files

# Or build manually
cp -r ../modules .
langgraph build -t langgraph-api-server --config langgraph-deployment.json
rm -rf modules

# Run the full production stack
docker compose up -d
# This starts:
# - Redis (for caching and session management)
# - PostgreSQL (for persistent data storage)
# - LangGraph API server (for serving the Task Maistro system)

# Access the API at http://localhost:8123
# Access the Docs at http://localhost:8123/docs
# Access the LangGraph Studio at https://smith.langchain.com/studio/?baseUrl=http://localhost:8123
```

**Client Integration:**

```python
from langgraph_sdk import get_client
from langchain_core.messages import HumanMessage

# Connect to the deployed system
client = get_client(url="http://localhost:8123")

# Create a thread and interact
thread = await client.threads.create()
config = {"configurable": {"user_id": "Test"}}

# Stream responses from the Task Maistro system
async for chunk in client.runs.stream(
    thread["thread_id"],
    "task_maistro",
    input={"messages": [HumanMessage(content="Add a ToDo to call parents")]},
    config=config,
    stream_mode="values"
):
    if chunk.event == "values":
        print(chunk.data['messages'][-1])
```

**Production Features:**

- **Scalable Architecture**: Redis for caching, PostgreSQL for persistence
- **API Integration**: RESTful API for external system integration
- **Monitoring**: Built-in logging and debugging capabilities
- **Extensible Design**: Modular node system for easy customization
- **Cloud Ready**: Docker configurations for AWS, GCP, Azure deployment
- **Development Workflow**: Hot reloading with LangGraph development server
- **State Management**: Persistent checkpoints and recovery mechanisms

## 🔧 Common Issues and Solutions

### Python Version Issues

- **Problem:** LangGraph requires Python 3.11+
- **Solution:** Upgrade Python or use conda to create a 3.11 environment

### Graphviz Installation Issues

- **Problem:** `pygraphviz` installation fails
- **Solution:** Install system dependencies first:

  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config

  # macOS
  brew install graphviz

  # Windows
  # Download from https://graphviz.org/download/
  ```

### API Key Issues

- **Problem:** API calls failing
- **Solution:** Verify environment variables are set correctly:
  ```bash
  echo $OPENAI_API_KEY
  echo $LANGCHAIN_API_KEY
  echo $TAVILY_API_KEY
  ```

### LangGraph Studio Issues

- **Problem:** Studio not starting
- **Solution:** Check if `langgraph-cli` is installed:
  ```bash
  pip install "langgraph-cli[inmem]"
  ```

## 📚 Learning Path Recommendation

1. **Start with Coursera** - Get intuition and insights
2. **Move to LangChain Academy** - Learn detailed concepts
3. **Apply with Template** - Build real-world applications

## 🤝 Contributing

This repository contains educational materials and templates. For contributions:

- Follow the existing code style
- Add comprehensive documentation
- Include tests for new features
- Update this README for significant changes

## 📄 License

This project contains materials from multiple sources:

- Coursera course materials (follow Coursera's terms)
- LangChain Academy materials (follow LangChain's license)
- Custom template by Steve from HiveMind

## 🆘 Support

- **Coursera Course Issues:** Contact the course instructors
- **LangChain Academy Issues:** Check the [official repository](https://github.com/langchain-ai/langchain-academy.git)
- **Template Issues:** Contact Steve from HiveMind
- **General LangGraph Questions:** Check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/)

---

**Happy Learning! 🚀**
