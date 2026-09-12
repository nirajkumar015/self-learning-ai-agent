import ast
import operator


OPERATORS = {
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


def calculate(expression):

    try:
        tree = ast.parse(expression, mode="eval")

        def evaluate(node):

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value

                raise ValueError("Only numbers are allowed.")

            if isinstance(node, ast.BinOp):
                operation = OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError("Operator not allowed.")

                left = evaluate(node.left)
                right = evaluate(node.right)

                return operation(left, right)

            if isinstance(node, ast.UnaryOp):
                operation = OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError("Operator not allowed.")

                return operation(evaluate(node.operand))

            raise ValueError("Invalid mathematical expression.")

        return evaluate(tree.body)

    except Exception as error:

        return f"Calculator Error: {error}"