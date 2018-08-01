from check50 import *

class Fahrenheit(Checks):

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
        check50.run("./fahrenheit").stdin("37").stdout(number(98.6), "98.6\n").exit(0)

    @check50.check(compiles)
    def test0():
        """0 degrees Celsius yields 32.0 degrees Fahrenheit"""
        check50.run("./fahrenheit").stdin("0").stdout(number(32.0), "32.0\n").exit(0)

    @check50.check(compiles)
    def test100():
        """100.00 degrees Celsius yields 212.0 degrees Fahrenheit"""
        check50.run("./fahrenheit").stdin("100.00").stdout(number(212.0), "212.0\n").exit(0)

    @check50.check(compiles)
    def testneg40():
        """-40 degrees Celsius yields -40.0 degrees Fahrenheit"""
        check50.run("./fahrenheit").stdin("-40").stdout(number(-40.0), "-40.0\n").exit(0)

    @check50.check(compiles)
    def test18point5():
        """18.5 degrees Celsius yields 65.3 degrees Fahrenheit"""
        check50.run("./fahrenheit").stdin("18.5").stdout(number(65.3), "65.3\n").exit(0)

    @check50.check(compiles)
    def testneg123point45678():
        """-123.45678 degrees Celsius yields -190.2 degrees Fahrenheit"""
        check50.run("./fahrenheit").stdin("-123.45678").stdout(number(-190.2), "-190.2\n").exit(0)

    @check50.check(compiles)
    def test_reject_foo():
        """rejects a non-numeric input of "foo" """
        check50.run("./fahrenheit").stdin("foo").reject()

    @check50.check(compiles)
    def test_reject_empty_string():
        """rejects a non-numeric input of "" """
        check50.run("./fahrenheit").stdin("").reject()

def number(num):
    return "(^|[^\d]){}[^\d]".format(num)
