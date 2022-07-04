import check50
from re import escape, search, sub


@check50.check()
def exists():
    """seasons.py and test_seasons.py exist"""
    check50.exists("seasons.py")
    check50.exists("test_seasons.py")
    check50.include("testing.py")


@check50.check(exists)
def test_one_year():
    """Input of \"1999-01-01\" yields \"Five hundred twenty-five thousand, six hundred minutes\" when today is 2000-01-01"""
    test_valid_dates(date="1999-01-01", today="2000-01-01", output="Five hundred twenty-five thousand, six hundred minutes")


@check50.check(exists)
def test_two_years():
    """Input of \"2001-01-01\" yields \"One million, fifty-one thousand, two hundred minutes\" when today is 2003-01-01"""
    test_valid_dates(date="2001-01-01", today="2003-01-01", output="One million, fifty-one thousand, two hundred minutes")


@check50.check(exists)
def test_leap_year():
    """Input of \"1995-01-01\" yields \"Two million, six hundred twenty-nine thousand, four hundred forty minutes\" when today is 2000-01-1"""
    test_valid_dates(date="1995-01-01", today="2000-01-01", output="Two million, six hundred twenty-nine thousand, four hundred forty minutes")


@check50.check(exists)
def test_months():
    """Input of \"2020-06-01\" yields \"Six million, ninety-two thousand, six hundred forty minutes\" when today is 2032-01-01"""
    test_valid_dates(date="2020-06-01", today="2032-01-01", output="Six million, ninety-two thousand, six hundred forty minutes")


@check50.check(exists)
def test_day():
    """Input of \"1998-06-20\" yields \"Eight hundred six thousand, four hundred minutes\" when today is 2000-01-01"""
    test_valid_dates(date="1998-06-20", today="2000-01-01", output="Eight hundred six thousand, four hundred minutes")


@check50.check(exists)
def test_invalid_input():
    """Input of \"February 6th, 1998\" prompts program to exit with sys.exit"""
    test_invalid_dates(date="February 6th, 1998")


"""
test_seasons checks
"""


@check50.check(exists)
def test_student_file_passes():
    """seasons.py passes all checks in test_seasons.py"""
    check50.run("pytest test_seasons.py").exit(0)


"""
Helpers
"""


def regex(text):
    """match case-sensitively, allowing for only whitespace on either side"""
    return fr'^\s*{escape(text)}\s*$'


def set_today(date):

    # Parse date
    year, month, day = date.split(sep="-", maxsplit=2)
    month = month.lstrip("0")
    day = day.lstrip("0")

    # Substitute testing date object with new date object
    with open("testing.py", "r") as testing_file:
        new_testing_contents = sub(r"return date\(\d{4}, *\d{1,2}, *\d{1,2}\)", fr"return date({year}, {month}, {day})", testing_file.read())

    # Write updated date object to testing file
    with open("testing.py", "w") as testing_file:
        testing_file.write(new_testing_contents)


def test_valid_dates(date, today, output):
    set_today(today)
    check50.run("python3 testing.py").stdin(date, prompt=True).stdout(regex(output), output, regex=True).exit(0)


def test_invalid_dates(date):
    code = check50.run("python3 testing.py").stdin(date, prompt=True).exit()
    if code == 0:
        raise check50.Failure("Expected non-zero exit code.")
    out = check50.run("python3 testing.py").stdin(date, prompt=True).stdout()
    if search(r'(Traceback)', out):
        raise check50.Failure("Program exited with a traceback")