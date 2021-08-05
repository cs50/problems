import check50
import check50.c

@check50.check()
def exists():
    """experiment.py exists"""
    check50.exists("experiment.py")

@check50.check(exists)
def hello():
    """prints hello, world"""
    check50.run("python experiment.py").stdout("hello, world").exit()

