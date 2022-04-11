import check50


@check50.check()
def exists():
    """deep.py exists"""
    check50.exists("deep.py")


@check50.check(exists)
def test42():
    """input of 42 yields output of Yes"""
    check50.run("python3 deep.py").stdin("42", prompt=True).stdout("[Yy]es", "Yes", regex=True).exit()


@check50.check(exists)
def testfortytwo():
    """input of forty-two yields output of Yes"""
    check50.run("python3 deep.py").stdin("forty-two", prompt=True).stdout("[Yy]es", "Yes", regex=True).exit()


@check50.check(exists)
def testforty_two():
    """input of forty two yields output of Yes"""
    check50.run("python3 deep.py").stdin("forty two", prompt=True).stdout("[Yy]es", "Yes", regex=True).exit()


@check50.check(exists)
def testforty_two_malformed():
    """input of FoRty TwO yields output of Yes"""
    check50.run("python3 deep.py").stdin("FoRty TwO", prompt=True).stdout("[Yy]es", "Yes", regex=True).exit()


@check50.check(exists)
def test42_spaces():
    """input of 42, with spaces on either side, yields output of Yes"""
    check50.run("python3 deep.py").stdin(" 42 ", prompt=True).stdout("[Yy]es", "Yes", regex=True).exit()


@check50.check(exists)
def test50():
    """input of 50 yields output of No"""
    check50.run("python3 deep.py").stdin("50", prompt=True).stdout("[Nn]o", "No", regex=True).exit()


@check50.check(exists)
def testfifty():
    """input of fifty yields output of No"""
    check50.run("python3 deep.py").stdin("fifty", prompt=True).stdout("[Nn]o", "No", regex=True).exit()