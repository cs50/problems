import check50
import check50.c

@check50.check()
def exists():
    """calc.c exists"""
    check50.exists("calc.c")

@check50.check(exists)
def compiles():
    """calc.c compiles"""
    check50.c.compile("calc.c", lcs50=True)

@check50.check(compiles)
def test_handles_addition():
    """calculator handles addition"""
    check50.run("./calc 3 + 4").stdout(number("7.000000"), "7.000000\n").exit(0)

@check50.check(compiles)
def test_handles_subtraction():
    """calculator handles subtraction"""
    check50.run("./calc 10.5 - 6.2").stdout(number("4.300000"), "4.300000\n").exit(0)

@check50.check(compiles)
def test_handles_division():
    """calculator handles division"""
    check50.run("./calc 41.48 / -8.44").stdout(number(-4.914692), "-4.914692\n").exit(0)

@check50.check(compiles)
def test_handles_multiplication_with_x():
    """calculator handles multiplication with "x" """
    check50.run("./calc 11.1 x 9").stdout(number(99.900002),"99.900002\n").exit(0)

@check50.check(compiles)
def test_handles_modulo():
    """calculator handles modulo of integers"""
    check50.run("./calc 8 % 5").stdout(number("3.000000"), "3.000000\n").exit(0)

@check50.check(compiles)
def test_handles_modulo2():
    """calculator handles modulo of real numbers"""
    check50.run("./calc 8.1 % 4.9").stdout(number("3.200000"), "3.200000\n").exit(0)

@check50.check(compiles)
def test_handles_bad_operation():
    """handles invalid operation"""
    check50.run("./calc 11 J 8").exit(1)

@check50.check(compiles)
def test_argc_1():
    """handles lack of command line arguments"""
    check50.run("./calc").exit(1)

@check50.check(compiles)
def test_argc_5():
    """handles too many command line arguments"""
    check50.run("./calc 11.1 + 23 9").exit(1)

def number(num):
    return fr"(?<!\d){num}(?!\d)"
