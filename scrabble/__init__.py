import check50
import check50.c

@check50.check()
def exists():
    """scrabble.c exists"""
    check50.exists("scrabble.c")

@check50.check(exists)
def compiles():
    """scrabble.c compiles"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compiles)
def tie_letter_case():
    """handles letter cases correctly"""
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def tie_punctuation():
    """handles punctuation correctly"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test1():
    """correctly identifies 'Question?' and 'Question!' as a tie"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test2():
    """correctly identifies 'drawing' and 'illustration' as a tie"""
    check50.run("./scrabble").stdin("drawing").stdin("illustration").stdout("[Tt]ie!?", "Tie!").exit(0)

@check50.check(compiles)
def test3():
    """correctly identifies 'hai!' as winner over 'Oh,'"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

@check50.check(compiles)
def test4():
    """correctly identifies 'COMPUTER' as winner over 'science'"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test5():
    """correctly identifies 'Scrabble' as winner over 'wiNNeR'"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def test6():
    """correctly identifies 'pig' as winner over 'dog'"""
    check50.run("./scrabble").stdin("pig").stdin("dog").stdout("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!").exit(0)

@check50.check(compiles)
def complex_case():
    """correctly identifies 'Skating!' as winner over 'figure?'"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!").exit(0)

