import check50

HASHES = {
    "muppet_01.jpg" : 'dcb0aaa348dce041b01ee1cab133e068360aaa264be070c773df0481a9070e86',
    "muppet_02.jpg" : '8a57ea61beea2fb94c2e0f2c7959ecdab03dea05edb9c4d86e6b1f881d072fbf',
    "muppet_03.jpg" : '3b04d9d35cba8acee5716ba1e2c75f2f3d92612b4a11a71a88f7658473cf8f83',
    "muppet_04.jpg" : '7cce581e76b0b22dbc954b4de9a7cfa0bcc426645d0e584e2884d6c81ba55118',
    "muppet_05.jpg" : 'da1a9996ebd3516a0fec4ddf0989159597cd9ef90b57b0027e143e9fa9f62908',
    "muppet_06.jpg" : '47a0c0aa6ce5a5e7877a573e03b3e32870ce017f97bbbca6d05485a2db1716d7',
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
    check50.include("muppet_01.jpg")
    check50.include("muppet_02.jpg")
    check50.include("muppet_03.jpg")
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