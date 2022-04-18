import check50
from re import escape


@check50.check()
def exists():
    """extensions.py exists"""
    check50.exists("extensions.py")


@check50.check(exists)
def testgif():
    """input of cs50.gif yields output of image/gif"""
    input = "cs50.gif"
    output = "image/gif"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testjpg():
    """input of happy.jpg yields output of image/jpeg"""
    input = "happy.jpg"
    output = "image/jpeg"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testjpeg():
    """input of happy.jpeg yields output of image/jpeg"""
    input = "happy.jpeg"
    output = "image/jpeg"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpng():
    """input of check.png yields output of image/png"""
    input = "check.png"
    output = "image/png"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpdf():
    """input of document.pdf yields output of application/pdf"""
    input = "document.pdf"
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testtxt():
    """input of plain.txt yields output of text/plain"""
    input = "plain.txt"
    output = "text/plain"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testzip():
    """input of files.zip yields output of application/zip"""
    input = "files.zip"
    output = "application/zip"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testbin():
    """input of application.bin yields output of application/octet-stream"""
    input = "application.bin"
    output = "application/octet-stream"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpdf_capital():
    """input of document.PDF yields output of application/pdf"""
    input = "document.PDF"
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def testpdf_spaces():
    """input of document.PDF, with spaces on either side, yields output of application/pdf"""
    input = " document.pdf   "
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

    
@check50.check(exists)
def test_two():
    """input of test.txt.pdf, with one extra extension, yields output of application/pdf"""
    input = "test.txt.pdf"
    output = "application/pdf"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

    
@check50.check(exists)
def testjpg_substring():
    """input of zipper.jpg, with another extension name, yields output of image/jpeg"""
    input = "zipper.jpg"
    output = "image/jpeg"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()
    

@check50.check(exists)
def test_noextension():
    """input of myfile, with no extension, yields output of application/octet-stream"""
    input = "myfile"
    output = "application/octet-stream"
    check50.run("python3 extensions.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()
    
    
def regex(text):
    """match case-sensitively, allowing for spaces on either side"""
    return fr'^\s*{escape(text)}\s*$'
