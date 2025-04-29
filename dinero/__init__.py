import check50
import check50.c


@check50.check()
def exists():
    """cash.c existe"""
    check50.exists("cash.c")


@check50.check(exists)
def compiles():
    """cash.c compila"""
    check50.c.compile("cash.c", lcs50=True)


@check50.check(compiles)
def test041():
    """la entrada de 41 produce una salida de 4"""
    check50.run("./cash").stdin("41").stdout(coins(4), "4\n").exit(0)


@check50.check(compiles)
def test001():
    """la entrada de 1 produce la salida de 1"""
    check50.run("./cash").stdin("1").stdout(coins(1), "1\n").exit(0)


@check50.check(compiles)
def test015():
    """la entrada de 15 produce la salida de 2"""
    check50.run("./cash").stdin("15").stdout(coins(2), "2\n").exit(0)


@check50.check(compiles)
def test160():
    """la entrada de 160 produce la salida de 7"""
    check50.run("./cash").stdin("160").stdout(coins(7), "7\n").exit(0)


@check50.check(compiles)
def test230():
    """la entrada de 2300 produce la salida de 92"""
    check50.run("./cash").stdin("2300").stdout(coins(92), "92\n").exit(0)


@check50.check(compiles)
def test_reject_negative():
    """rechaza una entrada negativa como -1"""
    check50.run("./cash").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rechaza una entrada no-numérica de "foo" """
    check50.run("./cash").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rechaza una entrada no-numérica de "" """
    check50.run("./cash").stdin("").reject()


def coins(num):
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"
