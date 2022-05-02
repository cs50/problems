import check50
from re import escape, match


@check50.check()
def exists():
    """game.py exists"""
    check50.exists("game.py")


@check50.check(exists)
def test_string_level():
    """game.py rejects non-numeric level"""
    check50.run("python3 game.py").stdin("cat", prompt=True).reject()


@check50.check(exists)
def test_integer_level():
    """game.py rejects out-of-range level"""
    check50.run("python3 game.py").stdin("0", prompt=True).reject()
    check50.run("python3 game.py").stdin("-50", prompt=True).reject()


@check50.check(exists)
def test_valid_level():
    """game.py accepts valid level"""
    check50.run("python3 game.py").stdin("10", prompt=True).stdout(regex("Guess"), "Guess:", regex=True).kill()


@check50.check(test_valid_level)
def test_string_guess():
    """game.py rejects non-numeric guess"""
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("cat", prompt=True).reject()


@check50.check(test_valid_level)
def test_integer_guess():
    """game.py rejects out-of-range guess"""
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("0", prompt=True).reject()
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("-50", prompt=True).reject()


@check50.check(test_valid_level)
def test_too_large():
    """game.py outputs \"Too large!\" when guess is too large"""
    output = "Too large!"
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("100", prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(test_valid_level)
def test_just_right():
    """game.py outputs \"Just right!\" when guess is correct"""
    output = "Just right!"
    check50.run("python3 game.py").stdin("1", prompt=True).stdin("1", prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(test_valid_level)
def test_too_small():
    """game.py outputs \"Too small!\" when guess is too low"""

    # Run program
    program = check50.run("python3 game.py")

    # Set range to 1–1000
    program.stdin("1000000000", prompt=True)

    # Guess 1
    program.stdin("1", prompt=True).stdout(regex("Too small!"), "Too small!", regex=True).kill()


def regex(text):
    """match case-sensitively with any characters on either side"""
    return fr'(?i)^.*{escape(text)}.*$'