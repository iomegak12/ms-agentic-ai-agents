"""
Semantic Kernel Agent Demo
===========================
Demonstrates Semantic Kernel's agent capabilities with simple, easy-to-understand plugins.
Perfect for enterprise training on AI orchestration and agentic systems.

Author: REDIVAC Technologies
Purpose: Training demonstration for Fortune 500 clients
"""

import asyncio
from utils.kernel_setup import setup_kernel
from agents import (
    demo_basic_agent,
    demo_reasoning_agent,
    demo_agent_comparison,
    demo_enterprise_scenario
)


# ============================================================================
# MAIN DEMONSTRATION RUNNER
# ============================================================================
async def main():
    """
    Main function to run all demonstrations
    """
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "  SEMANTIC KERNEL AGENT DEMONSTRATION".center(78) + "║")
    print("║" + "  Enterprise AI Training by REDIVAC Technologies".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "=" * 78 + "╝")
    print()

    # Initialize kernel
    kernel = await setup_kernel()

    # Run demonstrations
    try:
        # Demo 1: Basic agent with auto function calling
        await demo_basic_agent(kernel)

        # Demo 2: Agent with complex reasoning
        await demo_reasoning_agent(kernel)

        # Demo 3: Compare agents
        await demo_agent_comparison(kernel)

        # Demo 4: Enterprise scenario
        await demo_enterprise_scenario(kernel)

        print("\n" + "=" * 80)
        print("ALL DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        print("\nKey Takeaways:")
        print("1. Agents: Use function calling to orchestrate complex workflows")
        print("2. Instructions: Different instructions guide agent behavior")
        print("3. Plugins: Modular, reusable components for specific capabilities")
        print("4. Orchestration: Agents automatically chain functions to achieve goals")
        print("\n")

    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        print("\nNote: Make sure to set your Azure OpenAI credentials:")
        print("  - AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
        print("  - AZURE_OPENAI_ENDPOINT")
        print("  - AZURE_OPENAI_API_KEY")


if __name__ == "__main__":
    asyncio.run(main())
