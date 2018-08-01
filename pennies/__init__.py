import check50
import check50.c

@check50.check()
def exists():
    """pennies.c exists"""
    check50.exists("pennies.c")

@check50.check(exists)
def compiles():
    """pennies.c compiles"""
    check50.c.compile("pennies.c", lcs50=True)

@check50.check(compiles)
def test28days1penny():
    """28 days, 1 penny on day one yields $2684354.55"""
    check50.run("./pennies").stdin("28").stdin("1").stdout("$2684354.55\n", regex=False).exit(0)

@check50.check(compiles)
def test31days1penny():
    """31 days, 1 penny on day one yields $21474836.47"""
    check50.run("./pennies").stdin("31").stdin("1").stdout("\$21474836.47\n", regex=False).exit(0)

@check50.check(compiles)
def test29days2pennies():
    """29 days, 2 pennies on day one yields $10737418.22"""
    check50.run("./pennies").stdin("29").stdin("2").stdout("\$10737418.22\n", regex=False).exit(0)

@check50.check(compiles)
def test30days30pennies():
    """30 days, 30 pennies on day one yields $322122546.90"""
    check50.run("./pennies").stdin("30").stdin("30").stdout("\$322122546.90\n", regex=False).exit(0)

@check50.check(compiles)
def test_invalid_days():
    """rejects days < 28 or > 31"""
    check50.run("./pennies").stdin("-8").reject().stdin("35").reject().stdin("1").reject()

@check50.check(compiles)
def test_negative_pennies():
    """rejects pennies < 1"""
    check50.run("./pennies").stdin("31").stdin("-10").reject().stdin("0").reject()

@check50.check(compiles)
def test_reject_foo_days():
    """rejects days == "foo" """
    check50.run("./pennies").stdin("foo").reject()

@check50.check(compiles)
def test_reject_foo_pennies():
    """rejects pennies == "foo" """
    check50.run("./pennies").stdin("30").stdin("foo").reject()

@check50.check(compiles)
def test_reject_empty_string_days():
    """rejects a non-numeric input of "" for days """
    check50.run("./pennies").stdin("").reject()

@check50.check(compiles)
def test_reject_empty_string_pennies():
    """rejects a non-numeric input of "" for pennies """
    check50.run("./pennies").stdin("30").stdin("").reject()
