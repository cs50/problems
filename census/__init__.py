from cs50 import SQL
from pathlib import Path

import check50
import re
import sqlparse


@check50.check()
def exists():
    """SQL files exist"""
    for file in [
        "rural.sql",
        "total.sql",
        "by_district.sql",
        "most_populated.sql",
    ]:
        check50.exists(file)
    check50.include("census.db")


@check50.check(exists)
def test_rural():
    """rural.sql creates a view without error"""
    test_view(SQL("sqlite:///census.db"), Path("rural.sql"))


@check50.check(exists)
def test_total():
    """total.sql creates a view without error"""
    test_view(SQL("sqlite:///census.db"), Path("total.sql"))


@check50.check(exists)
def test_by_district():
    """by_district.sql creates a view without error"""
    test_view(SQL("sqlite:///census.db"), Path("by_district.sql"))


@check50.check(exists)
def test_most_populated():
    """most_populated.sql creates a view without error"""
    test_view(SQL("sqlite:///census.db"), Path("most_populated.sql"))


def test_view(db: SQL, filename: Path) -> None:
    # Infer view name
    view_name = filename.stem

    # Read SQL file
    with open(filename, "r") as f:
        statement = sqlparse.format(f.read().strip(), strip_comments=True)

        # Check for intent
        if not re.search(
            rf'CREATE\s+VIEW\s+"?{re.escape(view_name)}"?', statement, re.IGNORECASE
        ):
            raise check50.Failure(
                f'{filename} does not create a view named "{view_name}"'
            )

    # Run CREATE VIEW statement on database
    try:
        db.execute(statement)
    except Exception as e:
        raise check50.Failure(f"Error when creating view: {str(e)}")

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
