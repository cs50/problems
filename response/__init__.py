import check50
from re import escape, search


@check50.check()
def exists():
    """response.py exists"""
    check50.exists("response.py")


@check50.check(exists)
def libraries():
    """response.py does not use re and uses either validators or validator-collection"""
    with open("response.py", "r") as file:
        contents = file.read()
        if not search(r'(?<!#)(?<! )((import[ \t]*(validators|validator_collection))|(from[ \t]*(validators|validator_collection)[ \t]*import[ \t]*[\w\*]+))', contents):
            raise check50.Failure("response.py does not import validators or validator-collection library", help="Did you forget to include \"import validators\" or \"import validator_collection\"?")
        if search(r'(?<!#)(?<! )((import[ \t]*re)|(from[ \t]*re[ \t]*import[ \t]*[\w\*]+))', contents):
            raise check50.Failure("response.py uses the re library", help="Be sure not to import functions from the re library, either via \"import re\" or via \"from re import ...\"")


@check50.check(libraries)
def test_valid_email():
    """response.py yields Valid when email address is \"malan@harvard.edu\""""
    input = "malan@harvard.edu"
    output = "Valid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(libraries)
def test_valid_email_2():
    """response.py yields Valid when email address is \"sysadmins@cs50.harvard.edu\""""
    input = "sysadmins@cs50.harvard.edu"
    output = "Valid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(libraries)
def test_invalid_email_spelled_out():
    """response.py yields Invalid when email address is \"malan at harvard dot edu\""""
    input = "malan at harvard dot edu"
    output = "Invalid"
    check50.run("python3 response.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(libraries)
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