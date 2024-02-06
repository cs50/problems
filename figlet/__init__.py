import check50
from re import escape


@check50.check()
def exists():
    """figlet.py exists"""
    check50.exists("figlet.py")
    check50.include("testing.py")


@check50.check(exists)
def test_one_argument():
    """figlet.py exits given one command-line argument"""
    exit = check50.run("python3 figlet.py test").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_first_argument():
    """figlet.py exits given invalid first command-line argument"""
    exit = check50.run("python3 figlet.py --front slant").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_second_argument():
    """figlet.py exits given invalid second command-line argument"""
    exit = check50.run("python3 figlet.py --font slnt").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_slanted_text():
    """figlet.py renders slanted text"""
    check_font_rendering(font="slant", text="CS50")


@check50.check(exists)
def test_rectangular_text():
    """figlet.py renders rectangular text"""
    check_font_rendering(font="rectangles", text="Hello, world")


@check50.check(exists)
def test_alphabet_text():
    """figlet.py renders alphabet text"""
    check_font_rendering(font="alphabet", text="Moo")


@check50.check(exists)
def test_random_text():
    """figlet.py renders text with random font"""
    check_font_rendering(font="random", text="PYTHON")


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'


def check_font_rendering(font, text):
    check50.include(f"{font}.txt")
    with open(f"{font}.txt", "r") as file:
        lines = file.readlines()
        output = ""
        for line in lines:
            output += line
    
    if font == "random":
        run = check50.run("python3 testing.py")
    else:
        run = check50.run(f"python3 figlet.py -f {font}")
    
    try:
        run.stdin(text, prompt=False).stdout(regex(output), output, regex=True).exit()
    except check50.Failure as fail:
        help = None
        
        # Assuming it failed because testing.py couldn't run the figlet.py file
        if font == "random" and not isinstance(fail, check50.Mismatch):
            help = "Does your script contain a parameterless main() function?"
        
        error = check50.Failure(str(fail), help=help)
    else:
        error = None

    if error:
        raise error
