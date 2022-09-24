import check50
import check50.c


@check50.check()
def exists():
    """substitution.c exists"""
    check50.exists("substitution.c")


@check50.check(exists)
def compiles():
    """substitution.c compiles"""
    check50.c.compile("substitution.c", lcs50=True)


@check50.check(compiles)
def encrypt1():
    """encrypts "A" as "Z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("A").stdout("ciphertext:\s*Z\n", "ciphertext: Z\n").exit(0)


@check50.check(compiles)
def encrypt2():
    """encrypts "a" as "z" using ZYXWVUTSRQPONMLKJIHGFEDCBA as key"""
    check50.run("./substitution ZYXWVUTSRQPONMLKJIHGFEDCBA").stdin("a").stdout("ciphertext:\s*z\n", "ciphertext: z\n").exit(0)


@check50.check(compiles)
def encrypt3():
    """encrypts "ABC" as "NJQ" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("ABC").stdout("ciphertext:\s*NJQ\n", "ciphertext: NJQ\n").exit(0)


@check50.check(compiles)
def encrypt4():
    """encrypts "XyZ" as "KeD" using NJQSUYBRXMOPFTHZVAWCGILKED as key"""
    check50.run("./substitution NJQSUYBRXMOPFTHZVAWCGILKED").stdin("XyZ").stdout("ciphertext:\s*KeD\n", "ciphertext: KeD\n").exit(0)


@check50.check(compiles)
def encrypt5():
    """encrypts "This is CS50" as "Cbah ah KH50" using YUKFRNLBAVMWZTEOGXHCIPJSQD as key"""
    check50.run("./substitution YUKFRNLBAVMWZTEOGXHCIPJSQD").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compiles)
def encrypt6():
    """encrypts "This is CS50" as "Cbah ah KH50" using yukfrnlbavmwzteogxhcipjsqd as key"""
    check50.run("./substitution yukfrnlbavmwzteogxhcipjsqd").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compiles)
def encrypt7():
    """encrypts "This is CS50" as "Cbah ah KH50" using YUKFRNLBAVMWZteogxhcipjsqd as key"""
    check50.run("./substitution YUKFRNLBAVMWZteogxhcipjsqd").stdin("This is CS50").stdout("ciphertext:\s*Cbah ah KH50\n", "ciphertext: Cbah ah KH50\n").exit(0)


@check50.check(compiles)
def encrypt8():
    """encrypts all alphabetic characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("The quick brown fox jumps over the lazy dog").stdout("ciphertext:\s*Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n", "ciphertext: Rqx tokug wljif nja eozby jhxl rqx cdmv sjp\n").exit(0)


@check50.check(compiles)
def encrypt9():
    """does not encrypt non-alphabetical characters using DWUSXNPQKEGCZFJBTLYROHIAVM as key"""
    check50.run("./substitution DWUSXNPQKEGCZFJBTLYROHIAVM").stdin("Shh... Don't tell!").stdout("ciphertext:\s*Yqq... Sjf'r rxcc!\n", "ciphertext: Yqq... Sjf'r rxcc!\n").exit(0)


@check50.check(compiles)
def handles_no_argv():
    """handles lack of key"""
    check50.run("./substitution").exit(1)


@check50.check(compiles)
def handles_too_many_args():
    """handles too many arguments"""
    check50.run("./substitution abcdefghijklmnopqrstuvwxyz abc").exit(1)


@check50.check(compiles)
def handles_invalid_length():
    """handles invalid key length"""
    check50.run("./substitution QTXDGMKIPV").exit(1)


@check50.check(compiles)
def handles_invalid_key_chars():
    """handles invalid characters in key"""
    check50.run("./substitution ZWGKPMJ^YISHFEXQON[DLUACVT").exit(1)


@check50.check(compiles)
def handles_duplicate_chars_upper():
    """handles duplicate characters in uppercase key"""
    check50.run("./substitution FAZRDTMGQEJPWAXUSKVIYCLONH").exit(1)


@check50.check(compiles)
def handles_duplicate_chars_lower():
    """handles duplicate characters in lowercase key"""
    check50.run("./substitution fazrdtmgqejpwaxuskviyclonh").exit(1)


@check50.check(compiles)
def handles_multiple_duplicate_chars():
    """handles multiple duplicate characters in key"""
    check50.run("./substitution MMCcEFGHIJKLMNOPqRqTUVWXeZ").exit(1)
