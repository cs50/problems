import check50
import check50.c


@check50.check()
def exists():
    """cash exists"""
    check50.exists("cash.c")


@check50.check(exists)
def compiles():
    """cash compiles"""
    check50.c.compile("cash.c", lcs50=True)


@check50.check(compiles)
def test041():
    """input of 0.41 yields output of 4"""
    check50.run("./cash").stdin("0.41").stdout("^4\n").exit(0)


@check50.check(compiles)
def test001():
    """input of 0.01 yields output of 1"""
    check50.run("./cash").stdin("0.01").stdout("^1\n").exit(0)


@check50.check(compiles)
def test015():
    """input of 0.15 yields output of 2"""
    check50.run("./cash").stdin("0.15").stdout("^2\n").exit(0)


@check50.check(compiles)
def test160():
    """input of 1.6 yields output of 7"""
    check50.run("./cash").stdin("1.6").stdout("^7\n").exit(0)


@check50.check(compiles)
def test230():
    """input of 23 yields output of 92"""
    check50.run("./cash").stdin("23").stdout("^92\n").exit(0)


@check50.check(compiles)
def test420():
    """input of 4.2 yields output of 18"""
    expected = "18\n"
    actual = check50.run("./cash").stdin("4.2").stdout()
    if not re.search("^18\n", actual):
        if re.search("^22\n", actual):
            help = "Did you forget to round your input to the nearest cent?"
        else:
            help = None
        raise Mismatch(expected, actual, help=help)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./cash").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./cash").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./cash").stdin("").reject()


def coins(num):
    return fr"(^|[^\d]){num}(?!\d)"
