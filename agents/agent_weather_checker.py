from __future__ import annotations

import requests
from typing import Dict, Any

from config import weather_settings


class WeatherCheckerAgent:

    def __init__(self):
        self.api_key = weather_settings.api_key
        self.base_url = weather_settings.base_url
        self.units = weather_settings.default_units
        self.lang = weather_settings.default_language

    def fetch_weather(self, city_name: str) -> Dict[str, Any]:

        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": self.units,
            "lang": self.lang
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            raise RuntimeError(
                f"Erreur API météo ({response.status_code}) : {response.text}"
            )

        data = response.json()
        return data

    def analyze_weather(self, weather_data: Dict[str, Any]) -> Dict[str, Any]:

        temperature = weather_data["main"]["temp"]
        weather_main = weather_data["weather"][0]["main"]
        weather_desc = weather_data["weather"][0]["description"]

        # Interprétation baignade
        if weather_main.lower() in ["rain", "thunderstorm", "drizzle"]:
            swimming = "Pluie"
        elif temperature >= 20:
            swimming = "OK"
        else:
            swimming = "Moyen"

        return {
            "temperature": temperature,
            "weather_main": weather_main,
            "weather_description": weather_desc,
            "swimming_recommendation": swimming
        }

    def get_weather_summary(self, city_name: str) -> Dict[str, Any]:

        raw_data = self.fetch_weather(city_name)
        analyzed = self.analyze_weather(raw_data)

        return {
            "location": city_name,
            **analyzed
        }
