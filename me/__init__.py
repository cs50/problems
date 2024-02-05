import check50
import check50.c
import re


@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")


@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)


@check50.check(compiles)
def emma():
    """responds to name Mario"""
    check_name("Mario")


@check50.check(compiles)
def inno():
    """responds to name Peach"""
    check_name("Peach")


@check50.check(compiles)
def kamryn():
    """responds to name Bowser"""
    check_name("Bowser")


def check_name(name):
    # Define expected, actual outputs
    expected = f"hello, {name}\n"
    actual = check50.run("./hello").stdin(name).stdout()

    # Check output
    if not re.match(regex(name), actual):
        if actual[-1] != "\n":
            raise check50.Mismatch(
                expected=expected,
                actual=actual,
                help=r"Forgot to print a newline at the end of your output?",
            )
        raise check50.Mismatch(expected=expected, actual=actual)


def regex(string):
    return f"^[Hh]ello, {re.escape(string)}\n$"
