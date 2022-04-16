import check50
from re import escape


@check50.check()
def exists():
    """coke.py exists"""
    check50.exists("coke.py")


@check50.check(exists)
def test_25():
    """coke accepts 25 cents"""
    input = "25"
    output = "25"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_10():
    """coke accepts 10 cents"""
    input = "10"
    output = "40"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_1():
    """coke accepts 5 cents"""
    input = "5"
    output = "45"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(exists)
def test_invalid():
    """coke rejects invalid amount of cents"""
    input = "30"
    output = "50"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(test_10)
def test_multiple():
    """coke accepts continued input"""
    input = "10"
    output = "30"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).kill()


@check50.check(test_25)
def test_terminate():
    """coke terminates at 50 cents"""
    input = "25"
    output = "0"
    check50.run("python3 coke.py").stdin(input, prompt=True).stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^[^\d]*{escape(text)}[^\d]*$'