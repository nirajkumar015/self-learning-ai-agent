import ast
import io
import operator
from contextlib import redirect_stdout


ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def run_python(code):

    try:

        tree = ast.parse(code, mode="exec")

        for node in ast.walk(tree):

            # Only allow basic calculations and print()
            if isinstance(node, ast.Call):

                if not (
                    isinstance(node.func, ast.Name)
                    and node.func.id == "print"
                ):
                    raise ValueError(
                        "Only print() is allowed."
                    )

            elif isinstance(node, ast.Name):

                if node.id != "print":
                    raise ValueError(
                        f"Name '{node.id}' is not allowed."
                    )

            elif isinstance(node, (
                ast.Import,
                ast.ImportFrom,
                ast.FunctionDef,
                ast.AsyncFunctionDef,
                ast.ClassDef,
                ast.Lambda,
                ast.With,
                ast.AsyncWith,
                ast.For,
                ast.AsyncFor,
                ast.While,
                ast.Try,
                ast.Raise,
                ast.Delete,
                ast.Global,
                ast.Nonlocal,
            )):

                raise ValueError(
                    "This Python operation is not allowed."
                )

        output = io.StringIO()

        safe_builtins = {
            "print": print
        }

        with redirect_stdout(output):

            exec(
                compile(tree, "<safe_python>", "exec"),
                {
                    "__builtins__": safe_builtins
                },
                {}
            )

        result = output.getvalue().strip()

        if result:
            return result

        return "Python code executed successfully."

    except Exception as error:

        return f"Python Error: {error}"