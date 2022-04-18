import check50
from re import escape


@check50.check()
def exists():
    """twttr.py exists"""
    check50.exists("twttr.py")


@check50.check(exists)
def test_twitter():
    """input of Twitter yields output of Twttr"""
    input = "Twitter"
    output = "Twttr"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_name():
    """input of \"What's your name?\" yields output of \"Wht's yr nm?\""""
    input = "What's your name?"
    output = "Wht's yr nm?"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_cs50():
    """input of CS50 yields output of CS50"""
    input = "CS50"
    output = "CS50"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_python():
    """input of PYTHON yields output of PYTHN"""
    input = "PYTHON"
    output = "PYTHN"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'