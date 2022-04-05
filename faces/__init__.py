import check50

@check50.check()
def exists():
    """faces.py exists"""
    check50.exists("faces.py")

@check50.check(exists)
def testHello():
    """input of \"Hello :)\" yields output of \"Hello 🙂\""""
    output = check50.run("python3 faces.py").stdin("Hello :)", prompt=False).stdout("Hello 🙂").exit()

@check50.check(exists)
def testGoodbye():
    """input of \"Goodbye :(\" yields output of \"Goodbye 🙁\""""
    output = check50.run("python3 faces.py").stdin("Goodbye :(", prompt=False).stdout("Goodbye 🙁").exit()

@check50.check(exists)
def testMultiple():
    """input of \"Hello :) Goodbye :(\" yields output of \"Hello 🙂 Goodbye 🙁\""""
    output = check50.run("python3 faces.py").stdin("Hello :) Goodbye :(", prompt=False).stdout("Hello 🙂 Goodbye 🙁").exit()