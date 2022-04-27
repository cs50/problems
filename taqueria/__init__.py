import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """taqueria.py exists"""
    check50.exists("taqueria.py")


@check50.check(exists)
def test_EOF():
    """input of EOF halts program"""
    check50.run("python3 taqueria.py").stdin(EOF, prompt=False).exit(0)


@check50.check(test_EOF)
def test_basic_order():
    """input of \"taco\", \"taco\", and \"tortilla salad\" results in $14.00"""
    items = ["taco", "taco", "tortilla salad"]
    output = 14.0
    check50.run("python3 taqueria.py").stdin(items[0], prompt=True).stdin(items[1], prompt=True).stdin(items[2], prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(test_EOF)
def test_basic_order_2():
    """input of \"burrito\", \"bowl\", and \"nachos\" results in $27.00"""
    items = ["burrito", "bowl", "nachos"]
    output = 27.0
    check50.run("python3 taqueria.py").stdin(items[0], prompt=True).stdin(items[1], prompt=True).stdin(items[2], prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(test_EOF)
def test_basic_order_3():
    """input of \"Baja Taco\", \"Quesadilla\", and \"Super Burrito\" results in $21.00"""
    items = ["Baja Taco", "Quesadilla", "Super Burrito"]
    output = 21.0
    check50.run("python3 taqueria.py").stdin(items[0], prompt=True).stdin(items[1], prompt=True).stdin(items[2], prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(test_EOF)
def test_capitalization():
    """input of \"Super quesadilla\" results in $9.50"""
    input = "Super quesadilla"
    output = 9.50
    check50.run("python3 taqueria.py").stdin(input, prompt=True).stdout(regex(f"{output:.2f}"), f"${output:.2f}", regex=True).kill()


@check50.check(test_EOF)
def test_invalid_order():
    """input of \"burger\" results in reprompt"""
    input = "burger"
    check50.run("python3 taqueria.py").stdin(input, prompt=True).reject()


def regex(cost):
    """match case-insensitively with dollar-sign required and only characters on either side"""
    return fr'(?i)^[\D]*\${escape(cost)}[\D]*$'