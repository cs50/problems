import check50
from re import escape, search


@check50.check()
def exists():
    """seasons.py and test_seasons.py exists"""
    check50.exists("seasons.py")
    check50.exists("test_seasons.py")
    check50.include("testing.py")


@check50.check(exists)
def test_one_year():
    """Input of \"1999-01-01\" yields \"Five hundred twenty-five thousand, six hundred minutes\""""
    date = "1999-01-01"
    output = "Five hundred twenty-five thousand, six hundred minutes"
    check50.run("python3 testing.py").stdin(date, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_two_years():
    """Input of \"1998-01-01\" yields \"One million, fifty-one thousand, two hundred minutes\""""
    date = "1998-01-01"
    output = "One million, fifty-one thousand, two hundred minutes"
    check50.run("python3 testing.py").stdin(date, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_leap_year():
    """Input of \"1995-01-01\" yields \"Two million, six hundred twenty-nine thousand, four hundred forty minutes\""""
    date = "1995-01-01"
    output = "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    check50.run("python3 testing.py").stdin(date, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_months():
    """Input of \"1998-06-01\" yields \"Eight hundred thirty-three thousand, seven hundred sixty minutes\""""
    date = "1998-06-01"
    output = "Eight hundred thirty-three thousand, seven hundred sixty minutes"
    check50.run("python3 testing.py").stdin(date, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_day():
    """Input of \"1998-06-20\" yields \"Eight hundred six thousand, four hundred minutes\""""
    date = "1998-06-20"
    output = "Eight hundred six thousand, four hundred minutes"
    check50.run("python3 testing.py").stdin(date, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_invalid_input():
    """Input of \"February 6th, 1998\" prompts program to exit"""
    date = "February 6th, 1998"
    code = check50.run("python3 testing.py").stdin(date, prompt=True).exit()
    if code == 0:
        check50.Failure("Expected non-zero exit code.")


"""
test_seasons checks
"""

@check50.check(exists)
def test_student_file_passes():
    """seasons.py passes all checks in test_seasons.py"""
    check50.run("pytest test_seasons.py").exit(0)


@check50.check(test_student_file_passes)
def test_number_functions():
    """test_seasons.py contains at least three functions"""
    out = check50.run("pytest test_seasons.py").stdout()
    matches = search(r'(\d) passed', out)
    if not matches:
        raise check50.Failure("Could not parse output of pytest")
    try:
        functions = int(matches.groups(1)[0])
    except ValueError:
        raise check50.Failure("Could not parse output of pytest")
    if functions < 3:
        raise check50.Failure("test_seasons.py does not contain at least three functions")


"""
Helpers
"""


def regex(text):
    """match case-sensitively, allowing for only whitespace on either side"""
    return fr'^\s*{escape(text)}\s*$'