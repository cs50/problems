import check50
import check50.c


@check50.check()
def exists():
    """reverse.c exists"""
    check50.include("input.wav")
    check50.exists("reverse.c")


@check50.check(exists)
def compiles():
    """reverse.c compiles"""
    check50.c.compile("reverse.c", lcs50=True)


@check50.check(compiles)
def test_nofile():
    """reverse.c handles lack of input file"""
    check50.run("./reverse").exit(1)


@check50.check(compiles)
def test_output_file():
    """reverse.c creates an output file"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    check50.exists("output.wav")


@check50.check(test_output_file)
def test_header():
    """reverse.c writes WAV header to output file"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    with open("output.wav", "rb") as f:
        f.seek(8)
        for b in [b'W', b'A', b'V', b'E']:
            if f.read(1) != b:
                raise check50.Failure("output file does not have WAV file signature")


@check50.check(compiles)
def test_reverses_audio():
    """reverse.c reverses ascending scale"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    if check50.hash("output.wav") != "d7beb50a997b78e257cf77e1c6fa0bf835e8e59f86aa082a7a35f7ccc8d307b4":
        raise check50.Failure("file is not reversed as specified")