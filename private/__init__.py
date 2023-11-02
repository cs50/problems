from cs50 import SQL
from pathlib import Path

import check50
import re
import sqlparse


@check50.check()
def exists():
    """private.sql exists"""
    check50.exists("private.sql")
    check50.include("private.db")


@check50.check(exists)
def test_execution():
    """private.sql creates a view named "message" without error"""
    db = SQL("sqlite:///private.db")
    test_view(db, Path("private.sql"), view_name="message")


@check50.check(test_execution)
def test_message():
    """private.sql produces view that reveals secret message"""
    db = SQL("sqlite:///private.db")
    try:
        result = db.execute(
            """\
            SELECT "phrase"
            FROM "message";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")

    if not result:
        raise check50.Failure('"message" view does not contain any rows')

    if "phrase" not in result[0].keys():
        raise check50.Failure('"message" view does not have a column named "phrase"')

    sentence = " ".join([row["phrase"] for row in result]).lower()
    expected = "find me in the place you least expect. behind the books"
    if sentence != expected:
        raise check50.Failure(
            'Sentence retrieved from "message" view does not match secret message',
            help="Do you have any leading or trailing whitespace in any of your phrases?",
        )


def test_view(db: SQL, filename: Path, view_name: str = "") -> None:
    # Infer view name
    if not view_name:
        view_name = filename.stem

    # Read SQL file
    with open(filename, "r") as f:
        contents = sqlparse.format(f.read().strip(), strip_comments=True)
        statements = sqlparse.split(contents)
    
    # Check for statements
    if not statements:
        raise check50.Failure(f"Could not find SQL statements in {filename}")

    # Check for intent
    found = False
    for statement in statements:
        if re.search(
            rf'CREATE\s+VIEW\s+"?{re.escape(view_name)}"?', statement, re.IGNORECASE
        ):
            found = True
    if not found:
        raise check50.Failure(
            f'{filename} does not create a view named "{view_name}"'
        )

    # Run statements on database
    for statement in statements:
        try:
            db.execute(statement.strip())
        except Exception as e:
            raise check50.Failure(f"Error when executing statement: {str(e)}")

    # SELECT from view to see contents
    try:
        db.execute(
            f"""\
            SELECT *
            FROM "{view_name}";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when selecting from view: {str(e)}")
