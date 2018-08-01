import check50
import check50.c

@check50.check()
def exists():
    """finder.c exists."""
    check50.include("FOO", "BAR", "this", "CATS.txt", "DOGS.txt")
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
    check_found("cats", expected="001.txt")

@check50.check(compiles)
def test_foo1():
    """finds foo with argc == 2"""
    check_found("foo", expected="002.txt")

@check50.check(compiles)
def test_foo2():
    """finds foo with argc == 3"""
    check_found("foo", "./", expected="003.txt")

@check50.check(compiles)
def test_foo3():
    """finds foo in foo/"""
    check_found("foo", "FOO/", expected="004.txt")

@check50.check(compiles)
def test_common():
    """finds common starting at ./"""
    check_found("common", expected="005.txt")


def check_found(*args, expected=None):
    check50.run(f"./finder {' '.join(args)}").exit(0)
    check50.exists("found.txt")

    with open("found.txt") as f:
        actual_found = f.read()

    check50.include(expected)
    with open(expected) as f:
        expected_found = f.read()

    if actual_found != expected_found:
        raise check50.Mismatch(expected_found, actual_found)
