import random
import re


def get_lines():
    """Get source of game.py to check if student has added an offset to randrange
    for example:
    my_number = randrange(max) + 1
    """
    with open('game.py', 'r', encoding='utf8') as f:
        src = f.read()
    return src


def randrange_has_mods(src):
    """Returns True if student code contains offset"""
    regex = r'randrange\(.*?\)\s\+\s\d+'
    if re.search(regex, src):
        return True
    else:
        return False


def get_mod(src):
    """Finally capture offset in student code"""
    regex = r'randrange\(.*?\)\s\+\s(\d+)'
    if digit := re.search(regex, src):
        return int(digit.group(1))


# Monkey-patch randint, randrange, choice
random.randint = lambda x, y: 4
src = get_lines()
if randrange_has_mods(src):
    # Student code contains an offset to randrange
    digit = get_mod(src)
    random.randrange = lambda x, *args, **kwargs: 4 - digit
else:
    # Student code does not have an offset added
    random.randrange = lambda x, *args, **kwargs: 4
random.choice = lambda x: 4


# Run game via import
import game

# Run game if not run when imported
try:
    game.main()
except AttributeError:

    # game has no main function
    pass
