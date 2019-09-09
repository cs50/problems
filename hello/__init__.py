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
def max():
    """responds to name Max"""
    check50.run("./hello").stdin("Max").stdout("Max").exit()

@check50.check(compiles)
def reese():
    """responds to name Reese"""
    check50.run("./hello").stdin("Reese").stdout("Reese").exit()

@check50.check(compiles)
def ileana():
    """responds to name Ileana"""
    check50.run("./hello").stdin("Ileana").stdout("Ileana").exit()
