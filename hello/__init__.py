import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists."""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles."""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def veronica():
    """responds to name Veronica."""
    check50.run("./hello").stdin("Veronica").stdout("Veronica").exit()

@check50.check(compiles)
def brian():
    """responds to name Brian."""
    check50.run("./hello").stdin("Brian").stdout("Brian").exit()
