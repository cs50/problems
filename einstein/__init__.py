import check50
import re

@check50.check()
def exists():
    """einstein.py exists"""
    check50.exists("einstein.py")

@check50.check(exists)
def test1():
    """input of 1 yields output of 90000000000000000"""
    output = check50.run("python3 einstein.py").stdin("1", prompt=False).stdout(r'(90,?0{3},?0{3},?0{3}.?(0+)?)|(90.?0{3}.?0{3}.?0{3},?(0+)?)', "90000000000000000").exit()

@check50.check(exists)
def test14():
    """input of 14 yields output of 1260000000000000000"""
    check50.run("python3 einstein.py").stdin("14", prompt=False).stdout(r'(1,?260,?0{3},?0{3},?0{3},?0{3},?0{3}.?(0+)?)|(1.?260.?0{3}.?0{3}.?0{3}.?0{3}.?0{3},?(0+)?)',"1260000000000000000").exit()

@check50.check(exists)
def test50():
    """input of 50 yields output of 4500000000000000000"""
    check50.run("python3 einstein.py").stdin("50", prompt=False).stdout(r'(4,?500,?0{3},?0{3},?0{3},?0{3},?0{3}.?(0+)?)|(4.?500.?0{3}.?0{3}.?0{3}.?0{3}.?0{3},?(0+)?)', "4500000000000000000").exit()