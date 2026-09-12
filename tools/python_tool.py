import io
from contextlib import redirect_stdout


def run_python(code):

    try:

        output = io.StringIO()

        with redirect_stdout(output):

            exec(code, {})

        result = output.getvalue().strip()

        if result:

            return result

        return "Python code executed successfully."

    except Exception as error:

        return f"Python Error: {error}"