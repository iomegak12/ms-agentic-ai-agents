"""
Business Logic Plugin
=====================
Business-related calculations and operations.
"""

from semantic_kernel.functions import kernel_function


class BusinessPlugin:
    """Business-related calculations and operations"""

    @kernel_function(
        name="calculate_discount",
        description="Calculates the discounted price given original price and discount percentage"
    )
    def calculate_discount(self, price: float, discount_percent: float) -> float:
        """Calculate price after discount"""
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        print(
            f"   [BusinessPlugin] Original: ${price}, Discount: {discount_percent}% → Final: ${final_price}")
        return final_price

    @kernel_function(
        name="calculate_tax",
        description="Calculates tax amount for a given price and tax rate"
    )
    def calculate_tax(self, price: float, tax_rate: float) -> float:
        """Calculate tax"""
        tax = price * (tax_rate / 100)
        print(
            f"   [BusinessPlugin] Price: ${price}, Tax rate: {tax_rate}% → Tax: ${tax}")
        return tax

    @kernel_function(
        name="calculate_profit_margin",
        description="Calculates profit margin percentage given cost and selling price"
    )
    def calculate_profit_margin(self, cost: float, selling_price: float) -> float:
        """Calculate profit margin"""
        profit = selling_price - cost
        margin = (profit / selling_price) * 100 if selling_price > 0 else 0
        print(
            f"   [BusinessPlugin] Cost: ${cost}, Price: ${selling_price} → Margin: {margin:.2f}%")
        return margin
