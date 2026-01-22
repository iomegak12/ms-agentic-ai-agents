"""
Text Processing Plugin
======================
Text manipulation and processing operations.
"""

from semantic_kernel.functions import kernel_function


class TextPlugin:
    """Text manipulation and processing operations"""

    @kernel_function(
        name="uppercase",
        description="Converts text to uppercase letters"
    )
    def uppercase(self, text: str) -> str:
        """Convert text to uppercase"""
        result = text.upper()
        print(f"   [TextPlugin] Converting to uppercase: {text} → {result}")
        return result

    @kernel_function(
        name="count_words",
        description="Counts the number of words in a text"
    )
    def count_words(self, text: str) -> int:
        """Count words in text"""
        words = text.split()
        count = len(words)
        print(f"   [TextPlugin] Counting words in '{text}': {count} words")
        return count

    @kernel_function(
        name="reverse_text",
        description="Reverses the order of characters in text"
    )
    def reverse_text(self, text: str) -> str:
        """Reverse text"""
        result = text[::-1]
        print(f"   [TextPlugin] Reversing: {text} → {result}")
        return result
