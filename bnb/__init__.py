from cs50 import SQL
from pathlib import Path

import check50
import re


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
    """available.sql produces correct view"""

    # Set filename to test
    filename = Path("available.sql")

    # Get view name from filename (e.g., "available" from "available.sql")
    view_name = filename.stem

    # Connect to database
    db = SQL("sqlite:///bnb.db")

    # Read SQL file
    with open(filename, "r") as f:
        statement = f.read().strip()

        # Check for intent
        if not re.search(
            rf'^CREATE\s+VIEW\s+"?{re.escape(view_name)}"?', statement, re.IGNORECASE
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
        results = db.execute(
            f"""\
            SELECT *
            FROM "{view_name}";
            """
        )
    except Exception as e:
        raise check50.Failure(f"Error when selecting from view: {str(e)}")

    # TODO: Compare results with expected contents of view, using helpers below


def check_single_col(actual, expected, ordered=False):
    """
    Checks that the single column in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (list)           expected result to match against

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert list to list of frozen sets or set of frozen sets
    try:
        if ordered:
            expected = [frozenset([elt]) for elt in expected]
        else:
            expected = {frozenset([elt]) for elt in expected}
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered)


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
