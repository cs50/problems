import check50
from re import escape

price = 37817.3283


@check50.check()
def exists():
    """bitcoin.py exists"""
    check50.exists("bitcoin.py")
    check50.include("testing.py")


@check50.check(exists)
def test_no_arguments():
    """bitcoin.py exits given no command-line argument"""
    check50.run("python3 bitcoin.py").exit(1)


@check50.check(exists)
def test_non_numeric_argument():
    """bitcoin.py exits given non-numeric command-line argument"""
    check50.run("python3 bitcoin.py cat").exit(1)


@check50.check(exists)
def test_single_coin():
    """bitcoin.py provides price of 1 Bitcoin to 4 decimal places"""
    coins = 1
    amount = coins * price
    check50.run(f"python3 testing.py {coins}").stdout(regex(amount), f'${amount:,.4f}', regex=True).exit(0)


@check50.check(exists)
def test_two_coins():
    """bitcoin.py provides price of 2 Bitcoin to 4 decimal places"""
    coins = 2
    amount = coins * price
    check50.run(f"python3 testing.py {coins}").stdout(regex(amount), f'${amount:,.4f}', regex=True).exit(0)


@check50.check(exists)
def test_decimal_coins():
    """bitcoin.py provides price of 2.5 Bitcoin to 4 decimal places"""
    coins = 2.5
    amount = coins * price
    check50.run(f"python3 testing.py {coins}").stdout(regex(amount), f'${amount:,.4f}', regex=True).exit(0)


def regex(amount):
    """match case-sensitively with any characters before or after"""
    amount = f'${amount:,.4f}'
    return fr'^.*{escape(amount)}.*$'