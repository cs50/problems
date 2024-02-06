import random

# Setting seed to have static "random" results
random.seed(0)

# Run game via import
import game

# Run game if not run when imported
try:
    game.main()
except AttributeError:

    # game has no main function
    pass
