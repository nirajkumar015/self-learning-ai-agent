from llm import chat


class Learner:
    def __init__(self):
        self.model = "gemini-3.8-flash"

    def learn(self, task, result, success):
        prompt = f"""
You are the learning system of an AI agent.

The agent attempted this task:

TASK:
{task}

RESULT:
{result}

SUCCESS:
{success}

Analyze this experience.

Extract one useful lesson that could help the agent
perform similar tasks better in the future.

Keep the lesson short and practical.

If there is no useful reusable lesson, return exactly:

NO_USEFUL_LESSON

Return ONLY the lesson.
"""

        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            lesson = response.message.content.strip()

            if not lesson:
                return "NO_USEFUL_LESSON"

            return lesson

        except Exception as error:
            print("\n⚠️ Learning system temporarily unavailable.")
            print(f"Learning error: {error}")
            print("➡️ Saving the experience without a lesson.")

            return "NO_USEFUL_LESSON"