from ollama import chat


class Learner:

    def __init__(self):
        self.model = "qwen3:4b"

    def learn(self, task, result, success):

        prompt = f"""
You are a learning module.

TASK:
{task}

RESULT:
{result}

SUCCESS:
{success}

Write ONE short reusable lesson.

The lesson must:
- be one sentence
- be practical
- be less than 25 words
- describe a method or strategy
- not repeat the answer
- not explain the reasoning
- not use Markdown
- not use headings
- not use bullet points
- not use examples

If there is no useful lesson, write exactly:

NO_USEFUL_LESSON

Return ONLY the lesson sentence.
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

        lesson = response.message.content.strip()

        # Basic cleanup if the model still adds formatting
        lesson = lesson.replace("**", "")
        lesson = lesson.replace("###", "")
        
        if len(lesson.split()) > 25:
            lesson = (
                "Use the successful procedure from this experience "
                "when handling similar tasks."
            )

        return lesson