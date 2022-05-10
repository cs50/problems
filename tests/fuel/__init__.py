import check50
from re import sub


@check50.check()
def exists():
    """test_fuel.py exist"""
    check50.exists("test_fuel.py")
    
    # Include testing fuel.py
    check50.include("fuel.py")


@check50.check(exists)
def test_correct():
    """correct fuel.py passes all test_fuel checks"""
    test_implementation("correct_test", code=0)


@check50.check(test_correct)
def test_convert():
    """test_fuel catches fuel.py returning incorrect ints in convert"""
    test_implementation("convert_test", code=1)


@check50.check(test_correct)
def test_value_error():
    """test_fuel catches fuel.py not raising ValueError in convert"""
    test_implementation("value_error_test", code=1)


@check50.check(test_correct)
def test_zero_division_error():
    """test_fuel catches fuel.py not raising ZeroDivisionError in convert"""
    test_implementation("zero_division_error_test", code=1)


@check50.check(test_correct)
def test_lower_bound():
    """test_fuel catches fuel.py returning incorrect percentages in gauge"""
    test_implementation("gauge_test", code=1)


@check50.check(test_correct)
def test_percent_gauge():
    """test_fuel catches fuel.py not printing % in gauge"""
    test_implementation("percent_gauge_test", code=1)


@check50.check(test_correct)
def test_lower_bound():
    """test_fuel catches fuel.py not labeling 1% as E in gauge"""
    test_implementation("lower_bound_test", code=1)


@check50.check(test_correct)
def test_upper_bound():
    """test_fuel catches fuel.py not labeling 99% as F in gauge"""
    test_implementation("upper_bound_test", code=1)


def patch_file(import_file):
    """patch a new version of is_valid by updating import statement"""

    # Update import statement with new filename
    with open("fuel.py", "r") as f:
        fuel = sub("with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{import_file}.pyc\", \"rb\") as test_file:", f.read())

    # Write new import statement to fuel.py
    with open("fuel.py", "w") as f:
        f.write(fuel)


def test_implementation(filename, code=0):
    """test an implementation of fuel.py against student's checks in test_fuel.py, expect a given exit status"""

    # Include new compiled testing version of fuel.py
    check50.include(f"{filename}.pyc")

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_fuel.py").exit(code=code)