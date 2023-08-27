import check50
import check50.c
import re


@check50.check()
def exists():
    """wordle.c exists"""
    check50.exists("wordle.c")
    check50.include("testing.c")
    check50.include("5.txt")


@check50.check(exists)
def compiles():
    """wordle.c compiles"""

    # Check if student code compiles
    check50.c.compile("wordle.c", lcs50=True)

    # Rename main function to "distro_main"
    wordle = re.sub("int\s+main", "int distro_main", open("wordle.c").read())

    # Read testing file
    testing = open("testing.c").read()

    # Combine student code and testing file
    with open("wordle_test.c", "w") as f:
        f.write(wordle)
        f.write("\n")
        f.write(testing)

    check50.c.compile("wordle_test.c", lcs50=True)


@check50.check(compiles)
def multiple_argv():
    """wordle rejects multiple command-line arguments"""
    check50.c.run("./wordle 5 5").exit(1)


@check50.check(compiles)
def zero_argv():
    """wordle rejects 0 command-line arguments"""
    check50.c.run("./wordle").exit(1)


@check50.check(compiles)
def reject_input():
    """wordle rejects inputs that are not 5, 6, 7, or 8"""
    for i in [3, 4, 9]:
        check50.c.run(f"./wordle {i}").exit(1)


@check50.check(compiles)
def reject_length():
    """wordle rejects guesses that are not of appropriate length"""
    for word in ["cs50", "wordle", "please"]:
        check50.c.run("./wordle_test get_guess").stdin(word).stdout("Input a 5-letter word:")


@check50.check(compiles)
def accept_length():
    """wordle accepts guesses of appropriate length"""
    for word in ["audio", "video", "cable"]:
        check50.c.run("./wordle_test get_guess").stdin(word).stdout(word)


@check50.check(compiles)
def incorrect_guess():
    """wordle recognizes guess with no matches"""
    for word in ["movie", "poker", "child"]:
        check50.c.run(f"./wordle_test check_word staff {word}").stdout(0)


@check50.check(compiles)
def partial_match_close():
    """wordle recognizes guess with close match"""
    for word in ["smile", "bison", "links"]:
        check50.c.run(f"./wordle_test check_word crash {word}").stdout(1)


@check50.check(compiles)
def partial_match_exact():
    """wordle recognizes guess with exact match"""
    for word in ["squid", "claim", "fluke"]:
        check50.c.run(f"./wordle_test check_word stare {word}").stdout(2)


@check50.check(compiles)
def partial_match_exact_and_close():
    """wordle recognizes guess with exact and close matches"""
    for word in ["agent", "burst", "canoe"]:
        check50.c.run(f"./wordle_test check_word arise {word}").stdout(3)

        
@check50.check(compiles)
def partial_multiple_matches():
    """wordle recognizes guess with multiple matches"""
    for word in ["drops", "ghost", "ports"]:
        check50.c.run(f"./wordle_test check_word sport {word}").stdout(5)


@check50.check(compiles)
def exact_match():
    """wordle recognizes correct guess"""
    for word in ["gnome", "sized", "world", "grill"]:
        check50.c.run(f"./wordle_test check_word {word} {word}").stdout(10)
