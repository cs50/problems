import os

import check50
import check50.py

@check50.check()
def exists():
    """helpers.py exists"""
    check50.exists("helpers.py")

@check50.check(exists)
def compiles():
    """helpers.py compiles"""
    check50.py.import_("helpers.py")

@check50.check(compiles)
def edit_empty():
    """takes 0 operations to convert "" to "" """
    check_distance("", "", 0)

@check50.check(compiles)
def edit_from_empty():
    """takes 3 operations to convert "dog" to "" """
    check_distance("dog", "", 3)

@check50.check(compiles)
def edit_to_empty():
    """takes 4 operations to convert "" to "dog" """
    check_distance("", "dog", 3)

@check50.check(compiles)
def edit_a_b():
    """takes 1 operation to convert "a" to "b" """
    check_distance("a", "b", 1)

@check50.check(compiles)
def edit_insertion():
    """takes 1 operation to convert "cat" to "coat" """
    check_distance("cat", "coat", 1)

@check50.check(compiles)
def edit_deletion():
    """takes 1 operation to convert "frog" to "fog" """
    check_distance("frog", "fog", 1)

@check50.check(compiles)
def edit_substitution():
    """takes 1 operation to convert "year" to "pear" """
    check_distance("year", "pear", 1)

@check50.check(compiles)
def edit_identical():
    """takes 0 operations to convert "today" to "today" """
    check_distance("today", "today", 0)

@check50.check(compiles)
def edit_to_longer():
    """takes 5 operations to convert "today" to "yesterday" """
    check_distance("today", "yesterday", 5)

@check50.check(compiles)
def edit_to_shorter():
    """takes 6 operations to convert "tomorrow" to "today" """
    check_distance("tomorrow", "today", 6)

@check50.check(compiles)
def edit_handles_case():
    """takes 3 operations to convert "today" to "ToDaY" """
    check_distance("today", "ToDaY", 3)


def check_distance(a, b, expected):
    helpers = check50.py.import_("helpers.py")
    check50.log(f"checking edit distance for inputs {repr(a)} and {repr(b)}...")
    with open(os.devnull, "w") as f:
        try:
            actual = helpers.distances(a, b)[len(a)][len(b)][0]
        except Exception as e:
            raise check50.Failure(str(e))

    if actual != expected:
        raise check50.Failure(f"expected edit distance of {expected}, not {actual}")

