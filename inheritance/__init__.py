import check50
import check50.c
import re

@check50.check()
def exists():
    """inheritance.c exists"""
    check50.exists("inheritance.c")
    check50.include("testing.c")

@check50.check(exists)
def compiles():
    """inheritance.c compiles"""
    check50.c.compile("inheritance.c", lcs50=True)

@check50.check(exists)
def compiles():
    """inheritance compiles"""
    check50.c.compile("inheritance.c", lcs50=True)
    inheritance = re.sub("int\s+main", "int distro_main", open("inheritance.c").read())
    testing = open("testing.c").read()
    with open("inheritance_test.c", "w") as f:
        f.write(inheritance)
        f.write("\n")
        f.write(testing)
    check50.c.compile("inheritance_test.c", lcs50=True)

@check50.check(compiles)
def correct_size():
    """create_family creates correct size of family"""
    check50.run("./inheritance_test").stdout("size_true.*").exit(0)


@check50.check(compiles)
def inheritance_rules_1():
    """create_family follows inheritance rules 1"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles)
def inheritance_rules_2():
    """create_family follows inheritance rules 2"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles)
def inheritance_rules_3():
    """create_family follows inheritance rules 3"""
    check50.run("./inheritance_test").stdout(".*allele_true.*").exit(0)

@check50.check(compiles)
def frees_memory():
    """free_family results in no memory leakages"""
    check50.c.valgrind("./inheritance").exit(0)