import check50


@check50.check()
def exists():
    """jars.py and test_jars.py exist"""
    check50.exists("jar.py")
    check50.include("test_file.py")


@check50.check(exists)
def test_init():
    """Jar's constructor initializes a cookie jar with given capacity"""
    check50.run("pytest test_file.py -k 'test_init'").exit(0)


@check50.check(exists)
def test_init_value_error():
    """Jar's constructor raises ValueError when called with negative capacity"""
    check50.run("pytest test_file.py -k 'test_raises_value_error'").exit(0)


@check50.check(exists)
def test_empty_str():
    """Empty jar prints zero cookies"""
    check50.run("pytest test_file.py -k 'test_empty_str'").exit(0)


@check50.check(exists)
def test_full_str():
    """Jar prints total number of cookies deposited"""
    check50.run("pytest test_file.py -k 'test_full_str'").exit(0)


@check50.check(exists)
def test_too_full():
    """Jar's deposit method raises ValueError when deposited cookies exceed the jar's capacity"""
    check50.run("pytest test_file.py -k 'test_too_full'").exit(0)


@check50.check(exists)
def test_withdraw():
    """Jar's withdraw method removes cookies from the jar's size"""
    check50.run("pytest test_file.py -k 'test_withdraw'").exit(0)


@check50.check(exists)
def test_empty():
    """Jar's withdraw method raises ValueError when withdrawn cookies exceed jar's size"""
    check50.run("pytest test_file.py -k 'test_empty'").exit(0)