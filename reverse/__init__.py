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


@check50.check(test_header)
def test_reverses_audio():
    """reverse.c reverses ascending scale"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    file_hash = check50.hash("output.wav")
    if file_hash != "bb4a927734bee48387e820ebf0ad3cf67fa5db88bf8c11eea6b61162174ec02f":
        if file_hash == "e1e69515128debe5575995e89f4003bc44e2d5a362afa7314e81b621e9620934":
            raise check50.Failure("file is not reversed as specified", help="looks like you included a reversed header at the end of your file!")
        raise check50.Failure("file is not reversed as specified")
