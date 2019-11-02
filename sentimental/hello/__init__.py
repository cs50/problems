import check50

@check50.check()
def exists():
    """hello.py exists."""
    check50.exists("hello.py")

@check50.check(exists)
def veronica():
    """responds to name Emma."""
    check50.run("python3 hello.py").stdin("Emma").stdout("Emma").exit()

@check50.check(exists)
def brian():
    """responds to name Rodrigo."""
    check50.run("python3 hello.py").stdin("Rodrigo").stdout("Rodrigo").exit()
