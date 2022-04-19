import check50
from re import escape


@check50.check()
def exists():
    """nutrition.py exists"""
    check50.exists("nutrition.py")


@check50.check(exists)
def test_apple():
    """input of apple yields output of 130"""
    input = "apple"
    output = "130"
    check50.run("python3 nutrition.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_avocado():
    """input of Avocado yields output of 50"""
    input = "Avocado"
    output = "50"
    check50.run("python3 nutrition.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_kiwifruit():
    """input of Kiwifruit yields output of 90"""
    input = "Kiwifruit"
    output = "90"
    check50.run("python3 nutrition.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_pear():
    """input of pear yields output of 100"""
    input = "pear"
    output = "100"
    check50.run("python3 nutrition.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_sweet_cherries():
    """input of Sweet Cherries yields output of 100"""
    input = "Sweet Cherries"
    output = "100"
    check50.run("python3 nutrition.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_none():
    """nutrition.py ignores invalid input"""
    input = "Tomato"
    output = ""
    output = str(check50.run("python3 nutrition.py").stdin(input, prompt=True).stdout())
    if output != "":
        raise check50.Mismatch("", output)


def regex(text):
    """match case-sensitively, allowing for characters (but not numbers) on either side"""
    return fr'^[^\d]*{escape(text)}[^\d]*$'