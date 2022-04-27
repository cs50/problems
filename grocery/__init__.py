import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """grocery.py exists"""
    check50.exists("grocery.py")


@check50.check(exists)
def test_EOF():
    """input of EOF halts program"""
    check50.run("python3 grocery.py").stdin(EOF, prompt=False).exit(0)


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
    """input of \"mango\", \"sugar\", and \"mango\" yields \"2 MANGO 1 SUGAR\""""
    items = ["mango", "sugar", "mango"]
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