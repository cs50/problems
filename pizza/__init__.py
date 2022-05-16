import check50
from re import escape


@check50.check()
def exists():
    """pizza.py exists"""
    check50.exists("pizza.py")


@check50.check(exists)
def test_no_arguments():
    """pizza.py exits given no command-line arguments"""
    exit = check50.run("python3 pizza.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_not_exist():
    """pizza.py exits given non-existent file"""
    exit = check50.run("python3 pizza.py non_existent.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_non_csv():
    """pizza.py exits given non-csv file"""
    check50.include("sicilian.txt")
    exit = check50.run("python3 pizza.py sicilian.txt").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_too_many_arguments():
    """pizza.py exits given too many command-line arguments"""
    check50.include("regular.csv")
    check50.include("sicilian.csv")
    check50.run("python3 pizza.py regular.csv sicilian.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_sicilian():
    """pizza.py renders prices from sicilian.csv"""
    check_table_rendering("sicilian")


@check50.check(exists)
def test_regular():
    """pizza.py renders prices from regular.csv"""
    check_table_rendering("regular")


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'


def check_table_rendering(pizza):
    check50.include(f"{pizza}.txt")
    check50.include(f"{pizza}.csv")
    with open(f"{pizza}.txt", "r") as file:
        lines = file.readlines()
        output = ""
        for line in lines:
            output += line
        check50.run(f"python3 pizza.py {pizza}.csv").stdout(regex(output), output, regex=True).exit(0)
