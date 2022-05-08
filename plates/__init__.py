import check50
from re import escape


@check50.check()
def exists():
    """plates.py exists"""
    check50.exists("plates.py")


@check50.check(exists)
def test_cs50():
    """input of CS50 yields output of Valid"""
    input = "CS50"
    output = "Valid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Ready Player One
@check50.check(exists)
def test_ECTO88():
    """input of ECTO88 yields output of Valid"""
    input = "ECTO88"
    output = "Valid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Ferris Buehler's Day Off
@check50.check(exists)
def test_NRVOUS():
    """input of NRVOUS yields output of Valid"""
    input = "NRVOUS"
    output = "Valid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Tests for Zero as first number
@check50.check(exists)
def test_CS05():
    """input of CS05 yields output of Invalid"""
    input = "CS05"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

    
# Numbers before letters (after the first 2 letters)
@check50.check(exists)
def test_CS50P2():
    """input of CS50P2 yields output of Invalid"""
    input = "CS50P2"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Non-alphanumeric characters (after the first 2 letters)
@check50.check(exists)
def test_PI3_14():
    """input of PI3.14 yields output of Invalid"""
    input = "PI3.14"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Length (too short)
@check50.check(exists)
def test_445108():
    """input of H yields output of Invalid"""
    input = "H"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Length (too long) (Back to the Future)
@check50.check(exists)
def test_OUTATIME():
    """input of OUTATIME yields output of Invalid"""
    input = "OUTATIME"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-insensitively, allowing for only spaces on either side"""
    return fr'(?i)^\s*{escape(text)}\s*$'
