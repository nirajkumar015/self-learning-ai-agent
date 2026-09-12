from ollama import chat


class FinalResponse:

    def __init__(self):

        self.model = "qwen3:4b"

    def generate(self, goal, results):

        results_text = ""

        for number, result in enumerate(
            results,
            start=1
        ):

            results_text += (
                f"Step {number}: {result}\n"
            )

        prompt = f"""
You are the final response system of an AI agent.

The user's original goal was:

{goal}

The agent completed these steps:

{results_text}

Create a concise final response for the user.

Rules:

- Clearly state whether the goal was completed.
- Summarize the important result.
- Mention important files created or read.
- Do not describe internal reasoning.
- Do not mention the Planner, Brain, or Learner.
- Keep the response under 100 words.

Return only the final response.
"""

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content.strip()