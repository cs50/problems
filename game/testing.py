import random

# Monkey-patch randint, randrange, choice
random.randint = lambda x, y : 4
random.randrange = lambda x, *args, **kwargs : 4
random.choice = lambda x : 4

# Run game via import
import game

# Run game if not run when imported
try:
    game.main()
except AttributeError:

    # game has no main function
    pass
