import check50
from re import escape


@check50.check()
def exists():
    """watch.py exists"""
    check50.exists("watch.py")
    check50.include("testing.py")


@check50.check(exists)
def test_simple_http():
    """watch.py extracts http:// formatted link from iframe with single attribute"""
    link = "http://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_simple_https():
    """watch.py extracts https:// formatted link from iframe with single attribute"""
    link = "https://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_simple_https_www():
    """watch.py extracts https://www. formatted link from iframe with single attribute"""
    link = "https://www.youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_complex_http():
    """watch.py extracts http:// formatted link from iframe with multiple attributes"""
    link = "http://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_complex_https():
    """watch.py extracts https:// formatted link from iframe with multiple attributes"""
    link = "https://youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_complex_https_www():
    """watch.py extracts https://www. formatted link from iframe with multiple attributes"""
    link = "https://www.youtube.com/embed/xvFZjo5PgG0"
    output = "https://youtu.be/xvFZjo5PgG0"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_non_youtube():
    """watch.py returns None when given iframe without YouTube link"""
    link = "https://cs50.harvard.edu/python"
    output = "None"
    test_simple_iframe(link, output)


@check50.check(exists)
def test_outside_iframe():
    """watch.py returns None when given YouTube link outside of an iframe"""
    input = "https://www.youtube.com/embed/xvFZjo5PgG0"
    output = "None"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


"""
Helpers
"""


def test_simple_iframe(link, output):
    input = f"<iframe src=\"{link}\"></iframe>"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


def test_complex_iframe(link, output):
    input = f"<iframe width=\"560\" height=\"315\" src=\"{link}\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"
    check50.run("python3 testing.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit(0)


def regex(text):
    """match case-sensitively, allowing for only whitespace on either side"""
    return fr'^\s*{escape(text)}\s*$'