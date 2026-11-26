import check50
import sys
from os import rename
from shutil import rmtree
from re import sub


@check50.check()
def exists():
    """test_bank.py exist"""
    check50.exists("test_bank.py")
    
    # Include testing bank.py
    check50.include("bank.py")


@check50.check(exists)
def test_correct():
    """correct bank.py passes all test_bank checks"""
    test_implementation("correct_test", code=0)


@check50.check(test_correct)
def test_reversed_values():
    """test_bank catches bank.py with incorrect values"""
    test_implementation("reversed_value_test", code=1)


@check50.check(test_correct)
def test_case_sensitive():
    """test_bank catches bank.py without case-insensitivity"""
    test_implementation("case_sensitive_test", code=1)


@check50.check(test_correct)
def test_starts_with():
    """test_bank catches bank.py not allowing for entire phrase"""
    test_implementation("starts_with_test", code=1)


def patch_file(import_file):
    """patch a new version of is_valid by updating import statement"""

    # Update import statement with new filename
    with open("bank.py", "r") as f:
        bank = sub(r"with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{import_file}.pyc\", \"rb\") as test_file:", f.read())

    # Write new import statement to bank.py
    with open("bank.py", "w") as f:
        f.write(bank)


def test_implementation(filename, code=0):
    """test an implementation of bank.py against student's checks in test_bank.py, expect a given exit status"""

    # Include new compiled testing version of bank.py
    include_pyc(filename)

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Remove cached bytecode so pytest imports the newly patched file, not a
    # stale __pycache__ entry (possible when the file's size and mtime are unchanged)
    rmtree("__pycache__", ignore_errors=True)

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_bank.py").exit(code=code)


def include_pyc(name):
    """Include name.pyc compiled for the running Python.

    Bytecode is specific to a Python minor version: executing a mismatch crashes the
    interpreter. The checks ship name.cpython-<major><minor>.pyc for each supported
    version (from cs50/cs50p-pytest-tests); include the right one under the plain name.
    """
    tag = f"cpython-{sys.version_info.major}{sys.version_info.minor}"
    check50.include(f"{name}.{tag}.pyc")
    rename(f"{name}.{tag}.pyc", f"{name}.pyc")
