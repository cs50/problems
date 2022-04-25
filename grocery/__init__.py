import check50
from re import escape
from pexpect import EOF


@check50.check()
def exists():
    """grocery.py exists"""
    check50.exists("grocery.py")


@check50.check(exists)
def test_EOF():
    """input of EOF halts program"""
    input = EOF
    check50.run("python3 grocery.py").stdin(input, prompt=False).exit()


@check50.check(test_EOF)
def test_single_items():
    """input of \"apple\" and \"banana\" yields \"1 APPLE 1 BANANA\""""
    items = ["apple", "banana"]
    output = "1 APPLE\n1 BANANA"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


@check50.check(test_EOF)
def test_multiple_items():
    """input of \"strawberry\" and \"strawberry\" yields \"2 STRAWBERRY\""""
    items = ["strawberry", "strawberry"]
    output = "2 STRAWBERRY"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


@check50.check(test_EOF)
def test_single_and_multiple_items():
    """input of \"mango\", \"mango\", and \"sugar\" yields \"2 MANGO 1 SUGAR\""""
    items = ["mango", "mango", "sugar"]
    output = "2 MANGO\n1 SUGAR"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(items[2], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


@check50.check(test_EOF)
def test_alphabetical():
    """input of \"tortilla\" and \"sweet potato\" yields \"1 SWEET POTATO 1 TORTILLA\""""
    items = ["tortilla", "sweet potato"]
    output = "1 SWEET POTATO\n1 TORTILLA"
    check50.run("python3 grocery.py").stdin(items[0], prompt=False).stdin(items[1], prompt=False).stdin(EOF, prompt=False).stdout(regex(output), output, regex=True).exit()


def regex(items):
    """match case-sensitively with only whitespace on either side"""
    return fr'^\s*{escape(items)}\s*$'