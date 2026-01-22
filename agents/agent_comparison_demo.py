"""
Agent Comparison Demo
=====================
Compares different agent instructions for the same task.
"""

from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.contents.chat_history import ChatHistory


async def demo_agent_comparison(kernel: Kernel):
    """
    Compare how different agent instructions handle the same complex task
    """
    print("\n" + "=" * 80)
    print("DEMO 3: AGENT COMPARISON")
    print("=" * 80)
    print("Same complex task executed by agents with different instructions.\n")

    task = """
    Calculate the profit margin for a product that costs $80 to make,
    sells for $120 after a 10% discount, and format the result as a percentage.
    """

    print(f"Task: {task.strip()}\n")

    # Using Direct Agent
    print("Approach 1: Direct Agent")
    print("-" * 60)
    agent1 = ChatCompletionAgent(
        kernel=kernel,
        name="DirectAgent",
        instructions="Use the available functions to solve the problem directly and efficiently."
    )

    chat_history = ChatHistory()
    chat_history.add_user_message(task)
    async for message in agent1.invoke(chat_history):
        print(f"Result: {message.content}\n")

    # Using Detailed Agent
    print("\nApproach 2: Detailed Reasoning Agent")
    print("-" * 60)
    agent2 = ChatCompletionAgent(
        kernel=kernel,
        name="DetailedAgent",
        instructions="Break down the problem into steps, explain your reasoning, and use the available functions to compute the answer."
    )

    chat_history = ChatHistory()
    chat_history.add_user_message(task)
    async for message in agent2.invoke(chat_history):
        print(f"Result: {message.content}\n")
