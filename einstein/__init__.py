import check50
import re


@check50.check()
def exists():
    """einstein.py exists"""
    check50.exists("einstein.py")


@check50.check(exists)
def test1():
    """input of 1 yields output of 90000000000000000"""
    output = check50.run("python3 einstein.py").stdin("1", prompt=False).stdout()

    # Extract number from stdout
    match = re.search(r"([.,]?(?:\d[.,]?)+)", output)
    if match is None:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match.group(0)

    # Match correct number
    if not re.match(r"^90(?:,?0{3}){5}(?:\.0+)?$", number) and not re.match(
        r"^90(?:\.?0{3}){5}(?:,0+)?$", number
    ):
        raise check50.Mismatch(
            "90000000000000000",
            number,
            help="Seems like your output might not be the right number!",
        )


@check50.check(exists)
def test14():
    """input of 14 yields output of 1260000000000000000"""
    output = check50.run("python3 einstein.py").stdin("14", prompt=False).stdout()

    # Extract number from stdout
    match = re.search(r"([.,]?(?:\d[.,]?)+)", output)
    if match is None:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match.group(0)

    # Match correct number
    if not re.match(r"^1,?260(?:,?0{3}){5}(?:\.0+)?$", number) and not re.match(
        r"1\.?260(?:\.?0{3}){5}(?:,0+)?$", number
    ):
        raise check50.Mismatch(
            "1260000000000000000",
            number,
            help="Seems like your output might not be the right number!",
        )


@check50.check(exists)
def test50():
    """input of 50 yields output of 4500000000000000000"""
    output = check50.run("python3 einstein.py").stdin("50", prompt=False).stdout()

    # Extract number from stdout
    match = re.search(r"([.,]?(?:\d[.,]?)+)", output)
    if match is None:
        raise check50.Failure("Looks like your program didn't output a number!")
    number = match.group(0)

    # Match correct number
    if not re.match(r"^4,?500(?:,?0{3}){5}(?:\.0+)?$", number) and not re.match(
        r"^4\.?500(?:\.?0{3}){5}(?:,0+)?$", number
    ):
        raise check50.Mismatch(
            "4500000000000000000",
            number,
            help="Seems like your output might not be the right number!",
        )
