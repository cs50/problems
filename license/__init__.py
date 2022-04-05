import check50


@check50.check()
def exists():
    """license.py exists"""
    check50.exists("license.py")

@check50.check(exists)
def testPython():
    """input of PYTHON yields PYTHN"""
    check50.run("python3 license.py").stdin("PYTHON", prompt=False).stdout("PYTHN").exit()

@check50.check(exists)
def testProgrammer():
    """input of PROGRAMMER yields PRGRMMR"""
    check50.run("python3 license.py").stdin("PROGRAMMER", prompt=False).stdout("PRGRMMR").exit()

@check50.check(exists)
def testCS50():
    """input of CS50 yields CS50"""
    check50.run("python3 license.py").stdin("CS50", prompt=False).stdout("CS50").exit()