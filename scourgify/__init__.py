import check50
from re import escape


@check50.check()
def exists():
    """scourgify.py exists"""
    check50.exists("scourgify.py")


@check50.check()
def test_no_arguments():
    """scourgify.py exits given no command-line arguments"""
    check50.run("python3 scourgify.py").exit(1)


@check50.check()
def test_too_few_arguments():
    """scourgify.py exits given too few command-line arguments"""
    check50.run("python3 scourgify.py 1.csv").exit(1)


@check50.check()
def test_too_many_arguments():
    """scourgify.py exits given too many command-line arguments"""
    check50.run("python3 scourgify.py 1.csv 2.csv 3.csv").exit(1)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'