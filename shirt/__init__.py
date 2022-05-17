import check50

HASHES = {
    "muppet_01.jpg" : 'b782475a5dd3b0d7b3202cebc8a70f5d795dd196e9c18564691d5edc11ccf7c9',
    "muppet_02.jpg" : 'f989a97f95563f587e158bb55a1fc6dba075f1e221acec988612caaa0d1a6b78',
    "muppet_03.jpg" : 'fa7b30def84d46559c54e718d167de93e52785f9b613db8a647ddcfbbe9aff98',
    "muppet_04.jpg" : '8f59304412e181f1a18d3b36ad88d7b2911a7eea8f471c7e437e2cbed5893152',
    "muppet_05.jpg" : 'eeb531294c2211ba578dafe5c1f53d974f77312cec5b7bcc315c2bb429b3ac1d',
    "muppet_06.jpg" : '4918f1f41fa872e2807fd325d4e460bcce9b1f23660cdf0e73dc3127fccc1046',
}


@check50.check()
def exists():
    """shirt.py exists"""
    check50.exists("shirt.py")
    check50.include("shirt.png")


@check50.check(exists)
def test_fewer_arguments():
    """shirt.py exits given zero command-line arguments"""
    exit = check50.run("python3 shirt.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_extension():
    """shirt.py exits given a file without a .jpg, .jpeg, or .png extension"""
    check50.include("invalid_extension.bmp")
    exit = check50.run("python3 shirt.py invalid_extension.bmp").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_non_existent_file():
    """shirt.py exits given a non-existent file"""
    exit = check50.run("python3 shirt.py non_existent_file.jpg").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_mismatched_extension():
    """shirt.py exits given an output file with a different extension than input file"""
    check50.include("muppet_01.jpg")
    exit = check50.run("python3 shirt.py muppet_01.jpg muppet_01_out.png").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_more_arguments():
    """shirt.py exits given more than two command-line arguments"""
    for file in ["muppet_01.jpg", "muppet_02.jpg", "muppet_03.jpg"]:
        check50.include(file)
    exit = check50.run("python3 lines.py muppet_01.jpg muppet_02.jpg muppet_03.jpg").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_muppet_01():
    """shirt.py correctly displays shirt on muppet_01.jpg"""
    test_shirt("muppet_01.jpg")


@check50.check(exists)
def test_muppet_02():
    """shirt.py correctly displays shirt on muppet_02.jpg"""
    test_shirt("muppet_02.jpg")


@check50.check(exists)
def test_muppet_03():
    """shirt.py correctly displays shirt on muppet_03.jpg"""
    test_shirt("muppet_03.jpg")


@check50.check(exists)
def test_muppet_04():
    """shirt.py correctly displays shirt on muppet_04.jpg"""
    test_shirt("muppet_04.jpg")


@check50.check(exists)
def test_muppet_05():
    """shirt.py correctly displays shirt on muppet_05.jpg"""
    test_shirt("muppet_05.jpg")


@check50.check(exists)
def test_muppet_06():
    """shirt.py correctly displays shirt on muppet_06.jpg"""
    test_shirt("muppet_06.jpg")


def test_shirt(photo):
    check50.include(photo)
    check50.run(f"python3 shirt.py {photo} {photo[:-4]}_out.jpg").exit(0)
    hash = check50.hash(f"{photo[:-4]}_out.jpg")
    if hash != HASHES[photo]:
        raise check50.Failure("Image does not match")