from cs50 import SQL
from pathlib import Path

import check50
import re
import sqlparse


FILES = [
    "available.sql",
    "frequently_reviewed.sql",
    "june_vacancies.sql",
    "no_descriptions.sql",
    "one_bedrooms.sql",
]


@check50.check()
def exists():
    """SQL files exist"""
    for file in FILES:
        check50.exists(file)
    check50.include("bnb.db")


@check50.check(exists)
def test_execution():
    """all files create a view without error"""
    for file in FILES:
        test_view(SQL("sqlite:///bnb.db"), Path(file))


@check50.check(test_execution)
def test_no_descriptions():
    """no_descriptions.sql produces correct view"""
    db = SQL("sqlite:///bnb.db")

    # Find count of rows in view
    try:
        result = db.execute(
            """\
            SELECT COUNT(*) AS "rows"
            FROM "no_descriptions";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    no_descriptions_rows = int(result[0]["rows"])

    # Find count of rows in listings table
    try:
        result = db.execute(
            """\
            SELECT COUNT(*) AS "rows"
            FROM "listings";
            """
        )
    except Exception as e:
        raise check50.Failure(f'Error when querying "listings" table: {str(e)}')
    listings_rows = int(result[0]["rows"])

    # View should have same number of rows as listings
    if no_descriptions_rows != listings_rows:
        raise check50.Failure('"no_descriptions" view does not contain all listings in "listings" table')
    
    # Test available column names in view
    try:
        result = db.execute(
            """\
            SELECT "name" FROM pragma_table_info("no_descriptions")
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when finding columns available in view: {str(e)}")

    for row in result:
        if row["name"] == "description":
            raise check50.Failure('"no_descriptions" view contains a column named "description"')


@check50.check(test_execution)
def test_one_bedrooms():
    """one_bedrooms.sql produces correct view"""
    db = SQL("sqlite:///bnb.db")
    try:
        result = db.execute(
            """\
            SELECT COUNT(*) AS "rows"
            FROM "one_bedrooms";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    rows = int(result[0]["rows"])
    
    # bnb.db used by check is smaller than bnb.db used by students
    if rows != 1:
        raise check50.Failure('"one_bedrooms" view does not contain the correct number of rows')


@check50.check(test_execution)
def test_available():
    """available.sql produces correct view"""
    db = SQL("sqlite:///bnb.db")
    try:
        result = db.execute(
            """\
            SELECT COUNT(*) AS "rows"
            FROM "available";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    rows = int(result[0]["rows"])
    
    # bnb.db used by check is smaller than bnb.db used by students
    if rows != 564:
        raise check50.Failure("available.sql does not contain the correct number of rows")


@check50.check(test_execution)
def test_june_vacancies():
    """june_vacancies.sql produces correct view"""
    db = SQL("sqlite:///bnb.db")
    try:
        result = db.execute(
            """\
            SELECT COUNT(*) AS "rows"
            FROM "june_vacancies";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    rows = int(result[0]["rows"])
    
    # bnb.db used by check is smaller than bnb.db used by students
    if rows != 2:
        raise check50.Failure("june_vacancies.sql does not contain the correct number of rows")


@check50.check(test_execution)
def test_frequently_reviewed():
    """frequently_reviewed.sql produces correct view"""
    db = SQL("sqlite:///bnb.db")
    try:
        result = db.execute(
            """\
            SELECT *
            FROM "frequently_reviewed"
            LIMIT 1;
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when querying view: {str(e)}")
    
    try:
        host_name = result[0]["host_name"]
    except KeyError:
        raise check50.Failure('View does not have column called "host_name"')

    try:
        property_type = result[0]["property_type"]
    except KeyError:
        raise check50.Failure('View does not have column called "property_type"')
    
    # bnb.db used by check is smaller than bnb.db used by students
    if host_name != "John" or property_type != "Private room in rental unit":
        raise check50.Failure("frequently_reviewed.sql does not include most-reviewed property as first row")


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
