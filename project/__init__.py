import re
import check50


@check50.check()
def exists():
    """DESIGN.md, schema.sql, and queries.sql exist"""
    check50.exists("DESIGN.md")
    check50.exists("schema.sql")
    check50.exists("queries.sql")


@check50.check(exists)
def check_design_length():
    """DESIGN.md is of sufficient length"""
    text = open("DESIGN.md").read().lower()
    if len(text) < 3000:
        raise check50.Failure(f"DESIGN.md is not long enough.")


@check50.check(exists)
def check_design_url():
    """DESIGN.md contains video URL"""
    text = open("DESIGN.md").read().lower()
    urls = re.findall("https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+", text)
    if not urls:
        raise check50.Failure(f"Video URL is missing.")


@check50.check(exists)
def check_schema():
    """schema.sql contains at least 2 CREATE TABLE statements"""
    test_contents("CREATE TABLE", "schema.sql", 2)


@check50.check(exists)
def check_queries():
    """queries.sql contains at least 2 SELECT statements"""
    test_contents("SELECT", "queries.sql", 2)


def test_contents(pattern: str, filename: str, quantity: int = 1) -> None:
    """
    Tests if the given pattern is in the filename quantity number of times

    positional arguments:
        pattern (str)       regex pattern to check for
        filename (str)      the file in which to look for the pattern
        quantity (int)      the number of times the pattern should appear

    raises:
        check50.Failure if the pattern is not found quantity number of times
    """
    with open(filename, "r") as f:
        contents = f.read()

    if not len(re.findall(pattern, contents, re.IGNORECASE)) >= quantity:
        if quantity == 1:
            message = f"Expected to find at least {quantity} {pattern} statement"
        else:
            message = f"Expected to find at least {quantity} {pattern} statements"
        raise check50.Failure(message)
