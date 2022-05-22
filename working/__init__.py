import check50
from re import escape, sub

"""
Setup
"""

@check50.check()
def exists():
    """working.py and test_working.py exist"""
    check50.exists("working.py")
    check50.exists("test_working.py")

"""
working.py checks
"""

@check50.check(exists)
def convert_9_to_5_short():
    """working.py converts \"9 AM to 5 PM\" to \"09:00 to 17:00\""""
    test_valid_time(input="9 AM to 5 PM", output="09:00 to 17:00")


@check50.check(exists)
def convert_9_to_5_long():
    """working.py converts \"9:00 AM to 5:00 PM\" to \"09:00 to 17:00\""""
    test_valid_time(input="9:00 AM to 5:00 PM", output="09:00 to 17:00")


@check50.check(exists)
def convert_8_to_8_short():
    """working.py converts \"8 PM to 8 AM\" to \"20:00 to 08:00\""""
    test_valid_time(input="8 PM to 8 AM", output="20:00 to 08:00")


@check50.check(exists)
def convert_8_to_8_long():
    """working.py converts \"8:00 PM to 8:00 AM\" to \"20:00 to 08:00\""""
    test_valid_time(input="8:00 PM to 8:00 AM", output="20:00 to 08:00")


@check50.check(exists)
def convert_12_to_12_short():
    """working.py converts \"12 AM to 12 PM\" to \"00:00 to 12:00\""""
    test_valid_time(input="12 AM to 12 PM", output="00:00 to 12:00")


@check50.check(exists)
def convert_12_to_12_long():
    """working.py converts \"12:00 AM to 12:00 PM\" to \"00:00 to 12:00\""""
    test_valid_time(input="12:00 AM to 12:00 PM", output="00:00 to 12:00")


@check50.check(exists)
def raise_for_invalid_time():
    """working.py raises ValueError when given \"8:60 AM to 4:60 PM\""""
    test_invalid_time(input="8:60 AM to 4:60 PM", error="ValueError")


@check50.check(exists)
def raise_for_invalid_spaces():
    """working.py raises ValueError when given \"9AM to 5PM\""""
    test_invalid_time(input="9AM to 5PM", error="ValueError")


@check50.check(exists)
def raise_for_invalid_format():
    """working.py raises ValueError when given \"09:00 to 17:00\""""
    test_invalid_time(input="09:00 to 17:00", error="ValueError")


"""
test_working.py checks
"""

@check50.check(exists)
def test_correct():
    """correct working.py passes all test_working checks"""
    test_implementation("working.py", "correct_test.pyc", "test_working.py", code=0)


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