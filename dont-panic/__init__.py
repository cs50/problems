from cs50 import SQL

import check50
import re
import sqlparse


@check50.check()
def exists():
    """hack.sql exists"""
    check50.exists("hack.sql")
    check50.include("dont-panic.db")


@check50.check(exists)
def test_execution():
    """hack.sql runs without error"""
    db = SQL("sqlite:///dont-panic.db")
    run_statements(db, "hack.sql")


@check50.check(test_execution)
def test_admin_password():
    """hack.sql correctly modifies password of admin user"""

    # Run hack.sql on database
    db = SQL("sqlite:///dont-panic.db")
    run_statements(db, "hack.sql")

    # Query for password
    try:
        password = run_query(
            db,
            """
            SELECT "password"
            FROM "users"
            WHERE "username" = 'admin';      
            """,
        )[0]["password"]
    except IndexError:
        raise check50.Failure("Query for password did not return results")

    # Check password
    expected_password = "982c0381c279d139fd221fce974916e7"
    if password != expected_password:
        helper_text = None
        if password == "oops!":
            helper_text = "Did you forget to put the password through an MD5 hash?"
        raise check50.Mismatch(
            expected=expected_password,
            actual=password,
            help=helper_text,
        )


@check50.check(test_admin_password)
def test_erase_logs():
    """hack.sql leaves no trace of true update to admin password"""

    # Run hack.sql on database
    db = SQL("sqlite:///dont-panic.db")
    run_statements(db, "hack.sql")

    # Check for update logs referencing admin
    results = run_query(
        db,
        """
        SELECT "type", "old_username", "new_password"
        FROM "user_logs"
        WHERE "type" = 'update'
        AND ("old_username" = 'admin' OR "new_username" = 'admin')
        AND "new_password" = "982c0381c279d139fd221fce974916e7"
        """,
    )
    if results:
        raise check50.Failure(
            "Expected not to find a record of changing the admin's password"
        )


@check50.check(test_erase_logs)
def test_add_data():
    """hack.sql correctly adds false log of changing admin's password"""

    # Run hack.sql on database
    db = SQL("sqlite:///dont-panic.db")
    run_statements(db, "hack.sql")

    # Check for update logs referencing admin
    results = run_query(
        db,
        """
        SELECT "type", "old_username", "new_password"
        FROM "user_logs"
        WHERE "type" = 'update'
        AND ("old_username" = 'admin' OR "new_username" = 'admin')
        """,
    )

    if not results:
        raise check50.Failure("Did not find a false log")

    check_multi_col(
        results,
        [{"update", "admin", "44bf025d27eea66336e5c1133c3827f7"}],
        ordered=False,
    )


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

    with open(filename) as f:

        # Read contents and strip comments
        contents = sqlparse.format(f.read().strip(), strip_comments=True)

        # Parse contents into list of SQL statements
        statements = sqlparse.split(contents)
        if not statements:
            raise check50.Failure(
                f"Could not find SQL statements in {filename}"
            )
        
        # Execute each statement starting from top of file
        try:
            for statement in statements:
                db.execute(statement.strip())
        except Exception as e:
            raise check50.Failure(f"Error when executing statements: {str(e)}")


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
