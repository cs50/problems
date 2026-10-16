import re

import check50

OUTPUT = re.compile(
    r"^After (\d+) simulations?\s*\n"
    r"with (\d+) students?\s*\n"
    r"there (?:were|was) (\d+) simulations? with at least one match\s*$"
)


@check50.check()
def exists():
    """probability.py exists"""
    check50.exists("probability.py")


@check50.check(exists)
def no_arguments():
    """prints an error message when given no command-line arguments"""
    check_error("python3 probability.py")


@check50.check(exists)
def one_argument():
    """prints an error message when given one command-line argument"""
    check_error("python3 probability.py 1000")


@check50.check(exists)
def output_format():
    """prints simulations, students, and matches in the expected format"""
    check_matches(900, 23, 0, 900)


@check50.check(output_format)
def one_student():
    """reports no matches with 1 student"""
    check_matches(1000, 1, 0, 0)


@check50.check(output_format)
def students_366():
    """reports a match in every simulation with 366 students"""
    check_matches(1000, 366, 1000, 1000)


@check50.check(output_format)
def students_23():
    """reports about 50% matches with 23 students"""
    check_matches(10000, 23, 4800, 5350)


@check50.check(output_format)
def students_70():
    """reports about 99.9% matches with 70 students"""
    check_matches(10000, 70, 9960, 10000)


@check50.check(output_format)
def students_10():
    """reports about 12% matches with 10 students"""
    check_matches(10000, 10, 1000, 1340)


def check_error(command):
    """Fail unless command prints an error message rather than nothing or a traceback."""
    actual = check50.run(command).stdout()
    if not actual.strip() or "Traceback (most recent call last)" in actual:
        raise check50.Failure(
            "expected an error message, but program did not print one",
            help="did you check len(sys.argv) before using the arguments?",
        )


def check_matches(simulations, students, low, high):
    """Run a simulation and require that its match count fall within [low, high]."""
    actual = check50.run(f"python3 probability.py {simulations} {students}").stdout(timeout=20)
    expected = (
        f"After {simulations} simulations\n"
        f"with {students} students\n"
        f"there were N simulations with at least one match\n"
    )
    match = OUTPUT.match(actual.strip())
    if not match:
        raise check50.Mismatch(expected, actual)
    if (int(match.group(1)), int(match.group(2))) != (simulations, students):
        raise check50.Mismatch(expected, actual, help="are you printing the number of simulations and students correctly?")
    matches = int(match.group(3))
    if not low <= matches <= high:
        if low == high:
            raise check50.Failure(f"expected {low} simulations with at least one match, not {matches}")
        raise check50.Failure(f"expected between {low} and {high} simulations with at least one match, not {matches}")
