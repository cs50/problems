from cs50 import SQL

import check50
import re
import sqlparse


@check50.check()
def exists():
    """import.sql exists"""
    check50.exists("import.sql")
    check50.include("meteorites.csv")


@check50.check(exists)
def test_execution():
    """import.sql runs without error"""

    # Check import.sql runs
    try:
        check50.run("cat import.sql | sqlite3 meteorites.db").exit(0)
    except check50.Failure:
        raise check50.Failure(
            "import.sql did not run without error", help="Have you checked your syntax?"
        )

    # Check meteorites.db was created
    try:
        check50.exists("meteorites.db")
    except check50.Failure:
        raise check50.Failure(
            "import.sql did not create meteorites.db",
            help="Does your file not contain a .import or CREATE TABLE statement?",
        )


@check50.check(test_execution)
def test_table_created():
    """import.sql creates a table named \"meteorites\" """
    db = SQL("sqlite:///meteorites.db")
    results = run_query(
        db,
        """
        SELECT "name"
        FROM "sqlite_schema"
        WHERE "type" = 'table'
        AND "name" NOT LIKE 'sqlite_%';
        """,
    )
    if not results:
        raise check50.Failure("No tables created in meteorites.db")
    table_names = [row["name"] for row in results]
    if "meteorites" not in table_names:
        raise check50.Failure('No table named "meteorites" found')


@check50.check(test_table_created)
def test_columns_exist():
    """import.sql creates a table named \"meteorites\" with all prescribed columns"""
    db = SQL("sqlite:///meteorites.db")
    results = db.execute('SELECT * FROM pragma_table_info("meteorites")')

    expected_columns = {
        "id",
        "name",
        "class",
        "mass",
        "discovery",
        "year",
        "lat",
        "long",
    }
    missing_columns = []
    extra_columns = []
    for column in results:
        if column["name"] not in expected_columns:
            missing_columns.append(column["name"])
            continue
        expected_columns.remove(column["name"])
    extra_columns = expected_columns

    if extra_columns or missing_columns:
        raise check50.Failure(
            'table "meteorites" is missing columns or has extra columns'
        )


@check50.check(test_columns_exist)
def test_empty_values_null():
    """no empty values from CSV are present in \"meteorites\" table"""
    db = SQL("sqlite:///meteorites.db")
    results = db.execute(
        """
        SELECT *
        FROM "meteorites"
        WHERE "mass" = ''
        OR "year" = ''
        OR "lat" = ''
        OR "long" = ''
        """,
    )

    if results:
        raise check50.Failure('empty values still exist in "meteorites" table')

    results = db.execute(
        """
        SELECT *
        FROM "meteorites"
        WHERE "mass" IS NULL
        OR "year" IS NULL
        OR "lat" IS NULL
        OR "long" IS NULL;
        """,
    )

    if not results:
        raise check50.Failure('NULL values are not present in "meteorites" table')


@check50.check(test_columns_exist)
def test_rounded_values():
    """all decimal values in \"meteorites\" table are rounded to two places"""
    db = SQL("sqlite:///meteorites.db")
    results = db.execute(
        """
        SELECT "mass", "lat", "long"
        FROM "meteorites"
        LIMIT 100;
        """,
    )

    pattern = r"^-?\d+(\.\d{1,2})?$"
    for row in results:
        for column_name in row.keys():
            if row[column_name]:
                if not re.search(pattern, str(row[column_name])):
                    raise check50.Failure(
                        f"Expected {row[column_name]} to be rounded to two decimal places"
                    )


@check50.check(test_columns_exist)
def test_no_relicts():
    """no meteorites of type \"relict\" found in \"meteorites\" table"""
    db = SQL("sqlite:///meteorites.db")
    for relict in [("Brunflo", 1980), ("David Glacier 92308", 1992), ("Gove", 1979)]:
        find_relict(db, *relict)


@check50.check(test_empty_values_null)
def test_sort_and_ids():
    """\"meteorites\" table properly sorts elements and assigns IDs"""
    db = SQL("sqlite:///meteorites.db")
    results = db.execute(
        """
        SELECT "id", "name", "year"
        FROM "meteorites"
        LIMIT 5;
        """,
    )
    check_multi_col(
        results,
        [
            {"1", "Apache Junction", "None"},
            {"2", "Asarco Mexicana", "None"},
            {"3", "Aus", "None"},
            {"4", "Benares (b)", "None"},
            {"5", "Cacilandia", "None"},
        ],
        ordered=True,
    )


def run_query(db: SQL, query: str) -> list[dict]:
    """
    Runs the SQL query contained in 'filename' and returns its output.

    positional arguments:
        filename (str)      file containing SQL query

    returns:
        list[dict]
    """

    try:
        query = sqlparse.format(query.strip(), strip_comments=True).strip()
        result = db.execute(query)
        return result
    except Exception as e:
        raise check50.Failure(f"Error when executing query: {str(e)}")


def find_relict(db: SQL, name: str, year: int) -> None:
    results = db.execute(
        f"""
        SELECT "name", "year"
        FROM "meteorites"
        WHERE "name" = '{name}'
        AND "year" = {year};
        """
    )
    if results:
        raise check50.Failure(f"Found relict meteorite {name} from {year}")


def check_single_cell(actual, expected):
    """
    Checks that the single cell in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (single element) expected result to match against

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert element to list of frozen set; ordered doesn't matter
    try:
        expected = [frozenset([expected])]
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered=True)


def check_multi_col(actual, expected, ordered=False):
    """
    Checks that the columns in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (list[set])      expected result to match against

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert list of sets to list of frozen sets or set of frozen sets
    try:
        if ordered:
            expected = [frozenset(unfrozen_set) for unfrozen_set in expected]
        else:
            expected = {frozenset(unfrozen_set) for unfrozen_set in expected}
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered)


def _check(actual, expected, ordered=False):
    """
    Checks that the SQL output in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected                  expected result to match against
            if ordered, should be list[frozenset];
            otherwise, set[frozenset]  (frozenset is needed for nested sets)

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # convert list of dictionaries to list of frozen sets or set of frozen sets,
    # depending on whether 'ordered' is True
    try:
        result = []
        for row_dict in actual:
            values = [str(elt) for elt in list(row_dict.values())]
            result.append(frozenset(values))
        result = result if ordered else set(result)
    except Exception as e:
        raise check50.Failure(f"Error with format of query: {str(e)}")

    # check result of query against expected values
    if result != expected:
        raise check50.Mismatch(
            "\n".join(", ".join(list(sorted(entry))) for entry in list(expected)),
            "\n".join(", ".join(list(sorted(entry))) for entry in list(result)),
        )
    return None
