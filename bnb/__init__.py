from cs50 import SQL
from pathlib import Path

import check50
import re
import sqlparse


@check50.check()
def exists():
    """SQL files exist"""
    for file in [
        "available.sql",
        "frequently_reviewed.sql",
        "june_vacancies.sql",
        "no_descriptions.sql",
        "one_bedrooms.sql",
    ]:
        check50.exists(file)
    check50.include("bnb.db")


@check50.check(exists)
def test_available():
    """available.sql creates a view without error"""
    test_view(SQL("sqlite:///bnb.db"), Path("available.sql"))


@check50.check(exists)
def test_frequently_reviewed():
    """frequently_reviewed.sql creates a view without error"""
    test_view(SQL("sqlite:///bnb.db"), Path("frequently_reviewed.sql"))


@check50.check(exists)
def test_no_descriptions():
    """no_descriptions.sql creates a view without error"""
    test_view(SQL("sqlite:///bnb.db"), Path("no_descriptions.sql"))


@check50.check(exists)
def test_one_bedrooms():
    """one_bedrooms.sql creates a view without error"""
    test_view(SQL("sqlite:///bnb.db"), Path("one_bedrooms.sql"))


@check50.check(exists)
def test_june_vacancies():
    """june_vacancies.sql creates a view without error"""
    test_view(SQL("sqlite:///bnb.db"), Path("june_vacancies.sql"))


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
