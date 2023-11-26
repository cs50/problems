import check50
import check50.c
import re


@check50.check()
def exists():
    """plurality.c exists"""
    check50.exists("plurality.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """plurality compiles"""
    check50.c.compile("plurality.c", lcs50=True)
    plurality = re.sub("int\s+main", "int distro_main", open("plurality.c").read())
    testing = open("testing.c").read()
    with open("plurality_test.c", "w") as f:
        f.write(plurality)
        f.write("\n")
        f.write(testing)
    check50.c.compile("plurality_test.c", lcs50=True)


@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_first():
    """vote returns true when given name of first candidate"""
    check50.run("./plurality_test 0 0").stdout("true").exit(0)


@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_middle():
    """vote returns true when given name of middle candidate"""
    check50.run("./plurality_test 0 1").stdout("true").exit(0)


@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_finds_name_last():
    """vote returns true when given name of last candidate"""
    check50.run("./plurality_test 0 2").stdout("true").exit(0)


@check50.check(compiles)
@check50.hidden("vote function did not return false")
def vote_returns_false():
    """vote returns false when given name of invalid candidate"""
    check50.run("./plurality_test 0 3").stdout("false").exit(0)


@check50.check(compiles)
@check50.hidden("vote function did not correctly update vote totals")
def first_vote_totals_correct():
    """vote produces correct counts when all votes are zero"""
    check50.run("./plurality_test 0 4").stdout("1 0 0").exit(0)


@check50.check(compiles)
@check50.hidden("vote function did not correctly update vote totals")
def subsequent_vote_totals_correct():
    """vote produces correct counts after some have already voted"""
    check50.run("./plurality_test 0 5").stdout("2 8 0").exit(0)


@check50.check(compiles)
@check50.hidden("vote function modified vote totals incorrectly")
def invalid_vote_votes_unchanged():
    """vote leaves vote counts unchanged when voting for invalid candidate"""
    check50.run("./plurality_test 0 6").stdout("2 8 0").exit(0)


@check50.check(compiles)
def print_winner0():
    """print_winner identifies Alice as winner of election"""
    out = check50.run("./plurality_test 0 7").stdout()
    check_winner(out, "Alice\n")


@check50.check(compiles)
def print_winner1():
    """print_winner identifies Bob as winner of election"""
    out = check50.run("./plurality_test 0 8").stdout()
    check_winner(out, "Bob\n")


@check50.check(compiles)
def print_winner2():
    """print_winner identifies Charlie as winner of election"""
    out = check50.run("./plurality_test 0 9").stdout()
    check_winner(out, "Charlie\n")


@check50.check(compiles)
@check50.hidden("print_winner function did not print both winners of election")
def print_winner3():
    """print_winner prints multiple winners in case of tie"""
    result = check50.run("./plurality_test 0 10").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)


@check50.check(compiles)
@check50.hidden("print_winner function did not print all three winners of election")
def print_winner4():
    """print_winner prints all names when all candidates are tied"""
    result = check50.run("./plurality_test 0 11").stdout()
    if set(result.split("\n")) - {""} != {"Alice", "Bob", "Charlie"}:
        raise check50.Mismatch("Alice\nBob\nCharlie\n", result)


# Note that check needs to be unhidden in order for help to be displayed
def check_winner(result, correct):
    if result == correct:
        return

    help = None
    r = result.rstrip()
    c = correct.rstrip()
    if r == c:
        if result[-1] == "\n":
            if result[-2].isspace():
                help = "did you print an extra space?"
        elif result[-1].isspace():
            help = "did you print a space instead of a newline?"
        else:
            help = "did you forget the newline after the name?"

    raise check50.Mismatch(correct, result, help=help)
