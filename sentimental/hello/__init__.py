import check50

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def prints_hello():
    """prints "hello, world\\n" """
    from re import match
    expected = "[Hh]ello, world!?\n"
    actual = check50.run("python3 hello.py").stdout()
    if not match(expected, actual):
        help = None
        if match(expected[:-1], actual):
            help = r'did you forget a newline ("\n") at the end of your string?'
        raise Mismatch("hello, world\n", actual, help=help)
