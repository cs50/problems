import check50
from re import escape


@check50.check()
def exists():
    """extensions.py exists"""
    check50.exists("extensions.py")


@check50.check(exists)
def testgif():
    """input of .gif yields output of image/gif"""
    input = ".gif"
    output = "image/gif"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testjpg():
    """input of .jpg yields output of image/jpeg"""
    input = ".jpg"
    output = "image/jpeg"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testjpeg():
    """input of .jpeg yields output of image/jpeg"""
    input = ".jpeg"
    output = "image/jpeg"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpng():
    """input of .png yields output of image/png"""
    input = ".png"
    output = "image/png"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpdf():
    """input of .pdf yields output of application/pdf"""
    input = ".pdf"
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testtxt():
    """input of .txt yields output of text/plain"""
    input = ".txt"
    output = "text/plain"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testzip():
    """input of .zip yields output of application/zip"""
    input = ".zip"
    output = "application/zip"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testbin():
    """input of .bin yields output of application/octet-stream"""
    input = ".bin"
    output = "application/octet-stream"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpdf_capital():
    """input of .PDF yields output of application/pdf"""
    input = ".pdf"
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpdf_spaces():
    """input of .PDF, with spaces on either side, yields output of application/pdf"""
    input = " .pdf   "
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    return fr'^[\s]*{escape(text)}[\s]*$'