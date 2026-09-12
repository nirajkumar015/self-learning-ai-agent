from memory import Memory
from brain import Brain
from planner import Planner
from learner import Learner
from final_response import FinalResponse

from tools.calculator import calculate
from tools.python_tool import run_python
from tools.file_tool import read_file, write_file


class Agent:

    def __init__(self, name):

        self.name = name
        self.memory = Memory()
        self.brain = Brain()
        self.planner = Planner()
        self.learner = Learner()
        self.final_response = FinalResponse()

    # ---------------------------------
    # THINK
    # ---------------------------------

    def think(self, task, context=""):

        print(f"\n{self.name} is thinking...")

        relevant_memories = self.memory.get_relevant_memories(task)

        if context:

            brain_task = f"""
Current task:
{task}

Previous step result:
{context}

Use the previous step result if the current task depends on it.
"""

        else:

            brain_task = task

        decision = self.brain.think(
            brain_task,
            relevant_memories
        )

        print("\n🧠 AI Brain:")
        print(decision)

        return decision

    # ---------------------------------
    # PLAN
    # ---------------------------------

    def plan(self, goal):

        print("\n📋 Agent is creating a plan...")

        plan = self.planner.create_plan(goal)

        print("\n📋 PLAN:")
        print(plan)

        return plan

    # ---------------------------------
    # ACT
    # ---------------------------------

    def act(self, task, thinking, planned_tool=None):

        print("\n🛠️ Agent is executing the planned tool...")

        lines = thinking.splitlines()

        tool = planned_tool

        # ---------------------------------
        # CALCULATOR
        # ---------------------------------

        if tool == "CALCULATOR":

            expression = ""

            for line in lines:

                if line.startswith("EXPRESSION:"):

                    expression = line.replace(
                        "EXPRESSION:",
                        ""
                    ).strip()

            if not expression:

                expression = task.strip()

                if expression.lower().startswith("calculate"):

                    expression = expression[
                        len("calculate"):
                    ].strip()

                elif expression.lower().startswith("compute"):

                    expression = expression[
                        len("compute"):
                    ].strip()

            result = calculate(expression)

            print("\n🧮 Calculator result:")
            print(result)

            return str(result)

        # ---------------------------------
        # PYTHON
        # ---------------------------------

        elif tool == "PYTHON":

            code = ""

            for line in lines:

                if line.startswith("CODE:"):

                    code = line.replace(
                        "CODE:",
                        ""
                    ).strip()

            # Fallback when Brain doesn't return CODE
            if not code:

                print(
                    "\n⚠️ Brain did not provide Python code."
                )

                print(
                    "🔧 Creating Python code from the task..."
                )

                code = self.create_python_code(task)

            if not code:

                return (
                    "Python Error: "
                    "Could not create Python code."
                )

            result = run_python(code)

            print("\n🐍 Python result:")
            print(result)

            return result

        # ---------------------------------
        # READ FILE
        # ---------------------------------

        elif tool == "READ_FILE":

            filename = ""

            for line in lines:

                if line.startswith("FILENAME:"):

                    filename = line.replace(
                        "FILENAME:",
                        ""
                    ).strip()

            if not filename:

                filename = self.extract_filename(task)

            if not filename:

                return (
                    "File Error: "
                    "No filename was provided."
                )

            result = read_file(filename)

            print("\n📁 File contents:")
            print(result)

            return result

        # ---------------------------------
        # WRITE FILE
        # ---------------------------------

        elif tool == "WRITE_FILE":

            filename = ""
            content = ""

            for line in lines:

                if line.startswith("FILENAME:"):

                    filename = line.replace(
                        "FILENAME:",
                        ""
                    ).strip()

                elif line.startswith("CONTENT:"):

                    content = line.replace(
                        "CONTENT:",
                        ""
                    ).strip()

            if not filename:

                filename = self.extract_filename(task)

            if not content:

                # Use previous step result when available
                content = ""

            if not filename:

                return (
                    "File Error: "
                    "No filename was provided."
                )

            if not content:

                return (
                    "File Error: "
                    "No content was provided."
                )

            result = write_file(
                filename,
                content
            )

            print("\n📁 File result:")
            print(result)

            return result

        # ---------------------------------
        # NONE
        # ---------------------------------

        elif tool == "NONE":

            print("\n💬 No tool needed.")

            answer = ""

            for line in lines:

                if line.startswith("ANSWER:"):

                    answer = line.replace(
                        "ANSWER:",
                        ""
                    ).strip()

            if answer:

                return answer

            return thinking

        # ---------------------------------
        # UNKNOWN TOOL
        # ---------------------------------

        else:

            return (
                f"Tool Error: Unknown planned tool "
                f"'{planned_tool}'."
            )

    # ---------------------------------
    # CREATE PYTHON CODE
    # ---------------------------------

    def create_python_code(self, task):

        task_lower = task.lower()

        # Handle simple multiplication
        if "*" in task:

            expression = task_lower

            if "calculate" in expression:

                expression = expression.replace(
                    "calculate",
                    ""
                ).strip()

            if "compute" in expression:

                expression = expression.replace(
                    "compute",
                    ""
                ).strip()

            return f"print({expression})"

        # Handle simple addition
        if "+" in task:

            expression = task_lower

            if "calculate" in expression:

                expression = expression.replace(
                    "calculate",
                    ""
                ).strip()

            if "compute" in expression:

                expression = expression.replace(
                    "compute",
                    ""
                ).strip()

            return f"print({expression})"

        return ""

    # ---------------------------------
    # EXTRACT FILENAME
    # ---------------------------------

    def extract_filename(self, task):

        words = task.split()

        for word in words:

            if "." in word:

                return word.strip(
                    ".,!?\"'"
                )

        return ""

    # ---------------------------------
    # OBSERVE
    # ---------------------------------

    def observe(self, result):

        print("\n👀 Agent observed the result:")
        print(result)

    # ---------------------------------
    # EVALUATE
    # ---------------------------------

    def evaluate(self, result):

        print("\n🔍 Agent is evaluating the result...")

        if result is None:

            return False

        result_text = str(result).strip()

        if not result_text:

            return False

        result_lower = result_text.lower()

        error_signals = [
            "error:",
            "python error:",
            "file error:",
            "calculator error:",
            "tool error:"
        ]

        for error in error_signals:

            if error in result_lower:

                return False

        return True

    # ---------------------------------
    # LEARN
    # ---------------------------------

    def learn(self, task, result, success):

        print(
            "\n🧠 Agent is learning from the experience..."
        )

        lesson = self.learner.learn(
            task,
            result,
            success
        )

        experience = {
            "task": task,
            "result": result,
            "success": success
        }

        if lesson != "NO_USEFUL_LESSON":

            experience["lesson"] = lesson

        self.memory.remember(experience)

        if lesson != "NO_USEFUL_LESSON":

            print("\n📚 Lesson learned:")
            print(lesson)

        else:

            print(
                "\n📚 No useful reusable lesson found."
            )

        print(
            "\n💾 Experience saved to memory."
        )

    # ---------------------------------
    # SHOW LEARNING
    # ---------------------------------

    def show_learning(self):

        memories = self.memory.get_memories()

        print("\n" + "=" * 50)
        print("🧠 WHAT I HAVE LEARNED")
        print("=" * 50)

        lessons_found = False

        for number, memory in enumerate(
            memories,
            start=1
        ):

            lesson = memory.get("lesson")

            if lesson:

                lessons_found = True

                print(f"\nLesson {number}:")
                print(
                    f"Task: {memory.get('task', '')}"
                )
                print(
                    f"Lesson: {lesson}"
                )
                print(
                    f"Success: {memory.get('success', '')}"
                )

        if not lessons_found:

            print("\nNo lessons learned yet.")

        print("\n" + "=" * 50)

    # ---------------------------------
    # FINAL RESPONSE
    # ---------------------------------

    def create_final_response(self, goal, results):

        print(
            "\n📝 Agent is creating the final response..."
        )

        response = self.final_response.generate(
            goal,
            results
        )

        return response