import check50
from re import escape, search, sub

"""
Setup
"""

@check50.check()
def exists():
    """working.py and test_working.py exist"""
    check50.exists("working.py")
    check50.exists("test_working.py")


@check50.check(exists)
def libraries():
    """working.py does not import libraries other than sys and re"""
    with open("working.py", "r") as file:
        contents = file.read()
        if search(r'(?<!#)(?<! )(((?:^|\n\s*)\bimport(?![ \t]*(re|sys)\b))|((?:^|\n\s*)\bfrom\b(?![ \t]*(re|sys)\b)))', contents):
            raise check50.Failure("working.py imports libraries other than sys and re", help="Be sure only to use \"import re\" and \"import sys\", or \"from re import ...\" and \"from sys import ...\"")


"""
working.py checks
"""


@check50.check(libraries)
def convert_9_to_5_short():
    """working.py converts \"9 AM to 5 PM\" to \"09:00 to 17:00\""""
    test_valid_time(input="9 AM to 5 PM", output="09:00 to 17:00")


@check50.check(libraries)
def convert_9_to_5_long():
    """working.py converts \"9:00 AM to 5:00 PM\" to \"09:00 to 17:00\""""
    test_valid_time(input="9:00 AM to 5:00 PM", output="09:00 to 17:00")


@check50.check(libraries)
def convert_8_to_8_short():
    """working.py converts \"8 PM to 8 AM\" to \"20:00 to 08:00\""""
    test_valid_time(input="8 PM to 8 AM", output="20:00 to 08:00")


@check50.check(libraries)
def convert_8_to_8_long():
    """working.py converts \"8:00 PM to 8:00 AM\" to \"20:00 to 08:00\""""
    test_valid_time(input="8:00 PM to 8:00 AM", output="20:00 to 08:00")


@check50.check(libraries)
def convert_12_to_12_short():
    """working.py converts \"12 AM to 12 PM\" to \"00:00 to 12:00\""""
    test_valid_time(input="12 AM to 12 PM", output="00:00 to 12:00")


@check50.check(libraries)
def convert_12_to_12_long():
    """working.py converts \"12:00 AM to 12:00 PM\" to \"00:00 to 12:00\""""
    test_valid_time(input="12:00 AM to 12:00 PM", output="00:00 to 12:00")


@check50.check(libraries)
def raise_for_invalid_time():
    """working.py raises ValueError when given \"8:60 AM to 4:60 PM\""""
    test_invalid_time(input="8:60 AM to 4:60 PM", error="ValueError")


@check50.check(libraries)
def raise_for_invalid_spaces():
    """working.py raises ValueError when given \"9AM to 5PM\""""
    test_invalid_time(input="9AM to 5PM", error="ValueError")


@check50.check(libraries)
def raise_for_invalid_format_24_hour():
    """working.py raises ValueError when given \"09:00 to 17:00\""""
    test_invalid_time(input="09:00 to 17:00", error="ValueError")


@check50.check(libraries)
def raise_for_invalid_format_dash():
    """working.py raises ValueError when given \"9 AM - 5 PM\""""
    test_invalid_time(input="9 AM - 5 PM", error="ValueError")


@check50.check(libraries)
def raise_for_invalid_format_minutes():
    """working.py raises ValueError when given \"10:7 AM - 5:1 PM\""""
    test_invalid_time(input="10:7 AM - 5:1 PM", error="ValueError")


"""
test_working.py checks
"""

@check50.check(libraries)
def test_correct():
    """correct working.py passes all test_working checks"""
    test_implementation("working.py", "correct_test.pyc", "test_working.py", code=0)


@check50.check(test_correct)
def test_incorrect_hours():
    """test_working.py catches working.py printing hours off by one"""
    test_implementation("working.py", "off_by_one_test.pyc", "test_working.py", code=1)


@check50.check(test_correct)
def test_incorrect_minutes():
    """test_working.py catches working.py printing minutes off by five"""
    test_implementation("working.py", "off_by_five_test.pyc", "test_working.py", code=1)


@check50.check(test_correct)
def test_raise_for_format():
    """test_working.py catches working.py not raising ValueError when user omits \" to \""""
    test_implementation("working.py", "raise_for_format_test.pyc", "test_working.py", code=1)


@check50.check(test_correct)
def test_raise_for_out_of_range_time():
    """test_working.py catches working.py not raising ValueError for out-of-range times"""
    test_implementation("working.py", "raise_for_out_of_range_test.pyc", "test_working.py", code=1)


"""
Helpers
"""


def test_valid_time(input, output):
    check50.run("python3 working.py").stdin(input, prompt=True).stdout(stdout_regex(output), output, regex=True).exit(0)


def test_invalid_time(input, error):
    check50.run("python3 working.py").stdin(input, prompt=True).stdout(traceback_regex(error), error, regex=True).exit(1)


def stdout_regex(text):
    """Match case-sensitively, allowing for only whitespace on either side"""
    return fr'^\s*{escape(text)}\s*$'


def traceback_regex(text):
    """Match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'


def test_implementation(base_filename, implementation_filename, test_filename, code=0):
    """Test implementation_file, an implementation of base_file, against student's checks in test_file. Expect a given exit status"""

    check50.include("pytest_helper.py")
    check50.include(implementation_filename)

    # Overwrite base_file with code to run implementation_file
    with open(base_filename, "w") as base_file, open("pytest_helper.py", "r") as pytest_helper:

        # Read text from pytest_helper
        pytest_helper_text = pytest_helper.read()

        # Replace open statement with implementation_file
        pytest_helper_text = sub("with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{implementation_filename}\", \"rb\") as test_file:", pytest_helper_text)

        # Write helper file text to base_file
        base_file.writelines(pytest_helper_text)

    # Expect that pytest will exit with given status code
    return check50.run(f"pytest {test_filename}").exit(code=code)
