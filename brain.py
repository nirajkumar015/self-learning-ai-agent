from llm import chat


class Brain:

    def __init__(self):
        self.model = "qwen3:4b"

    def think(self, task, memories=None):

        memory_text = ""

        if memories:

            memory_text = "\nRelevant lessons from previous experiences:\n"

            for memory in memories:

                lesson = memory.get("lesson", "")

                if lesson:
                    memory_text += (
                        f"- Previous task: {memory.get('task', '')}\n"
                        f"  Lesson: {lesson}\n"
                    )

        prompt = f"""
You are the brain of a self-learning AI agent.

Current task:

{task}

{memory_text}

Use previous lessons only when they are genuinely relevant.

Do not invent user preferences or facts that are not present
in the task or memories.

First decide whether the task needs a tool.

Available tools:

CALCULATOR
Use for mathematical calculations.

PYTHON
Use when Python code needs to be executed.

READ_FILE
Use when the user wants to read a file.

WRITE_FILE
Use when the user wants to create or modify a file.

NONE
Use only when no available tool is appropriate.

IMPORTANT:

If the task is mathematical and can be solved by the calculator,
prefer CALCULATOR instead of calculating mentally.

If the task asks to read a file, use READ_FILE.

If the task asks to create or modify a file, use WRITE_FILE.

If the task explicitly requires Python execution, use PYTHON.

Return EXACTLY one of these formats:

TOOL: CALCULATOR
EXPRESSION: 125 * 48

OR

TOOL: PYTHON
CODE: print(25 * 4)

OR

TOOL: READ_FILE
FILENAME: test.txt

OR

TOOL: WRITE_FILE
FILENAME: test.txt
CONTENT: Hello from MyAgent

OR

TOOL: NONE
ANSWER: your answer

Do not add explanations before or after the required format.
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