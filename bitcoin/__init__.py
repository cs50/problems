import random
import re

import check50

# Price (in USD) of 1 Bitcoin that check50's simulated CoinCap API returns.
# Deliberately different from the sample response in the problem's spec, so
# that students can't mistake the sample for the price check50 uses.
#
# If you change this value:
#   - keep the docstrings below in sync with it, and
#   - keep exactly 4 decimal places with an EVEN last digit, so that the
#     2.5-coin check's exact cost has at most 4 decimals and float vs. Decimal
#     arithmetic in students' programs can't round differently.
PRICE = "65432.1098"


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
    """bitcoin.py outputs $65,432.1098 for 1 Bitcoin when API's priceUsd is 65432.1098"""
    check_cost(coins=1, price=PRICE)


@check50.check(exists)
def test_two_coins():
    """bitcoin.py outputs $130,864.2196 for 2 Bitcoin when API's priceUsd is 65432.1098"""
    check_cost(coins=2, price=PRICE)


@check50.check(exists)
def test_decimal_coins():
    """bitcoin.py outputs $163,580.2745 for 2.5 Bitcoin when API's priceUsd is 65432.1098"""
    check_cost(coins=2.5, price=PRICE)


@check50.check(exists)
def test_random_price():
    """bitcoin.py outputs correct cost when API's priceUsd is a random value"""
    # Price has exactly 4 decimals and the coin count is an integer, so the
    # exact cost has at most 4 decimals and no rounding ambiguity is possible.
    dollars = random.randint(10_000, 150_000)
    cents = random.randint(0, 9_999)
    check_cost(coins=random.randint(3, 9), price=f"{dollars}.{cents:04d}")


def check_cost(coins, price):
    """
    Run bitcoin.py via testing.py, which simulates a CoinCap API response whose
    priceUsd is `price`, and ensure the output includes the cost of `coins` Bitcoin.
    """
    expected = cost(coins, price)
    check50.log(f'simulating API response with "priceUsd": "{price}"')
    check50.log(f"expecting output to include {expected} for {coins} Bitcoin")

    proc = check50.run(f"python3 testing.py {price} {coins}")
    actual = proc.stdout()  # waits for program to exit and records proc.exitcode

    if not contains_amount(actual, expected):
        facts = (
            f'check50 simulated an API response in which "priceUsd" was "{price}", '
            f"so {coins} Bitcoin should cost {expected}."
        )
        if price != PRICE and contains_amount(actual, cost(coins, PRICE)):
            # Output matches the price used by the other checks, not this one
            hint = (
                f"Your program output the cost at a price of {PRICE} even though the "
                f"API's response said {price}. Be sure to compute the cost using the "
                "price in the API's response rather than a hardcoded value."
            )
        elif proc.exitcode != 0:
            hint = (
                f"Your program exited with status {proc.exitcode} before outputting "
                "that cost, which usually means it raised an error. Try running it "
                "yourself to see the error."
            )
        else:
            hint = (
                "Be sure to multiply the number of Bitcoin by the price in the API's "
                "response and format the result to four decimal places with a "
                "thousands separator, e.g., $1,234.5678."
            )
        raise check50.Mismatch(expected, actual.strip(), help=f"{facts} {hint}")

    if proc.exitcode != 0:
        raise check50.Failure(f"expected exit code 0, not {proc.exitcode}")


def cost(coins, price):
    """Format the cost of `coins` Bitcoin at `price` USD each, e.g., $1,234.5678"""
    return f"${coins * float(price):,.4f}"


def contains_amount(output, amount):
    """Whether `output` contains `amount` exactly, not followed by more digits"""
    return re.search(re.escape(amount) + r"(?!\d)", output) is not None
