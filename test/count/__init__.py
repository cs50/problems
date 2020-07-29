import check50
import check50.c

@check50.check()
def compiles():
    check50.exists("count.c")
    check50.include("1.txt", "2.txt", "3.txt", "4.txt")
    check50.c.compile("count.c", lcs50=True)

@check50.check(compiles)
def test1():
    """count correctly counts file with all ASCII characters"""
    check50.run("./count 1.txt").stdout("Number of characters: 7\n").exit()

@check50.check(compiles)
def test2():
    """count correctly counts file with a two-byte character"""
    check50.run("./count 2.txt").stdout("Number of characters: 28\n").exit()

@check50.check(compiles)
def test3():
    """count correctly counts file with multiple emoji"""
    check50.run("./count 3.txt").stdout("Number of characters: 29\n").exit()

@check50.check(compiles)
def test4():
    """count correctly counts file with one, two and four-byte characters"""
    check50.run("./count 4.txt").stdout("Number of characters: 27\n").exit()
