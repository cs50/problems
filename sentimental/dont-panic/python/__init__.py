import check50


@check50.check()
def exists():
    """hack.py exists"""
    check50.exists("hack.py")
    check50.include("dont-panic.db")


@check50.check(exists)
def test_execution():
    """hack.py runs without error"""
    check50.run("python hack.py").exit(0)
