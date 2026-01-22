"""
Reasoning Agent Demo
====================
Demonstrates agent with complex reasoning capabilities.
"""

from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.contents.chat_history import ChatHistory


async def demo_reasoning_agent(kernel: Kernel):
    """
    Agent uses function calling to dynamically determine next steps.
    Best for: Complex problems requiring adaptive decision-making.
    """
    print("\n" + "=" * 80)
    print("DEMO 2: AGENT WITH COMPLEX REASONING")
    print("=" * 80)
    print("The Agent dynamically determines each next step.")
    print("It can adapt based on intermediate results.\n")

    agent = ChatCompletionAgent(
        kernel=kernel,
        name="ReasoningAgent",
        instructions="You are a helpful assistant that solves complex problems step by step. Use the available functions to perform calculations and data processing. Explain your reasoning as you work."
    )

    # Example 1: Complex business scenario
    print("Example 1: Multi-step business calculation with formatting")
    print("-" * 60)
    question = """
    A product costs $150. Apply a 25% discount, then calculate 10% tax on the discounted price.
    Finally, format the result as currency.
    """

    print(f"Question: {question.strip()}\n")
    print("Agent is working...\n")

    chat_history = ChatHistory()
    chat_history.add_user_message(question)

    response_chunks = []
    async for chunk in agent.invoke_stream(messages=chat_history):
        if chunk.content:
            response_chunks.append(chunk.content.content)
            print(chunk.content, end="", flush=True)
    
    print("\n")
    full_response = "".join(response_chunks)

    # Example 2: Data analysis scenario
    print("\nExample 2: Calculate average and format")
    print("-" * 60)
    question = "What is the average of these numbers: 10, 20, 30, 40, 50? Format it as currency."

    print(f"Question: {question}\n")
    print("Agent is working...\n")

    chat_history = ChatHistory()
    chat_history.add_user_message(question)

    response_chunks = []
    async for chunk in agent.invoke_stream(messages=chat_history):
        if chunk.content:
            response_chunks.append(chunk.content.content)
            print(chunk.content, end="", flush=True)
    
    print("\n")
    full_response = "".join(response_chunks)
