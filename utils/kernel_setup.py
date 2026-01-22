"""
Kernel Configuration Utilities
================================
Setup and configuration for Semantic Kernel.
"""

import os
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from plugins import MathPlugin, TextPlugin, BusinessPlugin, DataPlugin


async def setup_kernel():
    """Initialize the Semantic Kernel with Azure OpenAI"""

    # Load environment variables from .env file
    load_dotenv()

    kernel = Kernel()

    # Add Azure OpenAI Chat Completion Service
    deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-4o")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")

    chat_service = AzureChatCompletion(
        deployment_name=deployment_name,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
        service_id="chat"
    )

    kernel.add_service(chat_service)

    # Register all plugins
    kernel.add_plugin(MathPlugin(), plugin_name="MathPlugin")
    kernel.add_plugin(TextPlugin(), plugin_name="TextPlugin")
    kernel.add_plugin(BusinessPlugin(), plugin_name="BusinessPlugin")
    kernel.add_plugin(DataPlugin(), plugin_name="DataPlugin")

    print("✓ Kernel initialized with 4 plugins")
    print("  - MathPlugin (add, multiply, subtract)")
    print("  - TextPlugin (uppercase, count_words, reverse_text)")
    print("  - BusinessPlugin (calculate_discount, calculate_tax, calculate_profit_margin)")
    print("  - DataPlugin (format_currency, calculate_average, concatenate)")
    print()

    return kernel
