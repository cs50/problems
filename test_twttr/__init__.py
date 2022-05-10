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


@check50.check(exists)
def test_vowel_replacement():
    """test_twttr catches twttr.py without vowel replacement"""
    test_implementation("vowel_replacement_test", code=1)


@check50.check(exists)
def test_capital_vowel_replacement():
    """test_twttr catches twttr.py without capitalized vowel replacement"""
    test_implementation("capital_vowel_test", code=1)


@check50.check(exists)
def test_lower_vowel_replacement():
    """test_twttr catches twttr.py without lowercase vowel replacement"""
    test_implementation("lower_vowel_test", code=1)


@check50.check(exists)
def test_lower_vowel_replacement():
    """test_twttr catches twttr.py without number printing"""
    test_implementation("lower_vowel_test", code=1)


def patch_file(import_file):
    """patch a new version of convert by updating import statement"""

    # Update import statement with new filename
    with open("twttr.py", "r") as f:
        twttr = sub(f"from \w* import convert", f"from {import_file} import convert", f.read())

    # Write new import statement to plates.py
    with open("twttr.py", "w") as f:
        f.write(twttr)


def test_implementation(filename, code=0):
    """test an implementation of twttr.py against student's checks in test_twttr.py, expect a given exit status"""

    # Include new testing version of plates.py
    check50.include(f"{filename}.py")

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_twttr.py").exit(code=code)