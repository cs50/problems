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


# Numbers before letters (Doc Hudson, Cars)
@check50.check(exists)
def test_51HHMD():
    """input of 51HHMD yields output of Invalid"""
    input = "51HHMD"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Non-alphanumeric characters (Tow Mater, Cars)
@check50.check(exists)
def test_A113():
    """input of A-113 yields output of Invalid"""
    input = "A-113"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Length and non-alphanumeric characters (Luigi, Cars)
@check50.check(exists)
def test_445108():
    """input of 44.5-10.8 yields output of Invalid"""
    input = "This is CS50"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


# Length (Back to the Future)
@check50.check(exists)
def test_OUTATIME():
    """input of OUTATIME yields output of Invalid"""
    input = "OUTATIME"
    output = "Invalid"
    check50.run("python3 plates.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-insensitively, allowing for only spaces on either side"""
    return fr'(?i)^\s*{escape(text)}\s*$'