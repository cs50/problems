import check50
from re import escape


@check50.check()
def exists():
    """lines.py exists"""
    check50.exists("lines.py")


@check50.check(exists)
def test_fewer_arguments():
    """lines.py exits given zero command-line arguments"""
    exit = check50.run("python3 lines.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_file():
    """lines.py exits given a file without a .py extension"""
    check50.include("invalid_extension.txt")
    exit = check50.run("python3 lines.py invalid_extension.txt").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(test_invalid_file)
def test_more_arguments():
    """lines.py exits given more than one command-line argument"""
    check50.include("4.py")
    check50.include("2058.py")
    exit = check50.run("python3 lines.py 4.py 2058.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_plain():
    """lines.py yields 3 given a file with 3 lines of code"""
    test_line_count(3)


@check50.check(test_plain)
def test_whitespace():
    """lines.py yields 4 given a file with 4 lines and whitespace"""
    test_line_count(4)


@check50.check(test_whitespace)
def test_comment():
    """lines.py yields 5 given a file with 5 lines, whitespace, and comments"""
    test_line_count(5)


@check50.check(test_comment)
def test_docstring():
    """lines.py yields 9 given a file with 9 lines, whitespace, comments, and docstrings"""
    test_line_count(9)


@check50.check(test_docstring)
def test_open_source():
    """lines.py yields 2058 given 2058 lines of code in an open-source library file"""
    test_line_count(2058)
    

def test_line_count(lines):
    check50.include(f"{lines}.py")
    check50.run(f"python3 lines.py {lines}.py").stdout(regex(lines), f"{lines}", regex=True).exit(0)


def regex(lines):
    """accept line number without digits before or after"""
    return fr'^\D*{escape(str(lines))}\D*$'