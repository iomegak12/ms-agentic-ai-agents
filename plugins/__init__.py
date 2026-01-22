"""
Semantic Kernel Plugins
========================
Collection of plugins for enterprise training demonstrations.
"""

from .math_plugin import MathPlugin
from .text_plugin import TextPlugin
from .business_plugin import BusinessPlugin
from .data_plugin import DataPlugin
from .prompt_plugin import PromptPlugin
from .weather_info_plugin import WeatherInfoPlugin
from .destinations_plugin import DestinationsPlugin

__all__ = [
    'MathPlugin', 
    'TextPlugin', 
    'BusinessPlugin', 
    'DataPlugin',
    'PromptPlugin',
    'WeatherInfoPlugin',
    'DestinationsPlugin'
]
