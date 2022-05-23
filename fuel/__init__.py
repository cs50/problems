import check50
from re import escape


@check50.check()
def exists():
    """fuel.py exists"""
    check50.exists("fuel.py")


@check50.check(exists)
def test_3_over_4():
    """input of 3/4 yields output of 75%"""
    input = "3/4"
    output = "75%"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_round_down():
    """input of 1/3 yields output of 33%"""
    input = "1/3"
    output = "33%"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_round_up():
    """input of 2/3 yields output of 67%"""
    input = "2/3"
    output = "67%"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_empty():
    """input of 0/100 yields output of E"""
    input = "0/100"
    output = "E"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_almost_empty():
    """input of 1/100 yields output of E"""
    input = "1/100"
    output = "E"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_full():
    """input of 100/100 yields output of F"""
    input = "100/100"
    output = "F"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_almost_full():
    """input of 99/100 yields output of F"""
    input = "99/100"
    output = "F"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_ZeroDivisionError():
    """input of 100/0 results in reprompt"""
    input = "100/0"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_numerator_greater_than_denominator():
    """input of 10/3 results in reprompt"""
    input = "10/3"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_str_conversion():
    """input of three/four results in reprompt"""
    input = "three/four"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_float_numerator():
    """input of 1.5/4 results in reprompt"""
    input = "1.5/4"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_float_denominator():
    """input of 3/5.5 results in reprompt"""
    input = "3/5.5"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_no_slash():
    """input of 5-10 results in reprompt"""
    input = "5-10"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


def regex(percent):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(percent)}\s*$'