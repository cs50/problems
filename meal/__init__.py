import check50
from re import escape


@check50.check()
def exists():
    """meal.py exists"""
    check50.exists("meal.py")


@check50.check(exists)
def test_breakfast():
    """input of 7:00 yields output of \"breakfast time\""""
    input = "7:00"
    output = "breakfast time"
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_breakfast2():
    """input of 7:30 yields output of \"breakfast time\""""
    input = "7:30"
    output = "breakfast time"
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_lunch():
    """input of 12:42 yields output of \"lunch time\""""
    input = "12:42"
    output = "lunch time"
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_lunch():
    """input of 13:00 yields output of \"lunch time\""""
    input = "13:00"
    output = "lunch time"
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_dinner():
    """input of 18:32 yields output of \"dinner time\""""
    input = "18:32"
    output = "dinner time"
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_no_output():
    """input of 11:11 yields no output"""
    input = "11:11"
    output = ""
    check50.run("python3 meal.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(time):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(time)}\s*$'