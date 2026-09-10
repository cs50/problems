import check50
import check50.c


@check50.check()
def exists():
    """seats.c exists"""
    check50.exists("seats.c")


@check50.check(exists)
def compiles():
    """seats.c compiles"""
    check50.c.compile("seats.c", lcs50=True)


@check50.check(compiles)
def test_1x1():
    """prints a 1x1 seating chart"""
    process = check50.run("./seats")
    process.stdout("Enter number of rows:", regex=False).stdin("1", prompt=False)
    process.stdout("Enter number of seats per row:", regex=False).stdin("1", prompt=False)
    check_chart(process.stdout(), """
Row  1:   1
""")


@check50.check(compiles)
def test_3x5():
    """prints a 3x5 seating chart"""
    process = check50.run("./seats")
    process.stdout("Enter number of rows:", regex=False).stdin("3", prompt=False)
    process.stdout("Enter number of seats per row:", regex=False).stdin("5", prompt=False)
    check_chart(process.stdout(), """
Row  1:   1   2   3   4   5
Row  2:   6   7   8   9  10
Row  3:  11  12  13  14  15
""")


@check50.check(compiles)
def test_10x8():
    """prints a 10x8 seating chart using a single seat counter"""
    process = check50.run("./seats")
    process.stdout("Enter number of rows:", regex=False).stdin("10", prompt=False)
    process.stdout("Enter number of seats per row:", regex=False).stdin("8", prompt=False)
    check_chart(process.stdout(), """
Row  1:   1   2   3   4   5   6   7   8
Row  2:   9  10  11  12  13  14  15  16
Row  3:  17  18  19  20  21  22  23  24
Row  4:  25  26  27  28  29  30  31  32
Row  5:  33  34  35  36  37  38  39  40
Row  6:  41  42  43  44  45  46  47  48
Row  7:  49  50  51  52  53  54  55  56
Row  8:  57  58  59  60  61  62  63  64
Row  9:  65  66  67  68  69  70  71  72
Row 10:  73  74  75  76  77  78  79  80
""")


@check50.check(compiles)
def test_rejects_invalid_dimensions():
    """rejects non-positive rows and seats before drawing the chart"""
    out = check50.run("./seats").stdin("-1\n0\n2\n0\n-3\n3\n", prompt=False).stdout()

    if not contains_chart(out, """Row  1:   1   2   3
Row  2:   4   5   6
"""):
        raise check50.Failure(
            "program should keep re-prompting until given positive integers, "
            "then print a 2x3 chart"
        )


def normalize(text):
    """Split each non-blank line into whitespace-separated tokens.

    Any amount or kind of whitespace (spaces, tabs, column padding) between
    tokens is treated as equivalent, and blank lines are ignored.
    """
    return [line.split() for line in text.splitlines() if line.strip()]


def check_chart(output, correct):
    output_lines = normalize(output)
    correct_lines = normalize(correct)
    if output_lines == correct_lines:
        return
    raise check50.Mismatch(correct_lines, output_lines)


def contains_chart(output, correct):
    """Check whether `correct`'s lines appear, in order, anywhere in `output`.

    The chart's first line may be preceded on the same physical output line
    by leftover text (e.g. a prompt printed with no trailing newline right
    before the chart begins, or the tail end of a reprompt loop); every
    other chart line must match exactly.
    """
    output_lines = normalize(output)
    correct_lines = normalize(correct)
    span = len(correct_lines)
    first = correct_lines[0]
    for start in range(len(output_lines) - span + 1):
        candidate = output_lines[start]
        if (len(candidate) >= len(first)
                and candidate[len(candidate) - len(first):] == first
                and output_lines[start + 1:start + span] == correct_lines[1:]):
            return True
    return False
