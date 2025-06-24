import check50
from re import escape


@check50.check()
def exists():
    """game.py exists"""
    check50.exists("game.py")

    # The hard-coded number 4 is the answer to the game (specified in test.py).
    # This is the number that the user is trying to guess.
    check50.include("testing.py")


@check50.check(exists)
def test_string_level():
    """game.py rejects non-numeric level"""
    check50.run("python3 game.py").stdin("cat", prompt=True).stdout(
        regex("Level"), "Level:"
    ).kill()


@check50.check(exists)
def test_integer_level():
    """game.py rejects out-of-range level"""
    check50.run("python3 game.py").stdin("0", prompt=True).stdout(
        regex("Level"), "Level:"
    ).kill()


@check50.check(exists)
def test_valid_level():
    """game.py accepts valid level"""
    check50.run("python3 game.py").stdin("10", prompt=True).stdout(
        regex("Guess"), "Guess:", regex=True
    ).kill()


@check50.check(test_valid_level)
def test_string_guess():
    """game.py rejects nonnumeric guess"""
    check50.run("python3 game.py").stdin("1", prompt=True).stdin(
        "cat", prompt=True
    ).reject()


@check50.check(test_valid_level)
def test_out_of_range_large():
    """game.py rejects guess above specified range with \"Too large!\""""
    output = "Too large!"
    check50.run("python3 testing.py").stdin("4", prompt=True).stdin(
        "8", prompt=True
    ).stdout(regex(output), output, regex=True).reject()
    

@check50.check(test_valid_level)
def test_nonpositive_guess():
    """game.py rejects nonpositive guess"""
    check50.run("python3 game.py").stdin("1", prompt=True).stdin(
        "0", prompt=True
    ).stdout(reject_regex("Guess"), "Guess:").kill()
    check50.run("python3 game.py").stdin("50", prompt=True).stdin(
        "-50", prompt=True
    ).stdout(reject_regex("Guess"), "Guess:").kill()


@check50.check(test_valid_level)
def test_too_large():
    """game.py outputs \"Too large!\" when guess is too large"""
    output = "Too large!"
    check50.run("python3 testing.py").stdin("22", prompt=True).stdin(
        "18", prompt=True
    ).stdout(regex(output), output, regex=True).reject()


@check50.check(test_valid_level)
def test_just_right():
    """game.py outputs \"Just right!\" when guess is correct"""
    output = "Just right!"
    check50.run("python3 testing.py").stdin("6", prompt=True).stdin(
        "4", prompt=True
    ).stdout(regex(output), output, regex=True).exit()


@check50.check(test_valid_level)
def test_too_small():
    """game.py outputs \"Too small!\" when guess is too small"""
    output = "Too small!"
    check50.run("python3 testing.py").stdin("5", prompt=True).stdin(
        "2", prompt=True
    ).stdout(regex(output), output, regex=True).reject()


def regex(text):
    """match case-insensitively with any characters on either side"""
    return rf"(?i)^.*{escape(text)}.*$"


def reject_regex(text):
    """regex to reject if any text was printed before the expected text"""
    return rf"(?i)(?<!\n){escape(text)}"
