import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """professor.py exists"""
    check50.exists("professor.py")


@check50.check()
def test_level_low():
    """Little Professor rejects level of 0"""
    check50.run("python3 professor.py").stdin("0").reject()


@check50.check()
def test_level_high():
    """Little Professor rejects level of 4"""
    check50.run("python3 professor.py").stdin("4").reject()


@check50.check()
def test_question():
    """Little Professor accepts valid level"""
    check50.run("python3 professor.py").stdin("1").stdout(regex("+"), "+", regex=True).kill()


@check50.check()
def test_question2():
    """Little Professor tests a question"""
    output = check50.run("python3 professor.py").stdin("1").stdout()
    check50.log(output)


def regex(text):
    """match case-sensitively with any characters on either side"""
    return fr'^.*{escape(text)}.*$'