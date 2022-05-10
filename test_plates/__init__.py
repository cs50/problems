import check50
from re import escape, sub


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

    # Patch is_valid function from correct_test file
    update_plates("correct_test")

    # Expect that pytest will exit with status code 0, given correct plates.py
    check50.run("pytest test_plates.py").exit(0)


@check50.check(exists)
def test_valid_length():
    """test_plates catches plates.py without length checks"""

    # Include new testing version of plates.py
    check50.include("length_test.py")

    # Patch is_valid function from length_test file
    update_plates("length_test")

    # Expect that pytest will exit with status code 1, given faulty plates.py
    check50.run("pytest test_plates.py").exit(1)


@check50.check(exists)
def test_beginning_alpha():
    """test_plates catches plates.py without beginning alphabetical checks"""

    # Include new testing version of plates.py
    check50.include("beginning_alpha_test.py")

    # Patch is_valid function from beginning_alpha_test file
    update_plates("beginning_alpha_test")

    # Expect that pytest will exit with status code 1, given faulty plates.py
    check50.run("pytest test_plates.py").exit(1)


def update_plates(import_file):
    """patch a new version of is_valid by updating import statement"""

    with open("plates.py", "r") as f:
        plates = sub(f"from \w* import is_valid", f"from {import_file} import is_valid", f.read())

    with open("plates.py", "w") as f:
        f.write(plates)
