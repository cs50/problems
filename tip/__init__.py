import check50


@check50.check()
def exists():
    """tip.py exists"""
    check50.exists("tip.py")

@check50.check(exists)
def test50():
    """input of $50.00 and 15% yields $7.50"""
    check50.run("python3 tip.py").stdin("$50.00", prompt=True).stdin("15%", prompt=True).stdout(r'\$?7.50', 'Leave $7.50\n').exit()

@check50.check(exists)
def test100():
    """input of $100.00 and 18% yields $18.00"""
    check50.run("python3 tip.py").stdin("$100.00", prompt=True).stdin("18%", prompt=True).stdout(r'\$?18.00', 'Leave $18.00\n').exit()

@check50.check(exists)
def test15():
    """input of $15.00 and 25% yields $3.75"""
    check50.run("python3 tip.py").stdin("$15.00", prompt=True).stdin("25%", prompt=True).stdout(r'\$?3.75', 'Leave $3.75\n').exit()