import check50
import check50.c

@check50.check()
def exists():
    """fahrenheit.c exists"""
    check50.exists("fahrenheit.c")

@check50.check(exists)
def compiles():
    """fahrenheit.c compiles"""
    check50.c.compile("fahrenheit.c", lcs50=True)

@check50.check(compiles)
def test37():
    """37 degrees Celsius yields 98.6 degrees Fahrenheit"""
    check50.run("./fahrenheit 37").stdout(number(98.6), "98.6\n").exit(0)

@check50.check(compiles)
def test0():
    """0 degrees Celsius yields 32.0 degrees Fahrenheit"""
    check50.run("./fahrenheit 0").stdout(number(32.0), "32.0\n").exit(0)

@check50.check(compiles)
def test100point00():
    """100.00 degrees Celsius yields 212.0 degrees Fahrenheit"""
    check50.run("./fahrenheit 100.00").stdout(number(212.0), "212.0\n").exit(0)

@check50.check(compiles)
def testneg40():
    """-40 degrees Celsius yields -40.0 degrees Fahrenheit"""
    check50.run("./fahrenheit -40").stdout(number(-40.0), "-40.0\n").exit(0)

@check50.check(compiles)
def test_lack_of_arguments():
    """handles lack of command line arguments"""
    check50.run("./fahrenheit").exit(1)

@check50.check(compiles)
def test_too_many_arguments():
    """handles too many command line arguments"""
    check50.run("./fahrenheit 0 32").exit(1)

def number(num):
    n = num.replace('.', '\\.')
    return fr"(?<!\d){n}(?!\d)"
