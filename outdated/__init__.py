import check50
from re import escape


@check50.check()
def exists():
    """outdated.py exists"""
    check50.exists("outdated.py")


@check50.check(exists)
def test_harvard_digits():
    """input of 9/8/1636 outputs 1636-09-08"""
    input = "9/8/1636"
    output = "1636-09-08"
    check50.run("python3 outdated.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_harvard_characters():
    """input of September 8, 1636 outputs 1636-09-08"""
    input = "September 8, 1636"
    output = "1636-09-08"
    check50.run("python3 outdated.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_yale_digits():
    """input of 10/9/1701 outputs 1701-10-09"""
    input = "10/9/1701"
    output = "1701-10-09"
    check50.run("python3 outdated.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_yale_characters():
    """input of October 9, 1701 outputs 1701-10-09"""
    input = "October 9, 1701"
    output = "1701-10-09"
    check50.run("python3 outdated.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_extra_spaces():
    """input of \" 9/8/1636 \" outputs 1636-09-08"""
    input = " 9/8/1636 "
    output = "1636-09-08"
    check50.run("python3 outdated.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_out_of_range_month():
    """input of 23/6/1912 results in reprompt"""
    input = "23/6/1912"
    check50.run("python3 outdated.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_out_of_order_char():
    """input of 10 December, 1815 results in reprompt"""
    input = "10 December, 1815"
    check50.run("python3 outdated.py").stdin(input, prompt=True).reject()

    
@check50.check(exists)
def test_incorrect_format():
    """input of October/9/1701 results in reprompt"""
    input = "October/9/1701"
    check50.run("python3 outdated.py").stdin(input, prompt=True).reject()
    
    
@check50.check(exists)
def test_out_of_range_day():
    """input of 1/50/2000 results in reprompt"""
    input = "1/50/2000"
    check50.run("python3 outdated.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_out_of_range_day_char():
    """input of December 80, 1980 results in reprompt"""
    input = "December 80, 1980"
    check50.run("python3 outdated.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_no_comma():
    """input of September 8 1636 results in reprompt"""
    input = "September 8 1636"
    check50.run("python3 outdated.py").stdin(input, prompt=True).reject()


def regex(items):
    """match case-sensitively with only whitespace on either side"""
    return fr'^\s*{escape(items)}\s*$'
