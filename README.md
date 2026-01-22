# Semantic Kernel Agent Demonstrations

**Enterprise AI Training by REDIVAC Technologies**

A comprehensive collection of Semantic Kernel demonstrations showcasing agent-based AI orchestration, function calling, and enterprise integration patterns. Perfect for Fortune 500 training sessions and hands-on workshops.

## 🚀 Overview

This repository demonstrates how to build production-ready AI agents using Microsoft Semantic Kernel. It includes:

- **4 Interactive Jupyter Notebooks** - Step-by-step learning path
- **Modular Plugin Architecture** - Reusable components for different capabilities
- **Agent-Based Orchestration** - Automatic function calling and workflow coordination
- **Real-World Scenarios** - Enterprise use cases like sales order processing
- **ChromaDB Integration** - RAG (Retrieval-Augmented Generation) patterns

## 📚 Project Structure

```
SKPlanners/
├── notebooks/              # Jupyter notebooks for interactive learning
│   ├── 1-basic-agent.ipynb
│   ├── 2-reasoning-agent.ipynb
│   ├── 3-agent-comparison.ipynb
│   ├── 4-enterprise-scenario.ipynb
│   └── 05-semantic-kernel-chromadb.ipynb
├── plugins/                # Reusable plugin modules
│   ├── math_plugin.py
│   ├── text_plugin.py
│   ├── business_plugin.py
│   ├── data_plugin.py
│   ├── prompt_plugin.py
│   ├── weather_info_plugin.py
│   └── destinations_plugin.py
├── agents/                 # Agent demonstration modules
│   ├── basic_agent_demo.py
│   ├── reasoning_agent_demo.py
│   ├── agent_comparison_demo.py
│   └── enterprise_agent_demo.py
├── utils/                  # Utility functions
│   └── kernel_setup.py
├── main.py                 # Main demo runner
├── .env                    # Environment configuration
└── requirements.txt        # Python dependencies
```

## 🔧 Setup

### Prerequisites

- Python 3.12+
- Azure OpenAI access
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SKPlanners
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   
   # Windows
   .\env\Scripts\activate
   
   # Linux/Mac
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
   AZURE_OPENAI_API_KEY=your-api-key
   AZURE_OPENAI_API_VERSION=2024-05-01-preview
   ```

## 🎯 Quick Start

### Run All Demos

```bash
python main.py
```

### Run Jupyter Notebooks

```bash
jupyter notebook notebooks/
```

Then open any notebook:
- `1-basic-agent.ipynb` - Start here for basic concepts
- `2-reasoning-agent.ipynb` - Complex reasoning patterns
- `3-agent-comparison.ipynb` - Compare different agent behaviors
- `4-enterprise-scenario.ipynb` - Real-world business use case
- `05-semantic-kernel-chromadb.ipynb` - RAG with ChromaDB

## 📖 Learning Path

### 1. Basic Agent (Demo 1)
Learn how agents automatically orchestrate function calls to solve tasks.

**Concepts:**
- Auto function calling
- Plugin integration
- Sequential execution

### 2. Reasoning Agent (Demo 2)
Explore complex problem-solving with adaptive decision-making.

**Concepts:**
- Dynamic reasoning
- Multi-step coordination
- Intermediate result handling

### 3. Agent Comparison (Demo 3)
Compare how different instructions affect agent behavior.

**Concepts:**
- Instruction engineering
- Behavior customization
- Output optimization

### 4. Enterprise Scenario (Demo 4)
Build a real-world sales order processing system.

**Concepts:**
- Business workflow automation
- Multi-plugin orchestration
- Production patterns

### 5. RAG with ChromaDB (Demo 5)
Implement Retrieval-Augmented Generation for context-aware responses.

**Concepts:**
- Vector database integration
- Semantic search
- Context retrieval

## 🔌 Plugins

### Core Plugins

- **MathPlugin** - Basic arithmetic operations
- **TextPlugin** - Text manipulation and processing
- **BusinessPlugin** - Business calculations (discounts, taxes, margins)
- **DataPlugin** - Data transformation and formatting

### Advanced Plugins

- **PromptPlugin** - RAG operations with ChromaDB
- **WeatherInfoPlugin** - Travel destination temperature data
- **DestinationsPlugin** - Detailed travel destination information

## 🏢 Enterprise Use Cases

This framework supports various enterprise scenarios:

- **Customer Service** - Automated support with context retrieval
- **Sales Processing** - Order calculations and pricing
- **Data Analysis** - Automated insights and reporting
- **Document Processing** - RAG-based document Q&A
- **Workflow Automation** - Multi-step business processes

## 🛠️ Development

### Adding a New Plugin

1. Create plugin file in `plugins/`
2. Define class with `@kernel_function` decorators
3. Add to `plugins/__init__.py`
4. Import in your demo or notebook

Example:
```python
from semantic_kernel.functions import kernel_function

class MyPlugin:
    @kernel_function(
        name="my_function",
        description="Description for the AI"
    )
    def my_function(self, param: str) -> str:
        return f"Processed: {param}"
```

### Creating a New Agent Demo

1. Create module in `agents/`
2. Define async function that accepts `Kernel`
3. Create `ChatCompletionAgent` with instructions
4. Add to `agents/__init__.py`

## 📊 Training Sessions

**Recommended for:**
- 16-40 hour enterprise training programs
- Hands-on AI/ML workshops
- Fortune 500 technical training
- Developer upskilling programs

**Topics Covered:**
1. Plugin Architecture (2-3 hours)
2. Agent-Based Orchestration (3-4 hours)
3. Complex Reasoning (4-5 hours)
4. Enterprise Integration (6-8 hours)
5. Advanced Topics (remaining time)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Ramkumar JD**  
REDIVAC Technologies

## 🔗 Resources

- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [ChromaDB Documentation](https://docs.trychroma.com/)

## 📝 Notes

- This demo uses Semantic Kernel v1.36.0+
- The planner classes (SequentialPlanner, StepwisePlanner) have been deprecated in favor of agent-based architecture
- All demos use Azure OpenAI, but can be adapted for OpenAI API

## 🐛 Troubleshooting

### Common Issues

**ImportError: No module named 'utils'**
- Ensure you're in the project root directory
- Check that `sys.path` includes parent directory (notebooks handle this automatically)

**Connection Error to Azure OpenAI**
- Verify your `.env` file has correct credentials
- Check API version compatibility
- Ensure endpoint URL is correct

**SQLite Version Error (ChromaDB)**
- Install pysqlite3-binary: `pip install pysqlite3-binary`
- See notebook for workaround code

---

**Happy Learning! 🎓**
