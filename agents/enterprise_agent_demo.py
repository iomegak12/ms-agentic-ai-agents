"""
Enterprise Agent Demo
=====================
Real-world enterprise scenario for sales order processing.
"""

from semantic_kernel import Kernel
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.contents.chat_history import ChatHistory


async def demo_enterprise_scenario(kernel: Kernel):
    """
    Realistic enterprise use case: Sales order processing
    """
    print("\n" + "=" * 80)
    print("DEMO 4: ENTERPRISE SCENARIO - SALES ORDER PROCESSING")
    print("=" * 80)
    print("Realistic business scenario demonstrating agent orchestration.\n")

    agent = ChatCompletionAgent(
        kernel=kernel,
        name="SalesAgent",
        instructions="You are a sales order processing assistant. Use the available functions to calculate prices, discounts, taxes, and profit margins. Provide clear, formatted results."
    )

    scenario = """
    A customer orders a product with list price of $500.
    They have a corporate discount of 15%.
    After discount, add 7% sales tax.
    Calculate the profit margin if our cost is $300.
    Format all monetary values as currency.
    """

    print(f"Scenario:\n{scenario}\n")
    print("Processing order through agent...\n")

    chat_history = ChatHistory()
    chat_history.add_user_message(scenario)

    response_chunks = []
    async for chunk in agent.invoke_stream(messages=chat_history):
        if chunk.content:
            response_chunks.append(chunk.content.content)
            print(chunk.content, end="", flush=True)
    
    print("\n")
    result = "".join(response_chunks)

    print(f"\nOrder Processing Complete!")
    print(f"Result: {result}")

    print("\n" + "=" * 80)
