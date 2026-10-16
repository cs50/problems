import ast
import shlex

import check50
import check50.py

FUNCTION = "print_triangle_reversed"
LOOPS = (ast.For, ast.AsyncFor, ast.While, ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)


@check50.check()
def exists():
    """recursive_triangle.py exists"""
    check50.exists("recursive_triangle.py")


@check50.check(exists)
def imports():
    """recursive_triangle.py imports"""
    check50.py.import_("recursive_triangle.py")


@check50.check(imports)
def defined():
    """recursive_triangle.py defines print_triangle_reversed"""
    find_function()


@check50.check(defined)
def recursive():
    """print_triangle_reversed is recursive and uses no loops"""
    functions = top_level_functions()
    reachable = reachable_from(FUNCTION, functions)
    for name in reachable:
        if any(isinstance(node, LOOPS) for node in ast.walk(functions[name])):
            raise check50.Failure(f"{name} uses a loop instead of recursion")
    if not any(name in reachable_from(callee, functions) for name in reachable for callee in callees(functions[name], functions)):
        raise check50.Failure(f"{FUNCTION} does not use recursion")


@check50.check(defined)
def side_length_4():
    """print_triangle_reversed(4) prints a reversed triangle of side length 4"""
    check_triangle(4)


@check50.check(defined)
def side_length_1():
    """print_triangle_reversed(1) prints a single row"""
    check_triangle(1)


@check50.check(defined)
def side_length_0():
    """print_triangle_reversed(0) prints nothing"""
    check_triangle(0)


@check50.check(defined)
def side_length_negative():
    """print_triangle_reversed(-3) prints nothing"""
    check_triangle(-3)


def top_level_functions():
    """Return a dict mapping the name of each top-level function to its AST node."""
    with open("recursive_triangle.py") as f:
        tree = ast.parse(f.read())
    return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


def find_function():
    """Return the AST node for print_triangle_reversed, or fail if it is missing."""
    functions = top_level_functions()
    if FUNCTION not in functions:
        raise check50.Failure(f"could not find a function named {FUNCTION}")
    return functions[FUNCTION]


def callees(function, functions):
    """Return the names of the top-level functions that function calls."""
    return {
        node.func.id for node in ast.walk(function)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in functions
    }


def reachable_from(name, functions):
    """Return the names of name and every top-level function it calls, directly or indirectly."""
    reachable, stack = set(), [name]
    while stack:
        current = stack.pop()
        if current not in reachable:
            reachable.add(current)
            stack.extend(callees(functions[current], functions))
    return reachable


def check_triangle(side_length):
    """Call print_triangle_reversed(side_length), ignoring anything printed on import."""
    expected = "".join("[]" * i + "\n" for i in range(side_length, 0, -1))
    program = (
        "import contextlib, io\n"
        "with contextlib.redirect_stdout(io.StringIO()):\n"
        "    import recursive_triangle\n"
        f"recursive_triangle.{FUNCTION}({side_length})\n"
    )
    actual = check50.run(f"python3 -c {shlex.quote(program)}").stdout()
    if actual != expected:
        raise check50.Mismatch(expected, actual)
