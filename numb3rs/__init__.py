import check50
from re import escape, sub

"""
setup
"""


@check50.check()
def exists():
    """numb3rs.py exists"""
    check50.exists("numb3rs.py")
    check50.include("testing.py")

"""
numb3rs.py checks
"""

@check50.check(exists)
def test_correct_ipv4_localhost():
    """numb3rs.py prints True for 127.0.0.1"""
    input = "127.0.0.1"
    output = "True"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_correct_ipv4_broadcast():
    """numb3rs.py prints True for 255.255.255.255"""
    input = "255.255.255.255"
    output = "True"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_correct_ipv4_harvard():
    """numb3rs.py prints True for 140.247.235.144"""
    input = "140.247.235.144"
    output = "True"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_incorrect_out_of_range():
    """numb3rs.py prints False for 256.255.255.255"""
    input = "256.255.255.255"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_incorrect_out_of_range2():
    """numb3rs.py prints False for 64.128.256.512"""
    input = "64.128.256.512"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_incorrect_ipv6():
    """numb3rs.py prints False for 2001:0db8:85a3:0000:0000:8a2e:0370:7334"""
    input = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_non_ip():
    """numb3rs.py prints False for cat"""
    input = "cat"
    output = "False"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


"""
test_numb3rs.py checks
"""

@check50.check(exists)
def test_correct():
    """correct numb3rs.py passes all test_numb3rs.py checks"""
    test_implementation("numb3rs.py", "correct_test.pyc", "test_numb3rs.py", code=0)


@check50.check(test_correct)
def test_first_byte():
    """test_numb3rs.py catches numb3rs.py only checking first byte of IPv4 address"""
    test_implementation("numb3rs.py", "first_byte_test.pyc", "test_numb3rs.py", code=1)


@check50.check(test_correct)
def test_invalid_format():
    """test_numb3rs.py catches numb3rs.py failing to return False for invalid IPv4 format"""
    test_implementation("numb3rs.py", "invalid_format_test.pyc", "test_numb3rs.py", code=1)


"""
Helpers
"""

def regex(text):
    """match case-insensitively, allowing for only whitespace on either side"""
    return fr'^(?i)\s*{escape(text)}\s*$'


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