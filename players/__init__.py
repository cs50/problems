from cs50 import SQL

import check50
import sqlparse


@check50.check()
def exists():
    """SQL files exist"""
    for i in range(10):
        check50.exists(f"{i + 1}.sql")
    check50.include("players-check.db")


@check50.check(exists)
def test1():
    """1.sql produces correct result"""
    check_multi_col(
        run_query("1.sql"),
        [{'Cairo', 'GA', 'USA'}],
        ordered=False,
    )


@check50.check(exists)
def test2():
    """2.sql produces correct result"""
    check_single_cell(run_query("2.sql"), 'L')


@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_single_col(
        run_query("3.sql"),
        ['20557',
        '20558',
        '20559',
        '20560',
        '20561',
        '20562',
        '20563',
        '20564',
        '20565',
        '20566',
        '20567',
        '20568',
        '20569',
        '20570',
        '20571',
        '20572',
        '20573',
        '20574',
        '20575',
        '20576'],
        ordered=False,
    )


@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_multi_col(
        run_query("4.sql"),
        [{'Reach', 'Al'},
        {'Albert', 'Pujols'},
        {'Leonard', 'Andy'},
        {'Anibal', 'Sanchez'},
        {'Barney', 'Dreyfuss'},
        {'Bob', 'Addy'},
        {'Higham', 'Dick'},
        {'Duffy', 'Ed'},
        {'Fergy', 'Malone'},
        {'George', 'Hall'},
        {'Heubel', 'George'},
        {'Harry', 'Wright'},
        {'Votto', 'Joey'},
        {'Perez', 'Oliver'},
        {'Cano', 'Robinson'},
        {'Rynie', 'Wolters'},
        {'Jackson', 'Sam'},
        {'Bellan', 'Steve'},
        {'Molina', 'Yadier'}],
        ordered=True,
    )


@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_multi_col(
        run_query("5.sql"),
        [{'Spalding', 'Al'},
        {'Albert', 'Pujols'},
        {'Cooper', 'Andy'},
        {'Leonard', 'Andy'},
        {'Anibal', 'Sanchez'},
        {'Bill', 'Adair'},
        {'Bill', 'Evers'},
        {'Mathews', 'Bobby'},
        {'Cal', 'McVey'},
        {'Chappy', 'Lane'},
        {'Charlie', 'Gould'},
        {'Chuck', 'Lauer'},
        {'Force', 'Davy'},
        {'Allison', 'Doug'},
        {'Ezra', 'Sutton'},
        {'Fergy', 'Malone'},
        {'George', 'Wright'},
        {'Germany', 'Smith'},
        {'Harry', 'Wright'},
        {'Jackie', 'Robinson'},
        {'Smith', 'Joe'},
        {'John', 'Cassidy'},
        {'John', 'McMullin'},
        {'Upton', 'Justin'},
        {'Suzuki', 'Kurt'},
        {'Baldwin', 'Mark'},
        {'Jackson', 'Sam'},
        {'Tom', 'Carey'},
        {'Clippard', 'Tyler'},
        {'Molina', 'Yadier'}],
        ordered=True,
    )


@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_multi_col(
        run_query("6.sql"),
        [{'Baldwin', 'Mark', '1887-05-02'},
        {'Zay', '1886-10-07', 'William'},
        {'Smith', '1886-09-10', 'Elmer'},
        {'Jim', '1884-10-09', 'Gray'},
        {'1884-07-17', 'Chuck', 'Lauer'},
        {'Frank', '1884-04-24', 'Shaffer'},
        {'Germany', 'Smith', '1884-04-17'},
        {'Jake', 'Seymour', '1882-09-23'},
        {'Chappy', 'Lane', '1882-05-16'},
        {'Pratt', 'Al', '1871-05-04'}],
        ordered=True,
    )


@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_single_cell(run_query("7.sql"), '13')


@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_multi_col(
        run_query("8.sql"),
        [{'217.6', '73.2'}],
        ordered=False,
    )


@check50.check(exists)
def test9():
    """9.sql produces correct result"""
    check_multi_col(
        run_query("9.sql"),
        [{'Albert', 'Pujols'},
        {'Anibal', 'Sanchez'},
        {'Smith', 'Joe'},
        {'Votto', 'Joey'},
        {'Upton', 'Justin'},
        {'Suzuki', 'Kurt'},
        {'Perez', 'Oliver'},
        {'Cano', 'Robinson'},
        {'Clippard', 'Tyler'},
        {'Molina', 'Yadier'}],
        ordered=True,
    )


@check50.check(exists)
def test10():
    """10.sql runs without error"""
    run_query("10.sql")


def run_query(filename):
    """
    Runs the SQL query contained in 'filename' and returns its output.

    positional arguments:
        filename (str)      file containing SQL query

    returns:
        list[dict]
    """

    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///players-check.db")
        result = db.execute(query)
        return result
    except Exception as e:
        raise check50.Failure(f"Error when executing query: {str(e)}")


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
