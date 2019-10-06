import check50
import check50.c


@check50.check()
def exists():
    """dictionary.c, dictionary.h, and Makefile exist"""
    check50.exists("dictionary.c", "dictionary.h")


@check50.check(exists)
def compiles():
    """speller compiles"""
    check50.include("speller.c", "Makefile")
    check50.run("make").exit(0)


@check50.check(compiles)
def basic():
    """handles most basic words properly"""
    check50.include("basic")
    check50.run("./speller basic/dict basic/text").stdout(open("basic/out")).exit(0)


@check50.check(compiles)
def min_length():
    """handles min length (1-char) words"""
    check50.include("min_length")
    check50.run("./speller min_length/dict min_length/text").stdout(open("min_length/out")).exit(0)


@check50.check(compiles)
def max_length():
    """handles max length (45-char) words"""
    check50.include("max_length")
    check50.run("./speller max_length/dict max_length/text").stdout(open("max_length/out")).exit(0)


@check50.check(compiles)
def apostrophe():
    """handles words with apostrophes properly"""
    check50.include("apostrophe")
    check50.run("./speller apostrophe/without/dict apostrophe/with/text").stdout(open("apostrophe/outs/without-with")).exit(0)
    check50.run("./speller apostrophe/with/dict apostrophe/without/text").stdout(open("apostrophe/outs/with-without")).exit(0)
    check50.run("./speller apostrophe/with/dict apostrophe/with/text").stdout(open("apostrophe/outs/with-with")).exit(0)


@check50.check(compiles)
def case():
    """spell-checking is case-insensitive"""
    check50.include("case")
    check50.run("./speller case/dict case/text").stdout(open("case/out")).exit(0)


@check50.check(compiles)
def substring():
    """handles substrings properly"""
    check50.include("substring")
    check50.run("./speller substring/dict substring/text").stdout(open("substring/out")).exit(0)


@check50.check(substring)
def memory():
    """program is free of memory errors"""
    check50.c.valgrind("./speller substring/dict substring/text").stdout(open("substring/out"), timeout=10).exit(0)
