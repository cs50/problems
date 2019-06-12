import check50

@check50.check()
def exists():
    """vigenere.py exists."""
    check50.exists("vigenere.py")

@check50.check(exists)
def aa():
    """encrypts "a" as "a" using "a" as keyword"""
    check50.run("python3 vigenere.py a").stdin("a").stdout("ciphertext:\s*a\n", "ciphertext: a\n").exit(0)

@check50.check(exists)
def bazbarfoo_caqgon():
    """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
    check50.run("python3 vigenere.py baz").stdin("barfoo").stdout("ciphertext:\s*caqgon\n", "ciphertext: caqgon\n").exit(0)

@check50.check(exists)
def mixedBaZBARFOO():
    """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
    check50.run("python3 vigenere.py BaZ").stdin("BaRFoo").stdout("ciphertext:\s*CaQGon\n", "ciphertext: CaQGon\n").exit(0)

@check50.check(exists)
def allcapsBAZBARFOO():
    """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
    check50.run("python3 vigenere.py BAZ").stdin("BARFOO").stdout("ciphertext:\s*CAQGON\n", "ciphertext: CAQGON\n").exit(0)

@check50.check(exists)
def bazworld():
    """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
    check50.run("python3 vigenere.py baz").stdin("world!$?").stdout("ciphertext:\s*xoqmd!\$\?\n", "ciphertext: xoqmd!$?\n").exit(0)

@check50.check(exists)
def withspaces():
    """encrypts "hello, world!" as "iekmo, vprke!" using "baz" as keyword"""
    check50.run("python3 vigenere.py baz").stdin("hello, world!").stdout("ciphertext:\s*iekmo, vprke!\n", "ciphertext: iekmo, vprke!\n").exit(0)

@check50.check(exists)
def noarg():
    """handles lack of argv[1]"""
    check50.run("python3 vigenere.py").exit(1)

@check50.check(exists)
def toomanyargs():
    """handles argc > 2"""
    check50.run("python3 vigenere.py 1 2 3").exit(1)

@check50.check(exists)
def reject():
    """rejects "Hax0r2" as keyword"""
    check50.run("python3 vigenere.py Hax0r2").exit(1)
