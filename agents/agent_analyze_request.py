from __future__ import annotations

import json
from pathlib import Path

from groq import Groq

from config import groq_client, groq_settings


class AnalyzeRequestAgent:

    def __init__(self):
        
        base = Path("prompts")
        self.prompt_path = base / "analyze_prompt.txt"
        self.context_path = base / "analyze_context.txt"

        self.system_prompt = self.prompt_path.read_text(encoding="utf-8")
        self.context_text = self.context_path.read_text(encoding="utf-8")

        # Client Groq + modèle
        self.client: Groq = groq_client
        self.model_name: str = groq_settings.default_model

    def analyze(self, user_message: str) -> dict:

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": self.context_text},
            {"role": "user", "content": user_message},
        ]

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            response_format={"type": "json_object"}  
        )

        
        raw_output = response.choices[0].message.content

        try:
            parsed_json = json.loads(raw_output)
        except json.JSONDecodeError as error:
            print("Erreur lors du parsing JSON :", error)
            print("Contenu brut renvoyé par le modèle :")
            print(raw_output)

            
            parsed_json = {
                "location": None,
                "date_range": {"start": None, "end": None},
                "budget_total": None,
                "preferences": [],
                "people_count": None
            }

        return parsed_json
