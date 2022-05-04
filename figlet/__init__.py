import check50
from re import escape


@check50.check()
def exists():
    """figlet.py exists"""
    check50.exists("figlet.py")
    check50.include("alphabet.txt")
    check50.include("rectangles.txt")
    check50.include("slant.txt")


@check50.check(exists)
def test_one_argument():
    """figlet.py exits given one command-line argument"""
    check50.run("python3 figlet.py test").exit(1)


@check50.check(exists)
def test_invalid_first_argument():
    """figlet.py exits given invalid first command-line argument"""
    check50.run("python3 figlet.py --front slant").exit(1)


@check50.check(exists)
def test_invalid_second_argument():
    """figlet.py exits given invalid second command-line argument"""
    check50.run("python3 figlet.py --font slnt").exit(1)


@check50.check(exists)
def test_slanted_text():
    """figlet.py renders slanted text"""
    font = "slant"
    text = "CS50"
    with open(f"{font}.txt", "r") as file:
        lines = file.readlines()
        output = ""
        for line in lines:
            output += line
        check50.run(f"python3 figlet.py --font {font}").stdin(text, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_rectangular_text():
    """figlet.py renders rectangular text"""
    font = "rectangles"
    text = "Hello, world"
    with open(f"{font}.txt", "r") as file:
        lines = file.readlines()
        output = ""
        for line in lines:
            output += line
        check50.run(f"python3 figlet.py --font {font}").stdin(text, prompt=False).stdout(regex(output), output, regex=True).exit(0)


@check50.check(exists)
def test_alphabet_text():
    """figlet.py renders alphabet text"""
    font = "alphabet"
    text = "Moo"
    with open(f"{font}.txt", "r") as file:
        lines = file.readlines()
        output = ""
        for line in lines:
            output += line
        check50.run(f"python3 figlet.py -f {font}").stdin(text, prompt=False).stdout(regex(output), output, regex=True).exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'
