import check50
from re import sub


@check50.check()
def exists():
    """test_fuel.py exist"""
    check50.exists("test_fuel.py")
    
    # Include testing plates.py
    check50.include("fuel.py")


@check50.check(exists)
def test_correct():
    """correct fuel.py passes all test_fuel checks"""
    test_implementation("correct_test", code=0)


@check50.check(exists)
def test_float():
    """test_fuel catches fuel.py returning incorrect floats in convert"""
    test_implementation("float_test", code=1)


@check50.check(exists)
def test_int():
    """test_fuel catches fuel.py returning int instead of float in convert"""
    test_implementation("int_test", code=1)


@check50.check(exists)
def test_value_error():
    """test_fuel catches fuel.py not raising ValueError in convert"""
    test_implementation("value_error_test", code=1)


@check50.check(exists)
def test_zero_division_error():
    """test_fuel catches fuel.py not raising ZeroDivisionError in convert"""
    test_implementation("zero_division_test", code=1)


@check50.check(exists)
def test_float_gauge():
    """test_fuel catches fuel.py returning a float in gauge"""
    test_implementation("float_test_gauge", code=1)


@check50.check(exists)
def test_str_gauge():
    """test_fuel catches fuel.py accepting a str in gauge"""
    test_implementation("str_test_gauge", code=1)


def patch_file(import_file):
    """patch a new version of value by updating import statement"""

    # Update import statement with new filename
    with open("fuel.py", "r") as f:
        fuel = sub(f"from \w* import convert", f"from {import_file} import convert", f.read())
        fuel = sub(f"from \w* import gauge", f"from {import_file} import gauge", fuel)

    # Write new import statement to fuel.py
    with open("fuel.py", "w") as f:
        f.write(fuel)


def test_implementation(filename, code=0):
    """test an implementation of fuel.py against student's checks in fuel.py, expect a given exit status"""

    # Include new testing version of plates.py
    check50.include(f"{filename}.py")

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_fuel.py").exit(code=code)