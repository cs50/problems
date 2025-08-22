import check50
import check50.c

# permits either truncating or rounding the floats to ints
HASHES_HALF = [
    "268f2deee976fcc8dcc915be63cd3d4ac003a73a4b8bfd6f7b95c441a42ed1ec",
    "9a92829dcd2de343235607de1db01d374a44bd58738cb4070e354dead02e50c1",
]

HASHES_TENTH = [
    "4481b5a438d359718000dfd58e2a32a7b109eb4a5590e0650c6bd295979c64fc",
    "dae24291174811b2df95f6836e023e855c77bdc5bee3294542ba4bf1b95de2cc",
]

HASHES_DOUBLE = [
    "3d83603745302935c067379b704573e5addb4356ad407041f0a698070e6e4e7b",
]


@check50.check()
def exists():
    """volume.c exists"""
    check50.exists("volume.c")
    check50.include("input.wav")


@check50.check(exists)
def compiles():
    """volume.c compiles"""
    check50.c.compile("volume.c", lcs50=True)


@check50.check(compiles)
def audio_half():
    """reduces audio volume, factor of 0.5 correctly"""
    check50.run("./volume input.wav output.wav 0.5").exit(0)
    print("half: " + check50.hash("output.wav"))
    if check50.hash("output.wav") not in HASHES_HALF:
        raise check50.Failure("audio is not correctly altered, factor of 0.5")


@check50.check(compiles)
def audio_tenth():
    """reduces audio volume, factor of 0.1 correctly"""
    check50.run("./volume input.wav output.wav 0.1").exit(0)
    print("tenth: " + check50.hash("output.wav"))
    if check50.hash("output.wav") not in HASHES_TENTH:
        raise check50.Failure("audio is not correctly altered, factor of 0.1")


@check50.check(compiles)
def audio_x2():
    """increases audio volume, factor of 2 correctly"""
    check50.run("./volume input.wav output.wav 2").exit(0)
    print("double: " + check50.hash("output.wav"))
    if check50.hash("output.wav") not in HASHES_DOUBLE:
        raise check50.Failure("audio is not correctly altered, factor of 2")
