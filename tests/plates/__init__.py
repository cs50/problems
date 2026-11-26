import check50
import sys
from os import rename
from shutil import rmtree
from re import sub, match


@check50.check()
def exists():
    """test_plates.py exist"""
    check50.exists("test_plates.py")
    
    # Include testing plates.py
    check50.include("plates.py")


@check50.check(exists)
def test_correct():
    """correct plates.py passes all test_plates checks"""
    test_implementation("correct_test", code=0)


@check50.check(test_correct)
def test_beginning_alpha_checks():
    """test_plates catches plates.py without beginning alphabetical checks"""
    test_implementation("beginning_alpha_test", code=1)


@check50.check(test_correct)
def test_length_checks():
    """test_plates catches plates.py without length checks"""
    test_implementation("length_test", code=1)


@check50.check(test_correct)
def test_number_placement_checks():
    """test_plates catches plates.py without checks for number placement"""
    test_implementation("number_test", code=1)


@check50.check(test_correct)
def test_zero_checks():
    """test_plates catches plates.py without checks for zero placement"""
    test_implementation("zero_test", code=1)


@check50.check(test_correct)
def test_alnum_checks():
    """test_plates catches plates.py without checks for alphanumeric characters"""
    test_implementation("alnum_test", code=1)


def patch_file(import_file):
    """patch a new version of is_valid by updating import statement"""

    # Update import statement with new filename
    with open("plates.py", "r") as f:
        plates = sub(r"with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{import_file}.pyc\", \"rb\") as test_file:", f.read())

    # Write new import statement to plates.py
    with open("plates.py", "w") as f:
        f.write(plates)


def test_implementation(filename, code=0):
    """test an implementation of plates.py against student's checks in test_plates.py, expect a given exit status"""

    # Include new compiled testing version of plates.py
    include_pyc(filename)

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Remove cached bytecode so pytest imports the newly patched file, not a
    # stale __pycache__ entry (possible when the file's size and mtime are unchanged)
    rmtree("__pycache__", ignore_errors=True)

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_plates.py").exit(code=code)


def include_pyc(name):
    """Include name.pyc compiled for the running Python.

    Bytecode is specific to a Python minor version: executing a mismatch crashes the
    interpreter. The checks ship name.cpython-<major><minor>.pyc for each supported
    version (from cs50/cs50p-pytest-tests); include the right one under the plain name.
    """
    tag = f"cpython-{sys.version_info.major}{sys.version_info.minor}"
    check50.include(f"{name}.{tag}.pyc")
    rename(f"{name}.{tag}.pyc", f"{name}.pyc")
