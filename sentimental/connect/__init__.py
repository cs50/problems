from cs50 import SQL

import check50
import re
import sqlparse


@check50.check()
def exists():
    """schema.sql exists"""
    check50.exists("schema.sql")


@check50.check(exists)
def test_create_tables():
    """schema.sql contains at least 1 CREATE TABLE statement"""
    test_contents("CREATE TABLE", "schema.sql")


@check50.check(exists)
def test_primary_keys():
    """schema.sql contains at least 1 PRIMARY KEY statement"""
    test_contents("PRIMARY KEY", "schema.sql")


@check50.check(exists)
def test_foreign_keys():
    """schema.sql contains at least 1 FOREIGN KEY statement"""
    test_contents("FOREIGN KEY", "schema.sql")


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
