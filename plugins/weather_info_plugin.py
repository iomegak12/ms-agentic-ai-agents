"""
Weather Info Plugin
===================
Plugin that provides average temperature information for travel destinations.
"""

from semantic_kernel.functions import kernel_function
from typing import Annotated


class WeatherInfoPlugin:
    """A Plugin that provides the average temperature for a travel destination."""

    def __init__(self):
        # Dictionary of destinations and their average temperatures
        self.destination_temperatures = {
            "maldives": "82°F (28°C)",
            "swiss alps": "45°F (7°C)",
            "african safaris": "75°F (24°C)"
        }

    @kernel_function(
        description="Get the average temperature for a specific travel destination."
    )
    def get_destination_temperature(
        self, 
        destination: str
    ) -> Annotated[str, "Returns the average temperature for the destination."]:
        """Get the average temperature for a travel destination."""
        # Normalize the input destination (lowercase)
        normalized_destination = destination.lower()

        # Look up the temperature for the destination
        if normalized_destination in self.destination_temperatures:
            return f"The average temperature in {destination} is {self.destination_temperatures[normalized_destination]}."
        else:
            return f"Sorry, I don't have temperature information for {destination}. Available destinations are: Maldives, Swiss Alps, and African safaris."
