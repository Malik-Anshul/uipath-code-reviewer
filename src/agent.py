import json
from src.prompts import SYSTEM_PROMPT

class CodeReviewAgent:
    def __init__(self, groq_client):
        self.client = groq_client
        self.history = []
        self.prompt = SYSTEM_PROMPT

    def code_review(self, code):
        messages = [
            {"role": "system", "content": self.prompt},
            *self.history[-10:],
            {"role": "user", "content": code}
        ]

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.4
            )

            text = response.choices[0].message.content.strip()

            self.history.append({"role": "user", "content": code})
            self.history.append({"role": "assistant", "content": text})

            try:
                parsed = json.loads(text)
                return parsed
            except json.JSONDecodeError:
                return {"error": "JSON parsing failed", "raw_response": text}

        except Exception as e:
            return {"error": f"API call failed: {str(e)}"}

    def clear_history(self):
        self.history = []
        print("History cleared ✅")

    def get_history(self):
        return self.history