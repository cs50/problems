import check50


@check50.check()
def exists():
    """Hack.java exists"""
    check50.exists("Hack.java")
    check50.include("dont-panic.db")
    check50.include("sqlite-jdbc-3.43.0.0.jar")


@check50.check(exists)
def compiles():
    """Hack.java compiles"""
    check50.run("javac Hack.java").exit(0)


@check50.check(compiles)
def test_execution():
    """Hack.java correctly changes admin password"""
    new_password = "CS50"
    check50.run("java -cp .:sqlite-jdbc-3.43.0.0.jar Hack").stdin(new_password).exit(0)
    check50.run("sqlite3 dont-panic.db 'SELECT password FROM users WHERE username = \"admin\";'").stdout(new_password).exit(0)

