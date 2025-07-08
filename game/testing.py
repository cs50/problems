import random
import sys
import importlib.util
import ast
import types

# Monkey-patch randint, randrange, choice
random.randint = lambda x, y: 4
random.randrange = lambda x, *args, **kwargs: 4
random.choice = lambda x: 4

with open("game.py", "r") as f:
    source = f.read()
    tree = ast.parse(source)

# Find the if __name__ == "__main__" block
main_guard_node = None
for node in ast.walk(tree):
    if isinstance(node, ast.If):
        # Check if this is the __name__ == "__main__" pattern
        if (isinstance(node.test, ast.Compare) and
            isinstance(node.test.left, ast.Name) and
            node.test.left.id == "__name__" and
            len(node.test.ops) == 1 and
            isinstance(node.test.ops[0], ast.Eq) and
            len(node.test.comparators) == 1 and
            isinstance(node.test.comparators[0], ast.Constant) and
                node.test.comparators[0].value == "__main__"):
            main_guard_node = node
            break

# Load and execute the module
spec = importlib.util.spec_from_file_location("game", "game.py")
game = importlib.util.module_from_spec(spec)
sys.modules['game'] = game

# If there's a main guard, we need to handle it specially
if main_guard_node:
    # Create a modified AST that excludes the if __name__ == "__main__" block
    # This prevents the guarded code from running during import
    modified_tree = ast.Module(body=[], type_ignores=[])
    for node in tree.body:
        if node != main_guard_node:
            modified_tree.body.append(node)

    # Compile and execute the modified module (without the main guard)
    code = compile(modified_tree, "game.py", "exec")
    exec(code, game.__dict__)

    # Now execute the code that was inside the main guard
    # Create a new module with just the guarded code
    guarded_code = ast.Module(body=main_guard_node.body, type_ignores=[])
    code = compile(guarded_code, "<main_guard>", "exec")
    exec(code, game.__dict__)
else:
    # No main guard, just execute normally
    spec.loader.exec_module(game)
