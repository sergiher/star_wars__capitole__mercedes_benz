import os

from google import genai  # type: ignore


class GoogleService:
    def __init__(self, model_name="gemini-2.0-flash-001"):
        self.model_name = model_name
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            self.client = None
        else:
            self.client = genai.Client(api_key=self.api_key)

    def generate_response(self, input_text: str):
        if not self.client:
            return "Please provide a GOOGLE_API_KEY"
        response = self.client.models.generate_content(
            model=self.model_name, contents=input_text
        )
        return response

    def explain_about(self, input_text: str) -> str:
        response = self.generate_response(input_text)
        if isinstance(response, str):
            return response
        return response.text
