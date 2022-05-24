import check50
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
def test_level_nonint():
    """Little Professor rejects level of one"""
    check50.run("python3 testing.py get_level").stdin("one", prompt=False).reject()
    
    
@check50.check(exists)
def test_valid_level():
    """Little Professor accepts valid level"""

    # Test all levels 1–3
    for level in range(1, 4):
        check50.run("python3 testing.py get_level").stdin(str(level), prompt=False).exit(0)


@check50.check(test_valid_level)
def test_range_level_1():
    """At Level 1, Little Professor generates addition problems using 0–9"""
    level = "1"

    # With random.seed(0) in testing.py, 6 + 6 is expected output from randint and randrange with range of 0–9
    output = "6 + 6 ="
    check50.run("python3 testing.py main").stdin(level, prompt=False).stdout(regex(output), output, regex=True)


@check50.check(test_valid_level)
def test_range_level_2():
    """At Level 2, Little Professor generates addition problems using 10–99"""
    level = "2"

    # With random.seed(0) in testing.py, 59 + 63 is expected output from randint and randrange with range of 10–99
    output = "59 + 63 ="
    check50.run("python3 testing.py main").stdin(level, prompt=False).stdout(regex(output), output, regex=True)


@check50.check(test_valid_level)
def test_range_level_3():
    """At Level 3, Little Professor generates addition problems using 100–999"""
    level = "3"

    # With random.seed(0) in testing.py, 964 + 494 is expected output from randint and randrange with range of 100–999
    output = "964 + 494 ="
    check50.run("python3 testing.py main").stdin(level, prompt=False).stdout(regex(output), output, regex=True)


@check50.check(test_range_level_1)
def test_generate_problems():
    """Little Professor generates 10 problems before exiting"""
    solutions = [12, 4, 15, 10, 12, 12, 10, 6, 10, 12]
    program = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for solution in solutions:
        program.stdin(str(solution), prompt=False)
    program.exit(0)


@check50.check(test_generate_problems)
def test_score():
    """Little Professor displays number of problems correct"""
    solutions = [12, 4, 15, 8, 8, 8, 12, 12, 10, 6, 10, 12]
    program = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for solution in solutions:
        program.stdin(str(solution), prompt=False)
    program.stdout(score_regex("9"), "9", regex=True)
    program.exit(0)


@check50.check(test_generate_problems)
def test_EEE():
    """Little Professor displays EEE when answer is incorrect"""
    check50.run("python3 testing.py main").stdin("1", prompt=False).stdin("0", prompt=False).stdout(regex("EEE"), "EEE", regex=True)


@check50.check(test_generate_problems)
def test_show_solution():
    """Little Professor shows solution after 3 incorrect attempts"""
    program = check50.run("python3 testing.py main").stdin("1", prompt=False)
    for _ in range(3):
        program.stdin("0", prompt=False)
    program.stdout(regex("12"), "12", regex=True)


def regex(text):
    """match case-sensitively with any characters on either side"""
    return fr'^.*{escape(text)}.*$'


def score_regex(score):
    """match case-insensitively with only final printing of score"""
    return fr'(?i)[^\d+=]*{score}[^\d+=]*$'
