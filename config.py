from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


@dataclass
class GroqSettings:
    api_key: str
    default_model: str = "openai/gpt-oss-20b"

    @classmethod
    def from_env(cls) -> "GroqSettings":
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY is missing. "
                "Check your .env file at the project root."
            )
        return cls(api_key=api_key)


@dataclass
class WeatherSettings:
    api_key: str
    base_url: str = "https://api.openweathermap.org/data/2.5/weather"
    default_units: str = "metric"   # Celsius
    default_language: str = "fr"    # Réponses de l'API en français

    @classmethod
    def from_env(cls) -> "WeatherSettings":
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENWEATHER_API_KEY is missing. "
                "Check your .env file at the project root."
            )
        return cls(api_key=api_key)


groq_settings = GroqSettings.from_env()
weather_settings = WeatherSettings.from_env()

groq_client = Groq(
    api_key=groq_settings.api_key
)
