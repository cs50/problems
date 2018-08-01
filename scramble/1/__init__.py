import check50
import check50.c

@check50.check()
def exists():
    """scramble.c exists."""
    check50.exists("scramble.c")
    check50.include("words.txt")

@check50.check(exists)
def compiles():
    """scramble.c compiles."""
    check50.c.compile("scramble.c", lcs50=True)

@check50.check(compiles)
def draw3():
    """draws board #3 correctly"""
    check50.run("./scramble 3").stdout("\s*N\s*E\s*H\s*I\n\s*E\s*D\s*N\s*T\n\s*T\s*E\s*A\s*I\n\s*E\s*O\s*V\s*T","  N E H I\n  E D N T\n  T E A I\n  E O V T").stdout(">")

@check50.check(compiles)
def draw5():
    """draws board #5 correctly"""
    check50.run("./scramble 5").stdout("\s*E\s*A\s*Y\s*A\n\s*D\s*A\s*E\s*I\n\s*L\s*T\s*A\s*E\n\s*W\s*E\s*I\s*E", "  E A Y A\n  D A E I\n  L T A E\n  W E I E").stdout(">")

@check50.check(compiles)
def lookup10():
    """user can only score a word once"""
    check50.run("./scramble 10").stdin("line").stdout("Score: 4").stdin("line").stdout("Score: 4").stdout("Time: .*\n\n>")

@check50.check(compiles)
def lookup15():
    """checks if user entries exist in words.txt"""
    check50.run("./scramble 15").stdin("hhh").stdout("Score: 0").stdin("leh").stdout("Score: 0").stdout("Time: .*\n\n>")

@check50.check(compiles)
def scramble5():
    """scrambles board #5 correctly"""
    check50.run("./scramble 5").stdin("scramble").stdout("\s*W\s*L\s*D\s*E\n\s*E\s*T\s*A\s*A\n\s*I\s*A\s*E\s*Y\n\s*E\s*E\s*I\s*A", "  W L D E\n  E T A A\n  I A E Y\n  E E I A")

@check50.check(compiles)
def scramble7():
    """scrambles board #7 correctly"""
    check50.run("./scramble 7").stdin("scramble").stdout("\s*S\s*N\s*A\s*L\n\s*S\s*A\s*L\s*T\n\s*T\s*M\s*Y\s*N\n\s*D\s*B\s*A\s*E", "  S N A L\n  S A L T\n  T M Y N\n  D B A E")
