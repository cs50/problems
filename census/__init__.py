from cs50 import SQL
from pathlib import Path

import check50
import re
import sqlparse


FILES = [
        "rural.sql",
        "total.sql",
        "by_district.sql",
        "most_populated.sql",
    ]


@check50.check()
def exists():
    """SQL files exist"""
    for file in FILES:
        check50.exists(file)
    check50.include("census.db")


@check50.check(exists)
def test_execution():
    """all files create a view without error"""
    for file in FILES:
        test_view_execution(SQL("sqlite:///census.db"), Path(file))


@check50.check(test_execution)
def test_rural():
    """rural.sql produces correct view"""
    db = SQL("sqlite:///census.db")
    try:
        result = db.execute(
            """\
            SELECT COUNT(*) AS "rows"
            FROM "rural";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    rows = int(result[0]["rows"])
    if rows != 461:
        raise check50.Failure("rural.sql does not contain the correct number of rows")


@check50.check(test_execution)
def test_total():
    """total.sql produces correct view"""
    db = SQL("sqlite:///census.db")
    try:
        result = db.execute(
            """\
            SELECT "households"
            FROM "total";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    try:
        households = int(result[0]["households"])
    except KeyError:
        raise check50.Failure('View does not have a column named "households"')
    
    if households != 5642674:
        raise check50.Failure("total.sql does not contain the correct number of households")


@check50.check(test_execution)
def test_by_district():
    """by_district.sql produces correct view"""
    db = SQL("sqlite:///census.db")
    try:
        result = db.execute(
            """\
            SELECT "families"
            FROM "by_district"
            WHERE "district" = 'Mustang';
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    try:
        families = int(result[0]["families"])
    except KeyError:
        raise check50.Failure('View does not have a colum named "families"')

    if families != 3751:
        raise check50.Failure("by_district.sql does not contain the correct number of families in the Mustang district")


@check50.check(test_execution)
def test_most_populated():
    """most_populated.sql produces correct view"""
    db = SQL("sqlite:///census.db")
    try:
        result = db.execute(
            """\
            SELECT *
            FROM "most_populated"
            LIMIT 1;
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    try:
        district = result[0]["district"]
    except KeyError:
        raise check50.Failure('View does not have a colum named "district"')

    if district != "Kathmandu":
        raise check50.Failure("most_populated.sql does not list Kathmandu as most populated district")


def test_view_execution(db: SQL, filename: Path) -> None:
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
