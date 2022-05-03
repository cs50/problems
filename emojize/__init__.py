import check50
from re import escape


@check50.check()
def exists():
    """emojize.py exists"""
    check50.exists("emojize.py")


@check50.check(exists)
def test_first_place():
    """input of \":1st_place_medal:\" yields output of 🥇"""
    input = ":1st_place_medal:"
    output = "🥇"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_money_bag():
    """input of \":money_bag:\" yields output of 💰"""
    input = ":money_bag:"
    output = "💰"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_smile_cat():
    """input of \":smile_cat:\" yields output of 😸"""
    input = ":smile_cat:"
    output = "😸"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_smile_cat():
    """input of \":candy:\" yields output of 🍬"""
    input = ":candy:"
    output = "🍬"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'