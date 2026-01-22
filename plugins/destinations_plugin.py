"""
Destinations Plugin
===================
Plugin that provides detailed information about travel destinations.
"""

from semantic_kernel.functions import kernel_function


class DestinationsPlugin:
    """Plugin for providing detailed travel destination information"""
    
    # Destination data store with rich details about popular travel locations
    DESTINATIONS = {
        "maldives": {
            "name": "The Maldives",
            "description": "An archipelago of 26 atolls in the Indian Ocean, known for pristine beaches and overwater bungalows.",
            "best_time": "November to April (dry season)",
            "activities": ["Snorkeling", "Diving", "Island hopping", "Spa retreats", "Underwater dining"],
            "avg_cost": "$400-1200 per night for luxury resorts"
        },
        "swiss alps": {
            "name": "The Swiss Alps",
            "description": "Mountain range spanning across Switzerland with picturesque villages and world-class ski resorts.",
            "best_time": "December to March for skiing, June to September for hiking",
            "activities": ["Skiing", "Snowboarding", "Hiking", "Mountain biking", "Paragliding"],
            "avg_cost": "$250-500 per night for alpine accommodations"
        },
        "safari": {
            "name": "African Safari",
            "description": "Wildlife viewing experiences across various African countries including Kenya, Tanzania, and South Africa.",
            "best_time": "June to October (dry season) for optimal wildlife viewing",
            "activities": ["Game drives", "Walking safaris", "Hot air balloon rides", "Cultural village visits"],
            "avg_cost": "$400-800 per person per day for luxury safari packages"
        },
        "bali": {
            "name": "Bali, Indonesia",
            "description": "Island paradise known for lush rice terraces, beautiful temples, and vibrant culture.",
            "best_time": "April to October (dry season)",
            "activities": ["Surfing", "Temple visits", "Rice terrace trekking", "Yoga retreats", "Beach relaxation"],
            "avg_cost": "$100-500 per night depending on accommodation type"
        },
        "santorini": {
            "name": "Santorini, Greece",
            "description": "Stunning volcanic island with white-washed buildings and blue domes overlooking the Aegean Sea.",
            "best_time": "Late April to early November",
            "activities": ["Sunset watching in Oia", "Wine tasting", "Boat tours", "Beach hopping", "Ancient ruins exploration"],
            "avg_cost": "$200-600 per night for caldera view accommodations"
        }
    }

    @kernel_function(
        name="get_destination_info",
        description="Provides detailed information about specific travel destinations."
    )
    def get_destination_info(self, query: str) -> str:
        """Get detailed information about a travel destination"""
        # Find which destination is being asked about
        query_lower = query.lower()
        matching_destinations = []

        for key, details in DestinationsPlugin.DESTINATIONS.items():
            if key in query_lower or details["name"].lower() in query_lower:
                matching_destinations.append(details)

        if not matching_destinations:
            return (f"User Query: {query}\n\n"
                    f"I couldn't find specific destination information in our database. "
                    f"Please use the general retrieval system for this query.")

        # Format destination information
        destination_info = "\n\n".join([
            f"Destination: {dest['name']}\n"
            f"Description: {dest['description']}\n"
            f"Best time to visit: {dest['best_time']}\n"
            f"Popular activities: {', '.join(dest['activities'])}\n"
            f"Average cost: {dest['avg_cost']}" for dest in matching_destinations
        ])

        return (f"Destination Information:\n{destination_info}\n\n"
                f"User Query: {query}\n\n"
                "Based on the above destination details, provide a helpful response "
                "that addresses the user's query about this location.")
