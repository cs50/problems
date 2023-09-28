from cs50 import SQL

import check50
import re
import sqlparse


@check50.check()
def exists():
    """schema.sql exists"""
    check50.exists("schema.sql")


@check50.check(exists)
def test_execution():
    """schema.sql runs without error"""
    db = create_database("atl.db")
    run_statements(db, "schema.sql")


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
    """schema.sql contains at least 1 FOREIGN KEY statements"""
    test_contents("FOREIGN KEY", "schema.sql")


def create_database(filename: str) -> SQL:
    """
    Creates a database with the specified filename and returns a connection to it.

    positional arguments:
        filename (str)      name of database to create

    returns:
        SQL object from the cs50 library
    """
    open(filename, "w").close()
    return SQL(f"sqlite:///{filename}")


def run_statements(db: SQL, filename: str) -> None:
    """
    Runs the SQL queries contained in 'filename' and checks for errors

    positional arguments:
        filename (str)      file containing SQL query

    returns:
        None
    """
    try:
        with open(filename) as f:
            queries = re.findall(r".*?;", f.read().strip(), re.DOTALL)
            if not queries:
                raise check50.Failure(
                    "Error when executing statements.",
                    help="Did you separate your statements with semicolons?",
                )
            for query in queries:
                db.execute(sqlparse.format(query, strip_comments=True).strip())
    except Exception as e:
        raise check50.Failure(f"Error when executing statements: {str(e)}")


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
