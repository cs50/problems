import check50

@check50.check()
def exists():
    """credit.py exists."""
    check50.exists("credit.py")

@check50.check(exists)
def test1():
    """identifies 378282246310005 as AMEX"""
    check50.run("python3 credit.py").stdin("378282246310005").stdout("AMEX\n").exit(0)

@check50.check(exists)
def test2():
    """identifies 371449635398431 as AMEX"""
    check50.run("python3 credit.py").stdin("371449635398431").stdout("AMEX\n").exit(0)

@check50.check(exists)
def test3():
    """identifies 5555555555554444 as MASTERCARD"""
    check50.run("python3 credit.py").stdin("5555555555554444").stdout("MASTERCARD\n").exit(0)

@check50.check(exists)
def test4():
    """identifies 5105105105105100 as MASTERCARD"""
    check50.run("python3 credit.py").stdin("5105105105105100").stdout("MASTERCARD\n").exit(0)

@check50.check(exists)
def test5():
    """identifies 4111111111111111 as VISA"""
    check50.run("python3 credit.py").stdin("4111111111111111").stdout("VISA\n").exit(0)

@check50.check(exists)
def test6():
    """identifies 4012888888881881 as VISA"""
    check50.run("python3 credit.py").stdin("4012888888881881").stdout("VISA\n").exit(0)

@check50.check(exists)
def test7():
    """identifies 1234567890 as INVALID"""
    check50.run("python3 credit.py").stdin("1234567890").stdout("INVALID\n").exit(0)

@check50.check(exists)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("python3 credit.py").stdin("foo").reject()

@check50.check(exists)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("python3 credit.py").stdin("").reject()
