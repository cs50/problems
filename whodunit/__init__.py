import check50
import check50.c

@check50.check()
def exists():
    """whodunit.c exists"""
    check50.exists("whodunit.c")

@check50.check(exists)
def compiles():
    """whodunit.c compiles"""
    check50.include("bmp.h")
    check50.c.compile("whodunit.c", lcs50=True)

@check50.check(compiles)
def different():
    """whodunit.c alters the image"""
    check50.include("clue.bmp")
    check50.run("./whodunit clue.bmp verdict.bmp").exit()
    if check50.hash("verdict.bmp") == check50.hash("clue.bmp"):
        raise check50.Failure("output image is identical to clue.bmp")
