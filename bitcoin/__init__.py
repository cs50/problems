import check50
from pexpect import EOF
from re import escape
import requests
import sys


@check50.check()
def exists():
    """bitcoin.py exists"""
    check50.exists("bitcoin.py")


@check50.check()
def test_no_arguments():
    """bitcoin.py exits given no command-line argument"""
    check50.run("python3 bitcoin.py").exit(1)


@check50.check()
def test_non_numeric_argument():
    """bitcoin.py exits given non-numeric command-line argument"""
    check50.run("python3 bitcoin.py cat").exit(1)


@check50.check()
def test_single_coin():
    """bitcoin.py provides price of 1 Bitcoin to 4 decimal places"""
    coins = 1
    price = get_price(coins)
    check50.run(f"python3 bitcoin.py {coins}").stdout(regex(price), price, regex=True).exit(0)


@check50.check()
def test_two_coins():
    """bitcoin.py provides price of 2 Bitcoin to 4 decimal places"""
    coins = 2
    price = get_price(coins)
    check50.run(f"python3 bitcoin.py {coins}").stdout(regex(price), price, regex=True).exit(0)


@check50.check()
def test_decimal_coins():
    """bitcoin.py provides price of 2.5 Bitcoin to 4 decimal places"""
    coins = 2.5
    price = get_price(coins)
    check50.run(f"python3 bitcoin.py {coins}").stdout(regex(price), price, regex=True).exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'


def get_price(coins):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        price = response.json()["bpi"]["USD"]["rate_float"]
    except requests.HTTPError:
        sys.exit("check50 encountered a server error")
    return f"${coins * price:,.4f}"