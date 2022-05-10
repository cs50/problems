import check50
from re import sub


@check50.check()
def exists():
    """test_twttr.py exist"""
    check50.exists("test_twttr.py")
    
    # Include testing plates.py
    check50.include("twttr.py")


@check50.check(exists)
def test_correct():
    """correct twttr.py passes all test_twttr checks"""
    test_implementation("correct_test", code=0)


def patch_file(import_file):
    """patch a new version of convert by updating import statement"""

    # Update import statement with new filename
    with open("twttr.py", "r") as f:
        plates = sub(f"from \w* import is_valid", f"from {import_file} import is_valid", f.read())

    # Write new import statement to plates.py
    with open("twttr.py", "w") as f:
        f.write(plates)


def test_implementation(filename, code=0):
    """test an implementation of twttr.py against student's checks in test_twttr.py, expect a given exit status"""

    # Include new testing version of plates.py
    check50.include(f"{filename}.py")

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_twttr.py").exit(code=code)