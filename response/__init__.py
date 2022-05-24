import check50
from re import escape


@check50.check()
def exists():
    """response.py exists"""
    check50.exists("response.py")


@check50.check(exists)
def test_valid_email():
    """response.py yields Valid when email address is \"malan@harvard.edu\""""
    input = "malan@harvard.edu"
    output = "Valid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_valid_email_2():
    """response.py yields Valid when email address is \"sysadmins@cs50.harvard.edu\""""
    input = "sysadmins@cs50.harvard.edu"
    output = "Valid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)



@check50.check(exists)
def test_invalid_email_spelled_out():
    """response.py yields Invalid when email address is \"malan at harvard dot edu\""""
    input = "malan at harvard dot edu"
    output = "Invalid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_invalid_email_at_symbols():
    """response.py yields Invalid when email address is \"malan@@@harvard.edu\""""
    input = "malan@@@harvard.edu"
    output = "Invalid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


"""
Helpers
"""


def regex(text):
    """match case-insensitively, allowing for only whitespace on either side"""
    return fr'(?i)^\s*{escape(text)}\s*$'