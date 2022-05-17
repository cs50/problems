import check50

HASHES = {
    "muppet_01.jpg" : 'ff9e67fb54eea3361a48d7d02ded267917356195d1c770f5c537a6bb5a955bc3',
    "muppet_02.jpg" : '39fa49339e41062988ccc875f377cc7af5df1d7a34bac1aac214942159b81b8c',
    "muppet_03.jpg" : '252e2283a07ce4cba53237793b1478f32c4360bb59ec12e091c4ddccde150934',
    "muppet_04.jpg" : '2961f103aedaf3fdd4c30512c69598b5ec57a1d78abd43b06729d408243c0569',
    "muppet_05.jpg" : '5191faf25d7e67d8ca214d68cc19472efc42a97c08abf71ced6a3a2e5264f106',
    "muppet_06.jpg" : '76574d615ca845b5adb7c6521465b55ce853ef1ed82505c7edc93254c52ba663',
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