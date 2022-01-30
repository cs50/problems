import check50
import check50.c
import re


@check50.check()
def exists():
    """tideman.c exists"""
    check50.exists("tideman.c")
    check50.include("testing.c")


@check50.check(exists)
def compiles():
    """tideman compiles"""
    check50.c.compile("tideman.c", lcs50=True)
    tideman = re.sub("int\s+main", "int distro_main", open("tideman.c").read())
    testing = open("testing.c").read()
    with open("tideman_test.c", "w") as f:
        f.write(tideman)
        f.write("\n")
        f.write(testing)
    check50.c.compile("tideman_test.c", lcs50=True)

@check50.check(compiles)
@check50.hidden("vote function did not return true")
def vote_returns_true():
    """vote returns true when given name of candidate"""
    check50.run("./tideman_test 0 0").stdout("true").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not return false")
def vote_returns_false():
    """vote returns false when given name of invalid candidate"""
    check50.run("./tideman_test 0 1").stdout("false").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not correctly set ranks")
def vote_sets_rank():
    """vote correctly sets rank for first preference"""
    check50.run("./tideman_test 0 2").stdout("1").exit(0)

@check50.check(compiles)
@check50.hidden("vote function did not correctly set ranks")
def vote_sets_all_rank():
    """vote correctly sets rank for all preferences"""
    check50.run("./tideman_test 0 2").stdout("1 2 0").exit(0)

@check50.check(compiles)
@check50.hidden("record_preferences function did not correctly set preferences")
def record_prefs_first():
    """record_preferences correctly sets preferences for first voter"""
    check50.run("./tideman_test 0 3").stdout("0 0 0 1 0 1 1 0 0 ").exit(0)

@check50.check(compiles)
@check50.hidden("record_preferences function did not correctly set preferences")
def record_prefs_all():
    """record_preferences correctly sets preferences for all voters"""
    check50.run("./tideman_test 0 4").stdout("0 2 2 4 0 5 3 5 0").exit(0)

@check50.check(compiles)
@check50.hidden("add_pairs function did not produce 3 pairs")
def add_pairs1():
    """add_pairs generates correct pair count when no ties"""
    check50.run("./tideman_test 1 5").stdout("3").exit(0)

@check50.check(compiles)
@check50.hidden("add_pairs function did not produce 2 pairs")
def add_pairs2():
    """add_pairs generates correct pair count when ties exist"""
    check50.run("./tideman_test 2 5").stdout("2").exit(0)

@check50.check(compiles)
@check50.hidden("add_pairs function did not produce correct pairs")
def add_pairs3():
    """add_pairs fills pairs array with winning pairs"""
    check50.run("./tideman_test 1 6").stdout("true true true ").exit(0)

@check50.check(compiles)
@check50.hidden("add_pairs function did not produce correct pairs")
def add_pairs4():
    """add_pairs does not fill pairs array with losing pairs"""
    check50.run("./tideman_test 1 7").stdout("0").exit(0)

@check50.check(compiles)
@check50.hidden("sort_pairs did not correctly sort pairs")
def sort_pairs1():
    """sort_pairs sorts pairs of candidates by margin of victory"""
    check50.run("./tideman_test 3 8").stdout("0 2 0 1 2 1 ").exit(0)

@check50.check(compiles)
@check50.hidden("lock_pairs did not lock all pairs")
def lock_pairs1():
    """lock_pairs locks all pairs when no cycles"""
    check50.run("./tideman_test 5 16").stdout("false false false true false true false false false false false false false false false false false false false true false false true false false ").exit(0)

@check50.check(compiles)
@check50.hidden("lock_pairs did not correctly lock all non-cyclical pairs")
def lock_pairs2():
    """lock_pairs skips final pair if it creates cycle"""
    check50.run("./tideman_test 6 14").stdout("false true false false false false false false false false true false false false false false false false false false false false false true false false true true false false false false false false false false ").exit(0)

@check50.check(compiles)
@check50.hidden("lock_pairs did not correctly lock all non-cyclical pairs")
def lock_pairs3():
    """lock_pairs skips middle pair if it creates a cycle"""
    check50.run("./tideman_test 5 15").stdout("false false false false false false false false true false true false false false false false false false false false false true true false false ").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner did not print winner of election")
def print_winner1():
    """print_winner prints winner of election when one candidate wins over all others"""
    check50.run("./tideman_test 4 12").stdout("^Alice\n?$").exit(0)

@check50.check(compiles)
@check50.hidden("print_winner did not print winner of election")
def print_winner2():
    """print_winner prints winner of election when some pairs are tied"""
    check50.run("./tideman_test 4 13").stdout("^Charlie\n?$").exit(0)
