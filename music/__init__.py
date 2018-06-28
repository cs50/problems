import check50
import check50.c

@check50.check()
def exists():
    """bday.txt and helpers.c exist"""

    # Ensure student files exist
    check50.exists("bday.txt", "helpers.c")

    # Include distribution code
    check50.include("helpers.h", "wav.h", "wav.c")

@check50.check(exists)
def compiles():
    """helpers.c compiles"""
    check50.c.compile("is_rest.c", "wav.c", "helpers.c", lcs50=True)
    check50.c.compile("duration.c", "wav.c", "helpers.c", lcs50=True)
    check50.c.compile("frequency.c", "wav.c", "helpers.c", lcs50=True)

@check50.check(exists)
def bday():
    """bday.txt is correct"""
    solution = ["D4@1/8", "D4@1/8", "E4@1/4", "D4@1/4", "G4@1/4", "F#4@1/2",
                "D4@1/8", "D4@1/8", "E4@1/4", "D4@1/4", "A4@1/4", "G4@1/2",
                "D4@1/8", "D4@1/8", "D5@1/4", "B4@1/4", "G4@1/4", "F#4@1/4",
                "E4@1/4", "C5@1/8", "C5@1/8", "B4@1/4", "G4@1/4", "A4@1/4",
                "G4@1/2"]

    try:
        with open("bday.txt") as f:
            bday = f.read().splitlines()
    except UnicodeDecodeError:
        raise check50.Failure("bday.txt does not seem to contain text")

    # Check length of song
    if len(solution) != len(bday):
        raise check50.Failure(f"expected {len(solution)} lines in bday.txt, but yours has {len(bday)}")

    # Make sure each note matches
    for note, (expected, actual) in enumerate(zip(solution, bday), 1):
        if expected != actual:
            raise check50.Failure(f"incorrect note on line {note}")

@check50.check(compiles)
def is_rest_true():
    """is_rest identifies "" as a rest"""
    check50.run("./is_rest ''").exit(0)

@check50.check(compiles)
def is_rest_false():
    """is_rest does not identify "A4" as a rest"""
    check50.run("./is_rest A4").exit(0)

@check50.check(compiles)
def duration_eighth():
    """fraction "1/8" returns duration 1"""
    check50.run("./duration 1/8").stdout("(?<!\d)1(?!\d)", "1").exit(0)

@check50.check(compiles)
def duration_quarter():
    """fraction "1/4" returns duration 2"""
    check50.run("./duration 1/4").stdout("(?<!\d)2(?!\d)", "2").exit(0)

@check50.check(compiles)
def duration_dotted_quarter():
    """fraction "3/8" returns duration 3"""
    check50.run("./duration 3/8").stdout("(?<!\d)3(?!\d)", "3").exit(0)

@check50.check(compiles)
def duration_half():
    """fraction of "1/2" returns duration 4"""
    check50.run("./duration 1/2").stdout("(?<!\d)4(?!\d)", "4").exit(0)

@check50.check(compiles)
def frequency_A4():
    """note A4 has frequency 440"""
    check50.run("./frequency A4").stdout("(?<!\d)440(?!\d)", "440").exit(0)

@check50.check(compiles)
def frequency_A6():
    """note A6 has frequency 1760"""
    check50.run("./frequency A6").stdout("(?<!\d)1760(?!\d)", "1760").exit(0)

@check50.check(compiles)
def frequency_ASharp5():
    """note A#5 has frequency 932"""
    check50.run("./frequency A#5").stdout("(?<!\d)932(?!\d)", "932").exit(0)

@check50.check(compiles)
def frequency_AFlat3():
    """note Ab3 has frequency 208"""
    check50.run("./frequency Ab3").stdout("(?<!\d)208(?!\d)", "208").exit(0)

@check50.check(compiles)
def frequency_C3():
    """note C3 has frequency 131"""
    check50.run("./frequency C3").stdout("(?<!\d)131(?!\d)", "131").exit(0)

@check50.check(compiles)
def frequency_Bb5():
    """note Bb5 has frequency 932"""
    check50.run("./frequency Bb5").stdout(f"(?<!\d)932(?!\d)", "932").exit(0)


FREQS = {"C3": 131, "C#3": 139, "D3": 147, "D#3": 156, "E3": 165, "F3": 175, "F#3": 185,
         "G3": 196, "G#3": 208, "A3": 220, "A#3": 233, "B3": 247, "C4": 262, "C#4": 277,
         "D4": 294, "D#4": 311, "E4": 330, "F4": 349, "F#4": 370, "G4": 392, "G#4": 415,
         "A4": 440, "A#4": 466, "B4": 494, "C5": 523, "C#5": 554, "D5": 587, "D#5": 622,
         "E5": 659, "F5": 698, "F#5": 740, "G5": 784, "G#5": 831, "A5": 880, "A#5": 932,
         "B5": 988}

@check50.check(compiles)
def frequencies():
    """produces all correct notes for octaves 3-5"""
    for note, frequency in FREQS.items():
        check50.run(f"./frequency {note}").stdout(f"(?<!\d){frequency}(?!\d)", str(frequency)).exit(0)
