import check50
import check50.c

@check50.check()
def exists():
    """vigenere.c exists."""
    check50.exists("vigenere.c")

@check50.check(exists)
def compiles():
    """vigenere.c compiles."""
    check50.c.compile("vigenere.c", lcs50=True)

@check50.check(compiles)
def aa():
    """encrypts "a" as "a" using "a" as keyword"""
    check50.run("./vigenere a").stdin("a").stdout("ciphertext:\s*a\n", "ciphertext: a\n").exit(0)

@check50.check(compiles)
def bazbarfoo_caqgon():
    """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
    check50.run("./vigenere baz").stdin("barfoo").stdout("ciphertext:\s*caqgon\n", "ciphertext: caqgon\n").exit(0)

@check50.check(compiles)
def mixedBaZBARFOO():
    """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
    check50.run("./vigenere BaZ").stdin("BaRFoo").stdout("ciphertext:\s*CaQGon\n", "ciphertext: CaQGon\n").exit(0)

@check50.check(compiles)
def allcapsBAZBARFOO():
    """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
    check50.run("./vigenere BAZ").stdin("BARFOO").stdout("ciphertext:\s*CAQGON\n", "ciphertext: CAQGON\n").exit(0)

@check50.check(compiles)
def bazworld():
    """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
    check50.run("./vigenere baz").stdin("world!$?").stdout("ciphertext:\s*xoqmd!\$\?\n", "ciphertext: xoqmd!$?\n").exit(0)

@check50.check(compiles)
def withspaces():
    """encrypts "hello, world!" as "iekmo, vprke!" using "baz" as keyword"""
    check50.run("./vigenere baz").stdin("hello, world!").stdout("ciphertext:\s*iekmo, vprke!\n", "ciphertext: iekmo, vprke!\n").exit(0)

@check50.check(compiles)
def noarg():
    """handles lack of argv[1]"""
    check50.run("./vigenere").exit(1)

@check50.check(compiles)
def toomanyargs():
    """handles argc > 2"""
    check50.run("./vigenere 1 2 3").exit(1)

@check50.check(compiles)
def reject():
    """rejects "Hax0r2" as keyword"""
    check50.run("./vigenere Hax0r2").exit(1)
