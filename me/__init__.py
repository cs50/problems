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
def mario():
    """responds to name Mario"""
    check_name("Mario")


@check50.check(compiles)
def peach():
    """responds to name Peach"""
    check_name("Peach")


@check50.check(compiles)
def bowser():
    """responds to name Bowser"""
    check_name("Bowser")


def check_name(name):
    # Define expected, actual outputs
    expected = f"hello, {name}\n"
    actual = check50.run("./hello").stdin(name).stdout()

    # Check output
    if not re.match(regex(name), actual):
        try:
            last_character = actual[-1]
        except IndexError:
            raise check50.Mismatch(expected=expected, actual=actual)

        if last_character != "\n":
            raise check50.Mismatch(
                expected=expected,
                actual=actual,
                help=r"Forgot to print a newline at the end of your output?",
            )
        raise check50.Mismatch(expected=expected, actual=actual)


def regex(string):
    return f"^[Hh]ello, {re.escape(string)}\n$"
