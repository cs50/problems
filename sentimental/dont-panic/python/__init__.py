import check50
from cs50 import SQL


@check50.check()
def exists():
    """hack.py exists"""
    check50.exists("hack.py")
    check50.include("dont-panic.db")


@check50.check(exists)
def test_execution():
    """hack.py correctly changes admin password"""
    new_password = "CS50"
    check50.run("python3 hack.py").stdin(new_password).exit(timeout=10)
    db = SQL("sqlite:///dont-panic.db")
    result = db.execute("SELECT password FROM users WHERE username = 'admin'")[0]["password"]
    if result != new_password:
        raise check50.Mismatch(str(expected), str(rows))

