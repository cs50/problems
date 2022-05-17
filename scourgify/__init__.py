import check50
import check50.internal
from re import escape


@check50.check()
def exists():
    """scourgify.py exists"""
    check50.exists("scourgify.py")
    check50.include("before.csv")
    check50.include("1.csv")
    check50.include("2.csv")
    check50.include("3.csv")


@check50.check(exists)
def test_no_arguments():
    """scourgify.py exits given no command-line arguments"""
    exit = check50.run("python3 scourgify.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_too_few_arguments():
    """scourgify.py exits given too few command-line arguments"""
    exit = check50.run("python3 scourgify.py 1.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_too_many_arguments():
    """scourgify.py exits given too many command-line arguments"""
    check50.run("python3 scourgify.py 1.csv 2.csv 3.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_file():
    """scourgify.py exits given invalid file"""
    exit = check50.run("python3 scourgify.py invalid_name.csv invalid_name2.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_create_file():
    """scourgify.py creates new csv file"""
    check50.run("python3 scourgify.py before.csv after.csv").exit(0)
    check50.exists("after.csv")


@check50.check(test_create_file)
def test_clean_file():
    """scourgify.py cleans csv file"""
    check50.run("python3 scourgify.py before.csv after.csv").exit(0)
    hash = check50.hash("after.csv")
    if hash == "584703d1422c3dc0006af54109c8ebfd8998ec8256a463e6ddeab6cb2869f92f":
        raise check50.Failure("CSV does not match specified format", help="Did you mistakenly open your file in append mode?")
    elif hash != "440790c127f56d3581809a6e5feef891a49f0039aff7944035afdf4a75aec170":
        raise check50.Failure("CSV does not match specified format")


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'