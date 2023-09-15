import re

import check50


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
    try:
        questions = read_questions("template.txt")
    except FileNotFoundError:
        raise check50.Failure("check50 couldn't find a template answers.txt file!")

    for i in range(len(questions)):
        if not check_answer(i, formatting=True):
            raise check50.Failure("invalid answers.txt formatting")


@check50.check(formatting)
def test012():
    """Lost Letter solved"""

    for i in range(0, 3):
        if not check_answer(i):
            raise check50.Failure(
                "answers.txt does not correctly solve the Lost Letter mystery"
            )


@check50.check(formatting)
def test345():
    """Devious Delivery solved"""

    for i in range(3, 6):
        if not check_answer(i):
            raise check50.Failure(
                "answers.txt does not correctly solve the Devious Delivery mystery"
            )


@check50.check(formatting)
def test6():
    """Forgotten Gift solved"""

    if not check_answer(6):
        raise check50.Failure(
            "answers.txt does not correctly solve the Forgotten Gift mystery"
        )


def check_answer(question_no, formatting=False):
    """
    Check answers.txt for the correct answer via regular expressions.

    Args:
        question_no (int): which number question is being checked
    Optional Args:
        formatting (bool): if True, only checks formatting, not provided answer

    Returns:
        (bool) whether answers.txt contains the correct answer as indicated in hex.
    """

    # reading the whole answers/template every check is a bit silly,
    # but without ways to pass information across checks it's unclear how else to do it
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
    ]

    # the upshot of all this; a list of tuples, where each tuple
    # represents the prefix (e.g. 'The Lost Letter belongs to: ')
    # and the hex (the 'ciphered' solution that should follow the colon)
    solutions = list(zip(prefixes, hexes))

    # grab specific question from solutions
    prefix, hex = solutions[question_no]
    if formatting:
        hex = None

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


def read_questions(filename: str) -> list[str]:
    # read and keep only the non-whitespace lines
    with open(filename, "r") as f:
        return list(filter(lambda s: not s.isspace(), f.readlines()))
