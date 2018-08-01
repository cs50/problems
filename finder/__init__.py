import check50
import check50.c

@check50.check()
def exists():
    """finder.c exists."""
    check50.exists("finder.c")

@check50.check(exists)
def compiles():
    """finder.c compiles."""
    check50.c.compile("finder.c", lcs50=True)

@check50.check(compiles)
def test_handles_lack_of_arguments():
    """handles lack of arguments"""
    check50.run("./finder").exit(1)

@check50.check(compiles)
def test_handles_too_many_arguments():
    """handles too many arguments"""
    check50.run("./finder x y z").exit(1)

@check50.check(compiles)
def test_cats():
    """finds cats in cats.txt"""
    check50.include("FOO", "BAR", "THIS", "CATS.txt", "DOGS.txt", "001.txt")
    check50.run("./finder cats").stdout()
    check_output(open("found.txt").read(), open("001.txt").read())

@check50.check(compiles)
def test_foo1():
    """finds foo with argc == 2"""
    check50.include("FOO", "BAR", "THIS", "CATS.txt", "DOGS.txt", "002.txt")
    check50.run("./finder foo").stdout()
    check_output(open("found.txt").read(), open("002.txt").read())

@check50.check(compiles)
def test_foo2():
    """finds foo with argc == 3"""
    check50.include("FOO", "BAR", "THIS", "CATS.txt", "DOGS.txt", "003.txt")
    check50.run("./finder foo ./").stdout()
    check_output(open("found.txt").read(), open("003.txt").read())

@check50.check(compiles)
def test_foo3():
    """finds foo in foo/"""
    check50.include("FOO", "BAR", "THIS", "CATS.txt", "DOGS.txt", "004.txt")
    check50.run("./finder foo FOO/").stdout()
    check_output(open("found.txt").read(), open("004.txt").read())

@check50.check(compiles)
def test_common():
    """finds common starting at ./"""
    check50.include("FOO", "BAR", "this", "CATS.txt", "DOGS.txt", "005.txt")
    check50.run("./finder common").stdout()
    check_output(open("found.txt").read(), open("005.txt").read())


def check_output(output, correct):
    if output == correct:
        return

    raise check50.Mismatch(correct, output)
