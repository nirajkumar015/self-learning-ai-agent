import os
import time
import random

from ollama import chat as ollama_chat


class Message:
    def __init__(self, content):
        self.content = content


class Response:
    def __init__(self, content):
        self.message = Message(content)


class LLM:

    def __init__(self):

        self.gemini_api_key = os.getenv("GEMINI_API_KEY")

        if self.gemini_api_key:

            from google import genai

            self.client = genai.Client(
                api_key=self.gemini_api_key
            )

            self.provider = "gemini"
            self.model = "gemini-3.8-flash"

        else:

            self.client = None
            self.provider = "ollama"
            self.model = "qwen3:4b"


    def chat(self, messages):

        prompt = "\n\n".join(
            message["content"]
            for message in messages
        )


        # ==============================
        # GEMINI
        # ==============================

        if self.provider == "gemini":

            max_attempts = 4

            for attempt in range(1, max_attempts + 1):

                try:

                    response = self.client.models.generate_content(
                        model=self.model,
                        contents=prompt
                    )

                    return Response(
                        response.text
                    )

                except Exception as error:

                    error_text = str(error)

                    is_temporary_error = (
                        "503" in error_text
                        or "UNAVAILABLE" in error_text
                        or "429" in error_text
                        or "RESOURCE_EXHAUSTED" in error_text
                    )

                    if not is_temporary_error:
                        raise

                    if attempt == max_attempts:
                        raise

                    wait_time = (
                        2 ** (attempt - 1)
                        + random.uniform(0, 1)
                    )

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retry {attempt}/{max_attempts}"
                    )

                    time.sleep(wait_time)


        # ==============================
        # OLLAMA
        # ==============================

        if self.provider == "ollama":

            try:

                response = ollama_chat(
                    model=self.model,
                    messages=messages
                )

                return Response(
                    response.message.content
                )

            except Exception as error:

                raise RuntimeError(
                    "Ollama is unavailable. "
                    "On Streamlit Cloud, add GEMINI_API_KEY "
                    "in App Settings → Secrets."
                ) from error


_llm = LLM()


def chat(model=None, messages=None):

    return _llm.chat(messages or [])