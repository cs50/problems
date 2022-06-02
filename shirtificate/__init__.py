import check50


@check50.check()
def exists():
    """shirtificate.py exist"""
    check50.exists("shirtificate.py")
    check50.include("shirtificate.png")


@check50.check(exists)
def test_create_pdf():
    """shirtificate.py creates a PDF called shirtificate.pdf"""
    check50.run("python3 shirtificate.py").stdin("John Harvard", prompt=True).exit(0)
    check50.exists("shirtificate.pdf")