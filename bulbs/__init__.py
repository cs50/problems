import check50
import check50.c

@check50.check()
def exists():
    """bulbs.c exists"""
    check50.exists("bulbs.c")


@check50.check(exists)
def compiles():
    """bulbs.c compiles"""
    check50.c.compile("bulbs.c", lcs50=True)


@check50.check(compiles)
def bulbs1():
    """bulbifies an empty message correctly"""
    check50.run("./bulbs").stdin("").stdout("").exit(0)
    

@check50.check(compiles)
def bulbs2():
    """bulbifies "I" correctly (single letter)"""
    check50.run("./bulbs").stdin("I").stdout("⚫🟡⚫⚫🟡⚫⚫🟡\n").exit(0)
    

@check50.check(compiles)
def bulbs3():
    """bulbifies "xyz" correctly (multiple lowercase)"""
    check50.run("./bulbs").stdin("xyz").stdout("⚫🟡🟡🟡🟡⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡🟡🟡🟡⚫🟡⚫\n").exit(0)


@check50.check(compiles)
def bulbs4():
    """bulbifies "?" correctly (non-alphabetical)"""
    check50.run("./bulbs").stdin("?").stdout("⚫⚫🟡🟡🟡🟡🟡🟡\n").exit(0)


@check50.check(compiles)
def bulbs5():
    """bulbifies "Hi!" correctly (complete message)"""
    check50.run("./bulbs").stdin("Hi!").stdout("⚫🟡⚫⚫🟡⚫⚫⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫🟡\n").exit(0)
    

@check50.check(compiles)
def bulbs6():
    """bulbifies "aBcDeFgHiJkLmNoPqRsTuVwXyZ" correctly (full alphabet mixed case)"""
    check50.run("./bulbs").stdin("aBcDeFgHiJkLmNoPqRsTuVwXyZ").stdout("⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡⚫⚫⚫⚫🟡⚫\n⚫🟡🟡⚫⚫⚫🟡🟡\n⚫🟡⚫⚫⚫🟡⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡⚫⚫⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫🟡⚫⚫🟡⚫⚫⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡⚫⚫🟡⚫🟡⚫\n⚫🟡🟡⚫🟡⚫🟡🟡\n⚫🟡⚫⚫🟡🟡⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡⚫⚫🟡🟡🟡⚫\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡⚫🟡⚫⚫⚫⚫\n⚫🟡🟡🟡⚫⚫⚫🟡\n⚫🟡⚫🟡⚫⚫🟡⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫🟡⚫🟡⚫🟡⚫⚫\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡⚫🟡⚫🟡🟡⚫\n⚫🟡🟡🟡⚫🟡🟡🟡\n⚫🟡⚫🟡🟡⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡⚫🟡🟡⚫🟡⚫\n").exit(0)


@check50.check(compiles)
def bulbs7():
    """bulbifies " CS50 :) " correctly (message with nonalphanumeric characters)"""
    check50.run("./bulbs").stdin(" CS50 :) ").stdout("⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡⚫⚫⚫⚫🟡🟡\n⚫🟡⚫🟡⚫⚫🟡🟡\n⚫⚫🟡🟡⚫🟡⚫🟡\n⚫⚫🟡🟡⚫⚫⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫⚫🟡🟡🟡⚫🟡⚫\n⚫⚫🟡⚫🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n").exit(0)


@check50.check(compiles)
def bulbs_finale():
    """bulbifies The Great Gatsby's first sentence"""
    check50.run("./bulbs").stdin("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.").stdout("⚫🟡⚫⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡🟡⚫🟡🟡⚫⚫\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡⚫⚫⚫🟡⚫\n⚫🟡🟡⚫🟡🟡⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫🟡🟡⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫🟡🟡⚫🟡⚫⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡⚫⚫🟡⚫⚫\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫⚫⚫🟡🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫🟡🟡⚫🟡⚫⚫⚫\n⚫🟡🟡⚫⚫⚫⚫🟡\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡⚫⚫🟡⚫⚫🟡\n⚫⚫🟡⚫⚫🟡🟡🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫⚫🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫🟡⚫⚫\n⚫🟡🟡🟡⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡🟡🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡🟡🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡🟡🟡⚫⚫🟡\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫🟡🟡⚫🟡\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫🟡🟡⚫\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫🟡🟡🟡⚫⚫🟡⚫\n⚫⚫🟡⚫⚫⚫⚫⚫\n⚫🟡🟡🟡⚫⚫🟡🟡\n⚫🟡🟡⚫🟡⚫⚫🟡\n⚫🟡🟡⚫🟡🟡🟡⚫\n⚫🟡🟡⚫⚫⚫🟡🟡\n⚫🟡🟡⚫⚫🟡⚫🟡\n⚫⚫🟡⚫🟡🟡🟡⚫\n").exit(0)