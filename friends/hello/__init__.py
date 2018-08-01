import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def test_hello_world():
    """prints "Hello, world!\n" if argv[1] is "world" """
    check50.run("./hello world").stdout("Hello, world!\n").exit(0)

@check50.check(compiles)
def test_hello_elphie():
    """prints "Hello, elphie!\n" if argv[1] is "elphie" """
    check50.run("./hello elphie").stdout("Hello, elphie!\n").exit(0)

@check50.check(compiles)
def test_lack_of_arguments():
    """handles lack of command line arguments"""
    check50.run("./hello").exit(1)

@check50.check(compiles)
def test_too_many_arguments():
    """handles too many command line arguments"""
    check50.run("./hello milo mochi elphie").exit(1)
