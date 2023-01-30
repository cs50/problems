import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./hello").stdin("Emma").stdout("Emma").exit()

@check50.check(compiles)
def inno():
    """responds to name Inno"""
    check50.run("./hello").stdin("Inno").stdout("Inno").exit()

@check50.check(compiles)
def kamryn():
    """responds to name Kamryn"""
    check50.run("./hello").stdin("Kamryn").stdout("Kamryn").exit()
