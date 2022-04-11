import check50


@check50.check()
def exists():
    """bank.py exists"""
    check50.exists("bank.py")


@check50.check(exists)
def testHello():
    """input of \"Hello\" yields output of $0"""
    check50.run("python3 bank.py").stdin("Hello", prompt=True).stdout(r'^[$]0[^\d]$', "$0", regex=True).exit()


@check50.check(exists)
def testHello():
    """input of \" Hello \" yields output of $0"""
    check50.run("python3 bank.py").stdin(" Hello ", prompt=True).stdout(r'^[$]0[^\d]$', "$0", regex=True).exit()


@check50.check(exists)
def testHello_Newman():
    """input of \"Hello, Newman\" yields output of $0"""
    check50.run("python3 bank.py").stdin("Hello, Newman", prompt=True).stdout(r'^[$]0[^\d]$', "$0", regex=True).exit()


@check50.check(exists)
def testHow_you_doing():
    """input of \"How you doing?\" yields output of $20"""
    check50.run("python3 bank.py").stdin("How you doing?", prompt=True).stdout(r'^[$]20[^\d]$', "$20", regex=True).exit()


@check50.check(exists)
def testWhats_happening():
    """input of \"What's happening?\" yields output of $100"""
    check50.run("python3 bank.py").stdin("What's happening?", prompt=True).stdout(r'^[$]100[^\d]$', "$100", regex=True).exit()


@check50.check(exists)
def testWhats_up():
    """input of \"what's up?\" yields output of $100"""
    check50.run("python3 bank.py").stdin("What's up?", prompt=True).stdout(r'^[$]100[^\d]$', "$100", regex=True).exit()