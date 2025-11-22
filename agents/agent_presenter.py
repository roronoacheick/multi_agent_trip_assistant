from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any

from groq import Groq
from config import groq_client, groq_settings


class PresenterAgent:

    def __init__(self):
        base = Path("prompts")
        self.prompt_path = base / "presenter_prompt.txt"
        self.context_path = base / "presenter_context.txt"

        self.system_prompt = self.prompt_path.read_text(encoding="utf-8")
        self.context_text = self.context_path.read_text(encoding="utf-8")

        self.client: Groq = groq_client
        self.model_name: str = groq_settings.default_model

    def present(
        self,
        scenarios: List[Dict[str, Any]],
        constraints: Dict[str, Any],
        weather: Dict[str, Any]
    ) -> str:
        
        payload = {
            "scenarios": scenarios,
            "constraints": constraints,
            "weather": weather
        }

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": self.context_text},
            {
                "role": "user",
                "content": f"Voici les données à présenter :\n{json.dumps(payload, indent=2, ensure_ascii=False)}"
            }
        ]

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages
        )

        return response.choices[0].message.content
