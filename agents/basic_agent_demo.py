"""
Basic Agent Demo
================
Demonstrates agent with auto function calling.
"""

from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.contents.chat_history import ChatHistory


async def demo_basic_agent(kernel: Kernel):
    """
    Agent with auto function calling chains functions together to achieve a goal.
    Best for: Tasks that require a clear sequence of steps.
    """
    print("=" * 80)
    print("DEMO 1: AGENT WITH AUTO FUNCTION CALLING")
    print("=" * 80)
    print("The Agent uses function calling to create a step-by-step plan to achieve a goal.")
    print("It chains functions together in sequence.\n")

    # Create agent with auto function calling enabled
    agent = ChatCompletionAgent(
        kernel=kernel,
        name="PlannerAgent",
        instructions="You are a helpful assistant that can perform calculations and text operations. Use the available functions to help answer questions."
    )

    # Example 1: Multi-step business calculation
    print("Example 1: Calculate final price after discount and tax")
    print("-" * 60)
    goal = "Calculate the final price if an item costs $100, has a 20% discount, and 8% tax rate"

    print(f"Goal: {goal}\n")
    print("Agent is processing...\n")

    chat_history = ChatHistory()
    chat_history.add_user_message(goal)

    async for message in agent.invoke(chat_history):
        print(f"Final Result: {message.content}\n")

    # Example 2: Text processing chain
    print("\nExample 2: Text transformation chain")
    print("-" * 60)
    goal = "Take the text 'hello world', convert it to uppercase, then count the words"

    print(f"Goal: {goal}\n")
    print("Agent is processing...\n")

    chat_history = ChatHistory()
    chat_history.add_user_message(goal)

    async for message in agent.invoke(chat_history):
        print(f"Final Result: {message.content}\n")
