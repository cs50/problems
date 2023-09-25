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
def test_thumbsup_alias():
    """input of \":thumbsup:\" yields output of 👍"""
    input = ":thumbsup:"
    output = "👍"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_alias_in_phrase():
    """input of \"hello, :earth_asia:\" yields output of hello, 🌏"""
    input = "hello, :earth_asia:"
    output = "hello, 🌏"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_multiple():
    """input of \":candy: or :ice_cream:?\" yields output of 🍬 or 🍨?"""
    input = ":candy: or :ice_cream:?"
    output = "🍬 or 🍨?"
    check50.run("python3 emojize.py").stdin(input, prompt=False).stdout(regex(output), output, regex=True).exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'
