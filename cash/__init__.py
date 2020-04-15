import check50
import check50.c


@check50.check()
def exists():
    """cash.c exists"""
    check50.exists("cash.c")


@check50.check(exists)
def compiles():
    """cash.c compiles"""
    check50.c.compile("cash.c", lcs50=True)


@check50.check(compiles)
def test041():
    """input of 0.41 yields output of 4"""
    check50.run("./cash").stdin("0.41").stdout(coins(4), "4\n").exit(0)


@check50.check(compiles)
def test001():
    """input of 0.01 yields output of 1"""
    check50.run("./cash").stdin("0.01").stdout(coins(1), "1\n").exit(0)


@check50.check(compiles)
def test015():
    """input of 0.15 yields output of 2"""
    check50.run("./cash").stdin("0.15").stdout(coins(2), "2\n").exit(0)


@check50.check(compiles)
def test160():
    """input of 1.6 yields output of 7"""
    check50.run("./cash").stdin("1.6").stdout(coins(7), "7\n").exit(0)


@check50.check(compiles)
def test230():
    """input of 23 yields output of 92"""
    check50.run("./cash").stdin("23").stdout(coins(92), "92\n").exit(0)


@check50.check(compiles)
def test420():
    """input of 4.2 yields output of 18"""
    from re import search
    expected = "18\n"
    actual = check50.run("./cash").stdin("4.2").stdout()
    if not search(coins(18), actual):
        help = None
        if search(coins(22), actual):
            help = "did you forget to round your input to the nearest cent?"
        raise check50.Mismatch(expected, actual, help=help)


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
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"
