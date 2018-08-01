less = __import__("check50").import_checks("../less")
from less import *

@check50.check(compiles)
def space_between():
    """Outputs HJ for hailey       James"""
    check50.run("./initials").stdin("hailey       James", prompt=False).stdout(match("HJ"), "HJ\n").exit(0)

@check50.check(compiles)
def space_before_after():
    """Outputs HJ for     hailey James    """
    check50.run("./initials").stdin("    hailey James    ", prompt=False).stdout(match("HJ"), "HJ\n").exit(0)
