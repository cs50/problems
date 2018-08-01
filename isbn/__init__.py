import check50
import check50.c

@check50.check()
def exists():
    """isbn.c exists"""
    check50.exists("isbn.c")

@check50.check(exists)
def compiles():
    """isbn.c compiles"""
    check50.c.compile("isbn.c", lcs50=True)

@check50.check(compiles)
def Absolute_Beginners_Guide():
    """Beginners Guide (0789751984) valid"""
    check50.run("./isbn").stdin("0789751984").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def Absolute_Beginners_Guide_fake():
    """Beginners Guide fake (0789751985) invalid"""
    check50.run("./isbn").stdin("0789751985").stdout("^NO\n", "NO\n").exit(0)

@check50.check(compiles)
def Programming_in_C():
    """Programming in C (0321776410) valid"""
    check50.run("./isbn").stdin("0321776410").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def Hackers_Delight():
    """Hackers Delight (0321842685) valid"""
    check50.run("./isbn").stdin("0321842685").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def phone_number():
    """Jennys number (6178675309) invalid"""
    check50.run("./isbn").stdin("6178675309").stdout("^NO\n", "NO\n").exit(0)

@check50.check(compiles)
def memory():
    """Mystery Test"""
    check50.run("./isbn").stdin("1632168146").stdout("^YES\n", "YES\n").exit(0)

@check50.check(compiles)
def ISBN_with_X():
    """rejects ISBNs with X as checksum"""
    check50.run("./isbn").stdin("078974984X").reject()

@check50.check(compiles)
def rejects_ISBNs_with_dashes():
    """rejects ISBNs with dashes"""
    check50.run("./isbn").stdin("0-789-75198-4").reject()

@check50.check(compiles)
def rejects_empty():
    """rejects a non-numeric input of "" """
    check50.run("./isbn").stdin("").reject()
