from cs50 import SQL

import check50
import re
import sqlparse


@check50.check()
def exists():
    """indexes.sql exists"""
    check50.exists("indexes.sql")
    check50.include("harvard.db")


@check50.check(exists)
def test_execution():
    """indexes.sql runs without error"""
    db = SQL("sqlite:///harvard.db")
    run_statements(db, "indexes.sql")


def run_statements(db: SQL, filename: str) -> None:
    """
    Runs the SQL queries contained in 'filename' and checks for errors

    positional arguments:
        filename (str)      file containing SQL query

    returns:
        None
    """

    with open(filename) as f:

        # Read contents and strip comments
        contents = sqlparse.format(f.read().strip(), strip_comments=True)

        # Parse contents into list of SQL statements
        statements = sqlparse.split(contents)
        if not statements:
            raise check50.Failure(
                f"Could not find SQL statements in {filename}."
            )
        
        # Execute each statement starting from top of file
        try:
            for statement in statements:
                db.execute(statement.strip())
        except Exception as e:
            raise check50.Failure(f"Error when executing statements: {str(e)}")
