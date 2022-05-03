import check50
from re import escape, match


@check50.check()
def exists():
    """game.py exists"""
    check50.exists("game.py")
    check50.include("testing.py")


@check50.check(exists)
def test_string_level():
    """game.py rejects non-numeric level"""
    check50.run("python3 testing.py").stdin("cat", prompt=True).reject()


@check50.check(exists)
def test_integer_level():
    """game.py rejects out-of-range level"""
    check50.run("python3 testing.py").stdin("0", prompt=True).reject()


@check50.check(exists)
def test_valid_level():
    """game.py accepts valid level"""
    check50.run("python3 testing.py").stdin("10", prompt=True).stdout(regex("Guess"), "Guess:", regex=True).kill()


@check50.check(test_valid_level)
def test_string_guess():
    """game.py rejects non-numeric guess"""
    check50.run("python3 testing.py").stdin("1", prompt=True).stdin("cat", prompt=True).reject()


@check50.check(test_valid_level)
def test_integer_guess():
    """game.py rejects out-of-range guess"""
    check50.run("python3 testing.py").stdin("1", prompt=True).stdin("0", prompt=True).reject()


@check50.check(test_valid_level)
def test_too_large():
    """game.py outputs \"Too large!\" when guess is too large"""
    output = "Too large!"
    check50.run("python3 testing.py").stdin("5", prompt=True).stdin("5", prompt=True).stdout(regex(output), output, regex=True).reject()


@check50.check(test_valid_level)
def test_just_right():
    """game.py outputs \"Just right!\" when guess is correct"""
    output = "Just right!"
    check50.run("python3 testing.py").stdin("5", prompt=True).stdin("4", prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(test_valid_level)
def test_too_small():
    """game.py outputs \"Too small!\" when guess is too low"""
    output = "Too small!"
    check50.run("python3 testing.py").stdin("5", prompt=True).stdin("2", prompt=True).stdout(regex(output), output, regex=True).reject()


def regex(text):
    """match case-sensitively with any characters on either side"""
    return fr'(?i)^.*{escape(text)}.*$'