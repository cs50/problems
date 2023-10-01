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
    check50.include("Hack.class")


@check50.check(compiles)
def test_execution():
    """Hack.java runs without error"""
    check50.run("java -cp .:sqlite-jdbc-3.43.0.0.jar Hack").exit(0)
