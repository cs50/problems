import check50
from re import escape


@check50.check()
def exists():
    """bank.py exists"""
    check50.exists("bank.py")


@check50.check(exists)
def testHello():
    """input of \"Hello\" yields output of $0"""
    input = "Hello"
    output = "$0"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testHello_spaces():
    """input of \" Hello \" yields output of $0"""
    input = " Hello "
    output = "$0"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testHello_Newman():
    """input of \"Hello, Newman\" yields output of $0"""
    input = "Hello, Newman"
    output = "$0"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testHow_you_doing():
    """input of \"How you doing?\" yields output of $20"""
    input = "How you doing?"
    output = "$20"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testWhats_happening():
    """input of \"What's happening?\" yields output of $100"""
    input = "What's happening?"
    output = "$100"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testWhats_up():
    """input of \"What's up?\" yields output of $100"""
    input = "What's up?"
    output = "$100"
    check50.run("python3 bank.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(amount):
    """match amount, allowing for characters (not numbers) on either side"""
    return fr'^([^\d](?<!\$None)(?<!\$nan))*{escape(amount)}([^\d](?<!\$None)(?<!\$nan))*$'
