"""
Math Operations Plugin
======================
Simple math operations plugin for basic calculations.
"""

from semantic_kernel.functions import kernel_function


class MathPlugin:
    """Simple math operations plugin for basic calculations"""

    @kernel_function(
        name="add",
        description="Adds two numbers together"
    )
    def add(self, number1: float, number2: float) -> float:
        """Add two numbers"""
        result = number1 + number2
        print(f"   [MathPlugin] Adding {number1} + {number2} = {result}")
        return result

    @kernel_function(
        name="multiply",
        description="Multiplies two numbers together"
    )
    def multiply(self, number1: float, number2: float) -> float:
        """Multiply two numbers"""
        result = number1 * number2
        print(f"   [MathPlugin] Multiplying {number1} × {number2} = {result}")
        return result

    @kernel_function(
        name="subtract",
        description="Subtracts second number from first number"
    )
    def subtract(self, number1: float, number2: float) -> float:
        """Subtract two numbers"""
        result = number1 - number2
        print(f"   [MathPlugin] Subtracting {number1} - {number2} = {result}")
        return result
