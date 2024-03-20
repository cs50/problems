import random
import re
import inspect

# Monkey-patch randint, randrange, choice
random.randint = lambda x, y: 4
random.randrange = lambda x, *args, **kwargs: 4
random.choice = lambda x: 4

# Run game via import
import game

# Run game if not run when imported
try:
    # Get commentless source
    source = re.sub(r"#.*(\n|$)", "", inspect.getsource(game))
    # Look for __name__ check
    if '__name__ == "__main__":' in source:
        game.main()
except AttributeError:
    # game has no main function
    pass
