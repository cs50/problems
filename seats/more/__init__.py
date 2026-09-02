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
def test_3x6_x3():
    """prints a 3x6 seating chart with aisle seats omitted"""
    out = check50.run("./seats").stdin("3\n6\n3\n").stdout()
    check_chart(out, """Enter number of rows: 3
Enter number of seats per row: 6
Enter aisle spacing: 3

Row  1:   1   2       4   5
Row  2:   7   8      10  11
Row  3:  13  14      16  17
""")


@check50.check(compiles)
def test_10x8_x4():
    """prints a 10x8 seating chart with blank columns for aisle seats"""
    out = check50.run("./seats").stdin("10\n8\n4\n").stdout()
    check_chart(out, """Enter number of rows: 10
Enter number of seats per row: 8
Enter aisle spacing: 4

Row  1:   1   2   3       5   6   7
Row  2:   9  10  11      13  14  15
Row  3:  17  18  19      21  22  23
Row  4:  25  26  27      29  30  31
Row  5:  33  34  35      37  38  39
Row  6:  41  42  43      45  46  47
Row  7:  49  50  51      53  54  55
Row  8:  57  58  59      61  62  63
Row  9:  65  66  67      69  70  71
Row 10:  73  74  75      77  78  79
""")


@check50.check(compiles)
def test_rejects_non_divisible_spacing():
    """rejects aisle spacing that does not evenly divide the row width"""
    out = check50.run("./seats").stdin("4\n5\n3\n").stdout()

    if "error" not in out.lower() or any(line.startswith("Row ") for line in out.splitlines()):
        raise check50.Failure(
            "program should print an error and halt when aisle spacing does not evenly divide the row width"
        )


@check50.check(compiles)
def test_rejects_invalid_dimensions():
    """rejects non-positive rows and seats before drawing the chart"""
    out = check50.run("./seats").stdin("-1\n0\n2\n0\n-3\n3\n3\n").stdout()

    if not contains_chart(out, """Row  1:   1   2   3
Row  2:   4   5   6
"""):
        raise check50.Failure(
            "program should keep re-prompting until given positive rows/seats, "
            "then print a 2x3 chart with no aisles"
        )


@check50.check(compiles)
def test_rejects_invalid_spacing():
    """rejects non-positive aisle spacing before drawing the chart"""
    out = check50.run("./seats").stdin("2\n4\n0\n-2\n4\n").stdout()

    if not contains_chart(out, """Row  1:   1   2   3   4
Row  2:   5   6   7   8
"""):
        raise check50.Failure(
            "program should keep re-prompting until given a positive aisle spacing, "
            "then print a 2x4 chart with no aisles"
        )


def normalize(text):
    """Split each non-blank line into whitespace-separated tokens.

    Any amount or kind of whitespace (spaces, tabs, column padding) between
    tokens is treated as equivalent, and blank lines are ignored. Aisle seats
    omitted from a row (surrounded only by whitespace) simply contribute no
    token, so the sequence of remaining seat numbers is still compared exactly.
    """
    return [line.split() for line in text.splitlines() if line.strip()]


def check_chart(output, correct):
    output_lines = normalize(output)
    correct_lines = normalize(correct)
    if output_lines == correct_lines:
        return
    raise check50.Mismatch(correct_lines, output_lines)


def contains_chart(output, correct):
    """Check whether `correct`'s lines appear, in order, anywhere in `output`."""
    output_lines = normalize(output)
    correct_lines = normalize(correct)
    span = len(correct_lines)
    return any(
        output_lines[start:start + span] == correct_lines
        for start in range(len(output_lines) - span + 1)
    )
