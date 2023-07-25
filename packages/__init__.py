import re

import check50

# global array of booleans; ith boolean designates whether answer i is right
results = []


@check50.check()
def exists():
    """log.sql and answers.txt exist"""
    check50.exists("log.sql", "answers.txt")
    check50.include("template.txt")

@check50.check(exists)
def log_file():
    """log file contains SELECT queries"""

    log = open("log.sql").read().lower()
    if "select" not in log:
        raise check50.Failure(f"missing SELECT queries in log.sql")

@check50.check(exists)
def formatting():
    """answers.txt formatted correctly"""

    # for internal purposes, all formatting and answers get checked within this function

    with open("answers.txt", "r") as f:
        answers = f.read().lower()

    with open("template.txt", "r") as f:
        # keep only the non-whitespace lines
        prefixes = filter(lambda s: not s.isspace(), f.readlines())

    hexes = [
        "322066696E6E6967616E20737472656574",
        "7265736964656E7469616C",
        "636F6E67726174756C61746F7279206C6574746572",
        "372068756D626F6C647420706C616365",
        "706F6C6963652073746174696F6E",
        "6475636B206465627567676572",
        "6D696B656C"
    ]

    # the upshot of all this; a list of tuples, where each tuple
    # represents the prefix (e.g. 'The Lost Letter belongs to: ')
    # and the hex (the 'ciphered' solution that should follow the colon)
    solutions = list(zip(prefixes, hexes))

    # store answers in results
    for prefix, hex in solutions:
        results.append(check_answer(prefix, hex, answers))

    # check formatting
    for prefix, _ in solutions:
        if not check_answer(prefix, None, answers):
            raise check50.Failure("invalid answers.txt formatting")

@check50.check(formatting)
def test1():
    """Lost Letter located"""

    if not results[0]:
        raise check50.Failure("wrong location for Lost Letter")

@check50.check(formatting)
def test2():
    """Lost Letter location type found"""

    if not results[1]:
        raise check50.Failure("wrong type for Lost Letter location")

@check50.check(formatting)
def test3():
    """Lost Letter contents discovered"""

    if not results[2]:
        raise check50.Failure("wrong contents for Lost Letter")

@check50.check(formatting)
def test4():
    """Devious Delivery located"""

    if not results[3]:
        raise check50.Failure("wrong location for Devious Delivery")

@check50.check(formatting)
def test5():
    """Devious Delivery location type found"""

    if not results[4]:
        raise check50.Failure("wrong type for Devious Delivery location")

@check50.check(formatting)
def test6():
    """Devious Delivery contents discovered"""

    if not results[5]:
        raise check50.Failure("wrong contents for Devious Delivery")

@check50.check(formatting)
def test7():
    """Forgotten Gift tracked down"""

    if not results[6]:
        raise check50.Failure("wrong possessor for Forgotten Gift")


def check_answer(prefix, hex, answers):
    """
    Check answers.txt for the correct answer via regular expressions.

    Args:
        prefix (str): the text up to and including the colon.
            an example is 'The Lost Letter was located at: '
        hex (str): the answer in hexadecimal.
            set to None if only looking to check formatting.
        answers (str): answers.txt as a string, converted to lowercase.

    Returns:
        (bool) whether answers.txt contains the correct answer as indicated in hex.
    """

    try:
        # permits any amount of whitespace between words,
        # and keeps the colon optional
        regex = "\s*".join(prefix.lower().split()) + "?\s*"

        # add decoded hex if hex exists; otherwise, just checking formatting
        if hex:
            regex += bytes.fromhex(hex).decode("utf-8")

        return bool(re.search(regex, answers))
    except Exception as e:
        raise check50.Failure(f"Error when checking answers.txt: {str(e)}")
