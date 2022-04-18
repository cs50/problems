import check50
from re import escape


@check50.check()
def exists():
    """camel.py exists"""
    check50.exists("camel.py")


@check50.check(exists)
def test_name():
    """input of \"name\" yields output of \"name\""""
    input = "name"
    output = "name"
    check50.run("python3 camel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_firstName():
    """input of \"firstName\" yields output of \"first_name\""""
    input = "firstName"
    output = "first_name"
    check50.run("python3 camel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_preferredFirstName():
    """input of \"preferredFirstName\" yields output of \"preferred_first_name\""""
    input = "preferredFirstName"
    output = "preferred_first_name"
    check50.run("python3 camel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-sensitively, allowing for characters on either side."""
    return fr'^.*{escape(text)}.*$'