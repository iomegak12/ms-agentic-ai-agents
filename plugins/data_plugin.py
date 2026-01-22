"""
Data Transformation Plugin
===========================
Data transformation and formatting operations.
"""

from semantic_kernel.functions import kernel_function


class DataPlugin:
    """Data transformation and formatting operations"""

    @kernel_function(
        name="format_currency",
        description="Formats a number as currency with dollar sign and two decimal places"
    )
    def format_currency(self, amount: float) -> str:
        """Format as currency"""
        result = f"${amount:,.2f}"
        print(f"   [DataPlugin] Formatting currency: {amount} → {result}")
        return result

    @kernel_function(
        name="calculate_average",
        description="Calculates the average of comma-separated numbers"
    )
    def calculate_average(self, numbers: str) -> float:
        """Calculate average from comma-separated string"""
        num_list = [float(n.strip()) for n in numbers.split(',')]
        avg = sum(num_list) / len(num_list)
        print(f"   [DataPlugin] Average of {numbers} = {avg}")
        return avg

    @kernel_function(
        name="concatenate",
        description="Joins multiple text strings together with a separator"
    )
    def concatenate(self, text1: str, text2: str, separator: str = " ") -> str:
        """Concatenate strings"""
        result = f"{text1}{separator}{text2}"
        print(
            f"   [DataPlugin] Concatenating: '{text1}' + '{text2}' → '{result}'")
        return result
