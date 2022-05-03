import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """professor.py exists"""
    check50.exists("professor.py")
    check50.include("testing.py")


@check50.check(exists)
def test_level_low():
    """Little Professor rejects level of 0"""
    check50.run("python3 testing.py get_level").stdin("0", prompt=False).reject()


@check50.check(exists)
def test_level_high():
    """Little Professor rejects level of 4"""
    check50.run("python3 testing.py get_level").stdin("4", prompt=False).reject()


@check50.check(exists)
def test_valid_level():
    """Little Professor accepts valid level"""
    check50.run("python3 testing.py get_level").stdin("1", prompt=False).exit(0)


@check50.check(exists)
def test_program():
    """Little Professor generates 10 problems before exiting"""
    solutions = [12, 4, 15, 10, 12, 12, 10, 6, 10, 12]
    program = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for solution in solutions:
        program.stdin(str(solution), prompt=False)
    program.exit(0)


@check50.check(exists)
def test_score():
    """Little Professor displays number of problems correct"""
    solutions = [12, 4, 15, 10, 12, 12, 10, 6, 10, 10, 12]
    program = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for solution in solutions:
        program.stdin(str(solution), prompt=False)
    program.stdout(regex("9"), "9", regex=True)
    program.exit(0)


@check50.check(exists)
def test_EEE():
    """Little Professor displays EEE when answer is incorrect"""
    check50.run("python3 testing.py main").stdin("1", prompt=False).stdin("0", prompt=False).stdout(regex("EEE"), "EEE", regex=True).kill()


@check50.check(exists)
def test_show_solution():
    """Little Professor shows solution after 3 incorrect attempts"""
    program = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for _ in range(3):
        program.stdin("0", prompt=False)
    program.stdout(regex("12"), "12", regex=True)
    program.kill()


def regex(text):
    """match case-sensitively with any characters on either side"""
    return fr'^.*{escape(text)}.*$'