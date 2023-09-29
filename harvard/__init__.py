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
        contents = sqlparse.format(f.read().strip(), strip_comments=True)
        queries = re.findall(r".*?;", contents, re.DOTALL)
        if not queries:
            raise check50.Failure(
                "Could not find statements.",
                help="Did you write statements separated by semicolons?",
            )
        try:
            for query in queries:
                db.execute(query.strip())
        except Exception as e:
            raise check50.Failure(f"Error when executing statements: {str(e)}")
