from ollama import chat


class Planner:

    def __init__(self):

        self.model = "qwen3:4b"

    def create_plan(self, goal):

        prompt = f"""
You are the planning system of an AI agent.

The user has given this goal:

{goal}

Break the goal into small, logical steps.

Available tools:

CALCULATOR
PYTHON
READ_FILE
WRITE_FILE
NONE

For every step, specify the tool that should be used.

Return ONLY this format:

STEP 1
TOOL: TOOL_NAME
TASK: what this step should do

STEP 2
TOOL: TOOL_NAME
TASK: what this step should do

Continue until the goal is complete.

Do not add explanations outside the steps.
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

        return response.message.content