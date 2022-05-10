import check50
from re import sub


@check50.check()
def exists():
    """test_plates.py exist"""
    check50.exists("test_plates.py")
    
    # Include testing plates.py
    check50.include("plates.py")
    

@check50.check(exists)
def test_correct():
    """correct plates.py passes all test_plates checks"""

    # Include new testing version of plates.py
    check50.include("correct_test.py")

    # Patch is_valid function from new test file
    update_plates("correct_test")

    # Expect that pytest will exit with status code 0, given correct plates.py
    check50.run("pytest test_plates.py").exit(0)


@check50.check(exists)
def test_beginning_alpha_checks():
    """test_plates catches plates.py without beginning alphabetical checks"""
    test_buggy_file("beginning_alpha_test")


@check50.check(exists)
def test_length_checks():
    """test_plates catches plates.py without length checks"""
    test_buggy_file("length_test")


@check50.check(exists)
def test_number_placement_checks():
    """test_plates catches plates.py without checks for number placement"""
    test_buggy_file("number_test")


@check50.check(exists)
def test_zero_checks():
    """test_plates catches plates.py without checks for zero placement"""
    test_buggy_file("zero_test")


@check50.check(exists)
def test_alnum_checks():
    """test_plates catches plates.py without checks for alphanumeric characters"""
    test_buggy_file("alnum_test")


def update_plates(import_file):
    """patch a new version of is_valid by updating import statement"""

    # Update import statement with new filename
    with open("plates.py", "r") as f:
        plates = sub(f"from \w* import is_valid", f"from {import_file} import is_valid", f.read())

    # Write new import statement to plates.py
    with open("plates.py", "w") as f:
        f.write(plates)


def test_buggy_file(test_name):

    # Include new testing version of plates.py
    check50.include(f"{test_name}.py")

    # Patch is_valid function from new test file
    update_plates(f"{test_name}")

    # Expect that pytest will exit with status code 1, given faulty plates.py
    return check50.run("pytest test_plates.py").exit(1)