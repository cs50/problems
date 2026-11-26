import check50
import sys
from os import rename
from shutil import rmtree
from re import sub


@check50.check()
def exists():
    """test_twttr.py exist"""
    check50.exists("test_twttr.py")
    
    # Include testing twttr.py
    check50.include("twttr.py")


@check50.check(exists)
def test_correct():
    """correct twttr.py passes all test_twttr checks"""
    test_implementation("correct_test", code=0)


@check50.check(test_correct)
def test_vowel_replacement():
    """test_twttr catches twttr.py without vowel replacement"""
    test_implementation("vowel_replacement_test", code=1)


@check50.check(test_correct)
def test_capital_vowel_replacement():
    """test_twttr catches twttr.py without capitalized vowel replacement"""
    test_implementation("capital_vowel_test", code=1)


@check50.check(test_correct)
def test_lower_vowel_replacement():
    """test_twttr catches twttr.py without lowercase vowel replacement"""
    test_implementation("lower_vowel_test", code=1)


@check50.check(test_correct)
def test_number_printing():
    """test_twttr catches twttr.py omitting numbers"""
    test_implementation("number_test", code=1)


@check50.check(test_correct)
def test_capital_output():
    """test_twttr catches twttr.py printing in uppercase"""
    test_implementation("capital_test", code=1)


@check50.check(test_correct)
def test_punctuation():
    """test_twttr catches twttr.py omitting punctuation"""
    test_implementation("punctuation_test", code=1)


def patch_file(import_file):
    """patch a new version of is_valid by updating import statement"""

    # Update import statement with new filename
    with open("twttr.py", "r") as f:
        twttr = sub(r"with open\(\".*\", \"rb\"\) as test_file:", f"with open(\"{import_file}.pyc\", \"rb\") as test_file:", f.read())

    # Write new import statement to twttr.py
    with open("twttr.py", "w") as f:
        f.write(twttr)


def test_implementation(filename, code=0):
    """test an implementation of twttr.py against student's checks in test_twttr.py, expect a given exit status"""

    # Include new compiled testing version of twttr.py
    include_pyc(filename)

    # Patch is_valid function from new test file
    patch_file(f"{filename}")

    # Remove cached bytecode so pytest imports the newly patched file, not a
    # stale __pycache__ entry (possible when the file's size and mtime are unchanged)
    rmtree("__pycache__", ignore_errors=True)

    # Expect that pytest will exit with given status code
    return check50.run("pytest test_twttr.py").exit(code=code)


def include_pyc(name):
    """Include name.pyc compiled for the running Python.

    Bytecode is specific to a Python minor version: executing a mismatch crashes the
    interpreter. The checks ship name.cpython-<major><minor>.pyc for each supported
    version (from cs50/cs50p-pytest-tests); include the right one under the plain name.
    """
    tag = f"cpython-{sys.version_info.major}{sys.version_info.minor}"
    check50.include(f"{name}.{tag}.pyc")
    rename(f"{name}.{tag}.pyc", f"{name}.pyc")
