import check50
import check50.c

@check50.check()
def exists():
    """pennies.c exist"""
    check50.exists("pennies.c")

@check50.check(exists)
def compiles():
    """pennies.c compiles"""
    check50.c.compile("pennies.c", lcs50=True)

@check50.check(compiles)
def test28days1penny():
    """28 days, 1 penny on day one yields $2684354.55 """
    check50.run("./pennies 28 1").stdout("$2684354.55\n", regex=False).exit(0)

@check50.check(compiles)
def test29days2pennies():
    """29 days, 2 pennies on day one yields $10737418.22"""
    check50.run("./pennies 29 2").stdout("$10737418.22\n", regex=False).exit(0)

@check50.check(compiles)
def test30days30pennies():
    """30 days, 30 pennies on day one yields $322122546.90"""
    check50.run("./pennies 30 30").stdout("$322122546.90\n", regex=False).exit(0)

@check50.check(compiles)
def test31days1penny():
    """31 days, 1 penny on day one yields $21474836.47"""
    check50.run("./pennies 31 1").stdout("$21474836.47\n", regex=False).exit(0)

@check50.check(compiles)
def test_rejects_invalid_days():
    """rejects days < 28 or > 31"""
    check50.run("./pennies 25 1").exit(1)

@check50.check(compiles)
def test_rejects_invalid_pennies():
    """rejects pennies < 1"""
    check50.run("./pennies 30 -10").exit(1)

@check50.check(compiles)
def test_lack_of_arguments():
    """handles lack of command line arguments"""
    check50.run("./pennies").exit(1)

@check50.check(compiles)
def test_too_many_arguments():
    """handles too many command line arguments"""
    check50.run("./pennies 28 35 42").exit(1)
