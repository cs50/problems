import check50
import check50.c

@check50.check()
def exists():
    """credit.c exists"""
    check50.exists("credit.c")

@check50.check(exists)
def compiles():
    """credit.c compiles"""
    check50.c.compile("credit.c", lcs50=True)

@check50.check(compiles)
def test1():
    """identifies 378282246310005 as AMEX"""
    check50.run("./credit").stdin("378282246310005").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test2():
    """identifies 371449635398431 as AMEX"""
    check50.run("./credit").stdin("371449635398431").stdout("AMEX\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test3():
    """identifies 5555555555554444 as MASTERCARD"""
    check50.run("./credit").stdin("5555555555554444").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test4():
    """identifies 5105105105105100 as MASTERCARD"""
    check50.run("./credit").stdin("5105105105105100").stdout("MASTERCARD\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test5():
    """identifies 4111111111111111 as VISA"""
    check50.run("./credit").stdin("4111111111111111").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test6():
    """identifies 4012888888881881 as VISA"""
    check50.run("./credit").stdin("4012888888881881").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test7():
    """identifies 4222222222222 as VISA"""
    check50.run("./credit").stdin("4222222222222").stdout("VISA\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test8():
    """identifies 1234567890 as INVALID (invalid length, checksum, identifying digits)"""
    check50.run("./credit").stdin("1234567890").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test9():
    """identifies 369421438430814 as INVALID (invalid identifying digits)"""
    check50.run("./credit").stdin("369421438430814").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test10():
    """identifies 4062901840 as INVALID (invalid length)"""
    check50.run("./credit").stdin("4062901840").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test11():
    """identifies 5673598276138003 as INVALID (invalid identifying digits)"""
    check50.run("./credit").stdin("5673598276138003").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test12():
    """identifies 4111111111111113 as INVALID (invalid checksum)"""
    check50.run("./credit").stdin("4111111111111113").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test13():
    """identifies 4222222222223 as INVALID (invalid checksum)"""
    check50.run("./credit").stdin("4222222222223").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test14():
    """identifies 3400000000000620 as INVALID (AMEX identifying digits, VISA/Mastercard length)"""
    check50.run("./credit").stdin("3400000000000620").stdout("INVALID\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def test15():
    """identifies 430000000000000 as INVALID (VISA identifying digits, AMEX length)"""
    check50.run("./credit").stdin("430000000000000").stdout("INVALID\n").stdout(check50.EOF).exit(0)
