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

def _test_credit_card(card_number, expected_output):
    """Helper function to test credit card validation with proper error handling"""
    try:
        check50.run("./credit").stdin(card_number).stdout(expected_output).stdout(check50.EOF).exit(0)
    except check50.Missing as e:
        raise check50.Failure("Program did not exit after processing input.")

@check50.check(compiles)
def test1():
    """identifies 378282246310005 as AMEX"""
    _test_credit_card("378282246310005", "AMEX\n")

@check50.check(compiles)
def test2():
    """identifies 371449635398431 as AMEX"""
    _test_credit_card("371449635398431", "AMEX\n")

@check50.check(compiles)
def test3():
    """identifies 5555555555554444 as MASTERCARD"""
    _test_credit_card("5555555555554444", "MASTERCARD\n")

@check50.check(compiles)
def test4():
    """identifies 5105105105105100 as MASTERCARD"""
    _test_credit_card("5105105105105100", "MASTERCARD\n")

@check50.check(compiles)
def test5():
    """identifies 4111111111111111 as VISA"""
    _test_credit_card("4111111111111111", "VISA\n")

@check50.check(compiles)
def test6():
    """identifies 4012888888881881 as VISA"""
    _test_credit_card("4012888888881881", "VISA\n")

@check50.check(compiles)
def test7():
    """identifies 4222222222222 as VISA"""
    _test_credit_card("4222222222222", "VISA\n")

@check50.check(compiles)
def test8():
    """identifies 1234567890 as INVALID (invalid length, checksum, identifying digits)"""
    _test_credit_card("1234567890", "INVALID\n")

@check50.check(compiles)
def test9():
    """identifies 369421438430814 as INVALID (invalid identifying digits)"""
    _test_credit_card("369421438430814", "INVALID\n")

@check50.check(compiles)
def test10():
    """identifies 4062901840 as INVALID (invalid length)"""
    _test_credit_card("4062901840", "INVALID\n")

@check50.check(compiles)
def test11():
    """identifies 5673598276138003 as INVALID (invalid identifying digits)"""
    _test_credit_card("5673598276138003", "INVALID\n")

@check50.check(compiles)
def test12():
    """identifies 4111111111111113 as INVALID (invalid checksum)"""
    _test_credit_card("4111111111111113", "INVALID\n")

@check50.check(compiles)
def test13():
    """identifies 4222222222223 as INVALID (invalid checksum)"""
    _test_credit_card("4222222222223", "INVALID\n")

@check50.check(compiles)
def test14():
    """identifies 3400000000000620 as INVALID (AMEX identifying digits, VISA/Mastercard length)"""
    _test_credit_card("3400000000000620", "INVALID\n")

@check50.check(compiles)
def test15():
    """identifies 430000000000000 as INVALID (VISA identifying digits, AMEX length)"""
    _test_credit_card("430000000000000", "INVALID\n")
