import check50
import check50.c
import random

# Scrabble points table for each letter (A-Z)
POINTS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Generate a list of letters that have one point in Scrabble
ONE_POINT_LETTERS = [chr(i + ord('a')) for i in range(26) if POINTS[i] == 1]

# Create a mapping of letters to their Scrabble points
POINTS_TABLE = {chr(i + ord('a')): POINTS[i] for i in range(26)}

# Store the comparison results POINTS[i+1] - POINTS[i] for each letter
POINTS_ORDER = [POINTS[i + 1] - POINTS[i] for i in range(len(POINTS) - 1)]

# Prepare a list of results based on the POINTS_ORDER (positive means player 2 wins, negative means player 1 wins, 0 means tie)
PLAYER_1_WINS = ("[Pp]layer 1 [Ww]ins!?", "Player 1 wins!")
PLAYER_2_WINS = ("[Pp]layer 2 [Ww]ins!?", "Player 2 wins!")
TIE = ("[Tt]ie!?", "Tie!")

# Create a list of results based on the POINTS_ORDER
RESULTS = []
for i in range(len(POINTS_ORDER)):
    if POINTS_ORDER[i] > 0:
        RESULTS.append(PLAYER_2_WINS)
    elif POINTS_ORDER[i] < 0:
        RESULTS.append(PLAYER_1_WINS)
    else:
        RESULTS.append(TIE)

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
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout(*TIE).exit(0)

@check50.check(compiles)
def tie_punctuation():
    """handles punctuation correctly"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout(*TIE).exit(0)

@check50.check(compiles)
def test1():
    """correctly identifies 'Question?' and 'Question!' as a tie"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout(*TIE).exit(0)

@check50.check(compiles)
def test2():
    """correctly identifies 'drawing' and 'illustration' as a tie"""
    check50.run("./scrabble").stdin("drawing").stdin("illustration").stdout(*TIE).exit(0)

@check50.check(compiles)
def test3():
    """correctly identifies 'hai!' as winner over 'Oh,'"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout(*PLAYER_2_WINS).exit(0)

@check50.check(compiles)
def test4():
    """correctly identifies 'COMPUTER' as winner over 'science'"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout(*PLAYER_1_WINS).exit(0)

@check50.check(compiles)
def test5():
    """correctly identifies 'Scrabble' as winner over 'wiNNeR'"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout(*PLAYER_1_WINS).exit(0)

@check50.check(compiles)
def test6():
    """correctly identifies 'pig' as winner over 'dog'"""
    check50.run("./scrabble").stdin("pig").stdin("dog").stdout(*PLAYER_1_WINS).exit(0)

@check50.check(compiles)
def complex_case():
    """correctly identifies 'Skating!' as winner over 'figure?'"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout(*PLAYER_2_WINS).exit(0)

@check50.check(complex_case)
def test_strict_order():
    """correctly identifies winner between random words"""
    indices = random.sample(range(len(POINTS)-1), min(5, len(POINTS)-1))
    for i in indices:
        check50.run("./scrabble").stdin(chr(i + ord('a'))).stdin(chr(i + 1 + ord('a'))).stdout(*RESULTS[i]).exit(0)

@check50.check(test_strict_order)
def test_scoring_accuracy():
    """implementation correctly calculates scores using the Scrabble points table"""
    letters = random.sample(list(POINTS_TABLE.items()), 5)
    for letter, points in letters:
        check50.run("./scrabble").stdin(letter).stdin(f'{random.choice(ONE_POINT_LETTERS) * points}').stdout(f"[Tt]ie!?", "Tie!").exit(0)