import random
random.randint = lambda x, y : 4
random.randrange = lambda x, y : 4
import game

# Run game if not run when imported
game.main()