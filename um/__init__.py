import check50
from re import escape, sub

"""
Setup
"""


@check50.check()
def exists():
    """um.py and test_um.py exist"""
    check50.exists("um.py")
    check50.exists("test_um.py")
    check50.include("testing.py")


"""
um.py checks
"""


@check50.check(exists)
def test_simple():
    """um.py yields 1 for \"um\""""
    test_phrase(input="um", count="1")


@check50.check(exists)
def test_comma():
    """um.py yields 1 for \"Hello, um, world\""""
    test_phrase(input="Hello, um, world", count="1")


@check50.check(exists)
def test_period():
    """um.py yields 1 for \"This is, um... CS50.\""""
    test_phrase(input="This is, um... CS50.", count="1")


@check50.check(exists)
def test_capital():
    """um.py yields 1 for \"Um... what are regular expressions?\""""
    test_phrase(input="Um... what are regular expressions?", count="1")


@check50.check(exists)
def test_multiple():
    """um.py yields 2 for \"Um, thanks, um, regular expressions make sense now.\""""
    test_phrase(input="Um, thanks, um, regular expressions make sense now.", count="2")


@check50.check(exists)
def test_part_of_word():
    """um.py yields 2 for \"Um? Mum? Is this that album where, um, the clumsy alums play drums?\""""
    test_phrase(input="Um? Mum? Is this that album where, um, the clumsy alums play drums?", count="2")


"""
test_um.py checks
"""


@check50.check(exists)
def test_correct():
    """correct um.py passes all test_um.py checks"""
    test_implementation("um.py", "correct_test.pyc", "test_um.py", code=0)


@check50.check(test_correct)
def test_part_of_words():
    """test_um.py catches um.py matching \"um\" in words"""
    test_implementation("um.py", "part_of_words_test.pyc", "test_um.py", code=1)


@check50.check(test_correct)
def test_only_spaces():
    """test_um.py catches um.py with regular expression requiring spaces around \"um\""""
    test_implementation("um.py", "only_spaces_test.pyc", "test_um.py", code=1)


@check50.check(test_correct)
def test_case_insensitive():
    """test_um.py catches um.py without case-insensitive matching of \"um\""""
    test_implementation("um.py", "case_insensitive_test.pyc", "test_um.py", code=1)


"""
Helpers
"""


def test_phrase(input, count):
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(count), count, regex=True).exit(0)


def regex(text):
    """Match case-insensitively, allowing for any characters on either side"""
    return fr'^(?i).*{escape(text)}.*$'


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