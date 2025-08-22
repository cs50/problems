import check50
from re import search
from re import findall

@check50.check()
def exists():
    """answers.txt exists"""
    check50.exists("answers.txt")

@check50.check(exists)
def answers():
    """answers all questions"""
    content = open("answers.txt", "r").read()
    if "TODO" in content:
        raise check50.Failure("Not all questions answered.")

@check50.check(exists)
def sorts():
    """correctly identifies each sort"""

    check50.log("checking that sorts are classified correctly...")

    expected = ["sort1 uses:\s*[Bb][Uu][Bb][Bb][Ll][Ee]", "sort2 uses:\s*[Mm][Ee][Rr][Gg][Ee]", "sort3 uses:\s*[Ss][Ee][Ll][Ee][Cc][Tt][Ii][Oo][Nn]"]
    actual = open("answers.txt", "r").read()

    for e in expected:
        if not search(e, actual):
            raise check50.Failure("Incorrect assignment of sorts.")

