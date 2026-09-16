import check50
import check50.c

@check50.check()
def exists():
    """caesar.c exists."""
    check50.exists("caesar.c")

@check50.check(exists)
def compiles():
    """caesar.c compiles."""
    check50.c.compile("caesar.c", lcs50=True)

@check50.check(compiles)
def rejects_negative_key():
    """rejects a key of -1"""
    check50.run("./caesar").stdin("-1").reject()

@check50.check(compiles)
def rejects_non_numeric_key():
    """rejects a non-numeric key of "banana" """
    check50.run("./caesar").stdin("banana").reject()

@check50.check(compiles)
def reprompts_for_key():
    """rejects -1 and "banana" as keys before accepting 1"""
    check50.run("./caesar") \
        .stdin("-1").reject() \
        .stdin("banana").reject() \
        .stdin("1").stdin("a") \
        .stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_a_as_b():
    """encrypts "a" as "b" using 1 as key"""
    check50.run("./caesar").stdin("1").stdin("a") \
        .stdout("[Cc]iphertext:\s*b\n", "ciphertext: b\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_yxocll():
    """encrypts "barfoo" as "yxocll" using 23 as key"""
    check50.run("./caesar").stdin("23").stdin("barfoo") \
        .stdout("[Cc]iphertext:\s*yxocll\n", "ciphertext: yxocll\n").exit(0)

@check50.check(compiles)
def encrypts_BARFOO_as_EDUIRR():
    """encrypts "BARFOO" as "EDUIRR" using 3 as key"""
    check50.run("./caesar").stdin("3").stdin("BARFOO") \
        .stdout("[Cc]iphertext:\s*EDUIRR\n", "ciphertext: EDUIRR\n").exit(0)

@check50.check(compiles)
def encrypts_BaRFoo_FeVJss():
    """encrypts "BaRFoo" as "FeVJss" using 4 as key"""
    check50.run("./caesar").stdin("4").stdin("BaRFoo") \
        .stdout("[Cc]iphertext:\s*FeVJss\n", "ciphertext: FeVJss\n").exit(0)

@check50.check(compiles)
def encrypts_barfoo_as_onesbb():
    """encrypts "barfoo" as "onesbb" using 65 as key"""
    check50.run("./caesar").stdin("65").stdin("barfoo") \
        .stdout("[Cc]iphertext:\s*onesbb\n", "ciphertext: onesbb\n").exit(0)

@check50.check(compiles)
def checks_for_handling_non_alpha():
    """encrypts "world, say hello!" as "iadxp, emk tqxxa!" using 12 as key"""
    check50.run("./caesar").stdin("12").stdin("world, say hello!") \
        .stdout("[Cc]iphertext:\s*iadxp, emk tqxxa!\n", "ciphertext: iadxp, emk tqxxa!\n").exit(0)
