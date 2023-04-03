from cs50 import SQL

import check50
import sqlparse


@check50.check()
def exists():
    """SQL files exists"""
    for i in range(1, 14):
        check50.exists(f"{i}.sql")
    check50.include("movies.db")


@check50.check(exists)
def test1():
    """1.sql produces correct result"""
    check_single_col(
        run_query("1.sql"),
        {"Iron Man", "The Dark Knight", "Slumdog Millionaire", "Kung Fu Panda"},
        ordered=False,
    )


@check50.check(exists)
def test2():
    """2.sql produces correct result"""
    check_single_cell(run_query("2.sql"), "1988")


@check50.check(exists)
def test3():
    """3.sql produces correct result"""
    check_single_col(
        run_query("3.sql"),
        [
            "Avengers: Infinity War",
            "Black Panther",
            "Eighth Grade",
            "Gemini Man",
            "Happy Times",
            "Incredibles 2",
            "Kirklet",
            "Ma Rainey's Black Bottom",
            "Roma",
            "The Professor",
            "Toy Story 4",
        ],
        ordered=True,
    )


@check50.check(exists)
def test4():
    """4.sql produces correct result"""
    check_single_cell(run_query("4.sql"), "2")


@check50.check(exists)
def test5():
    """5.sql produces correct result"""
    check_double_col(
        run_query("5.sql"),
        [
            {"Harry Potter and the Sorcerer's Stone", "2001"},
            {"Harry Potter and the Chamber of Secrets", "2002"},
            {"Harry Potter and the Prisoner of Azkaban", "2004"},
            {"Harry Potter and the Goblet of Fire", "2005"},
            {"Harry Potter and the Order of the Phoenix", "2007"},
            {"Harry Potter and the Half-Blood Prince", "2009"},
            {"Harry Potter and the Deathly Hallows: Part 1", "2010"},
            {"Harry Potter and the Deathly Hallows: Part 2", "2011"},
            {"Harry Potter: A History of Magic", "2017"},
        ],
        ordered=True,
    )


@check50.check(exists)
def test6():
    """6.sql produces correct result"""
    check_single_cell(run_query("6.sql"), "7.74")


@check50.check(exists)
def test7():
    """7.sql produces correct result"""
    check_double_col(
        run_query("7.sql"),
        [
            {"Inception", "8.8"},
            {"Toy Story 3", "8.3"},
            {"How to Train Your Dragon", "8.1"},
            {"Shutter Island", "8.1"},
            {"The King's Speech", "8.0"},
            {"Harry Potter and the Deathly Hallows: Part 1", "7.7"},
            {"Iron Man 2", "7.0"},
            {"Alice in Wonderland", "6.4"},
        ],
        ordered=True,
    )


@check50.check(exists)
def test8():
    """8.sql produces correct result"""
    check_single_col(
        run_query("8.sql"),
        {"Don Rickles", "Jim Varney", "Tom Hanks", "Tim Allen"},
        ordered=False,
    )


@check50.check(exists)
def test9():
    """9.sql produces correct result"""
    check_single_col(
        run_query("9.sql"),
        [
            "Craig T. Nelson",
            "Richard Griffifths",
            "Samuel L. Jackson",
            "Holly Hunter",
            "Jason Lee",
            "Rupert Grint",
            "Daniel Radcliffe",
            "Emma Watson",
        ],
        ordered=True,
    )


@check50.check(exists)
def test10():
    """10.sql produces correct result"""
    check_single_col(
        run_query("10.sql"),
        {"Christopher Nolan", "Frank Darabont", "Yimou Zhang"},
        ordered=False,
    )


@check50.check(exists)
def test11():
    """11.sql produces correct result"""
    check_single_col(
        run_query("11.sql"),
        ["42", "Black Panther", "Marshall", "Ma Rainey's Black Bottom", "Get on Up"],
        ordered=True,
    )


@check50.check(exists)
def test12():
    """12.sql produces correct result"""
    try:
        check_single_col(
            run_query("12.sql"),
            {
                "Corpse Bride",
                "Charlie and the Chocolate Factory",
                "Alice in Wonderland",
                "Alice Through the Looking Glass",
            },
            ordered=False,
        )
    except (check50.Failure, check50.Mismatch):

        # Alternate version of test12 to account for removing Johnny Depp from the specification
        check_single_col(
            run_query("12.sql"),
            {"Silver Linings Playbook", "Serena", "American Hustle", "Joy"},
            ordered=False,
        )


@check50.check(exists)
def test13():
    """13.sql produces correct result"""
    check_single_col(
        run_query("13.sql"),
        {
            "Bill Paxton",
            "Gary Sinise",
            "James McAvoy",
            "Jennifer Lawrence",
            "Tom Cruise",
            "Michael Fassbender",
            "Tom Hanks",
        },
        ordered=False,
    )


def run_query(filename):
    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///movies.db")
        result = db.execute(query)
        return result
    except Exception as e:
        raise check50.Failure(f"Error when executing query: {str(e)}")


def check_single_col(actual, expected, ordered=False):
    """
    Checks for queries that return just a single column, ensures correct results.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # Make sure there is only a single column
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {1}:
        raise check50.Failure("Query should only return a single column")

    # Get data from column
    try:
        result = [str(list(row.values())[0]) for row in actual]
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Check column data against expected values
    expected = [str(value) for value in expected]
    if not ordered:
        expected = set(expected)
    if result != expected:
        raise check50.Mismatch("\n".join(expected), "\n".join(list(result)))


def check_single_cell(actual, expected):
    return check_single_col(actual, [expected], ordered=True)


def check_double_col(actual, expected, ordered=False):
    """
    Checks for queries that return just a single column, ensures correct results.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # Make sure there are only two columns
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {2}:
        raise check50.Failure("Query should return exactly two columns")

    # Get data from column
    try:
        result = []
        for row in actual:
            values = list(row.values())
            result.append({str(values[0]), str(values[1])})
        result = result if ordered else set(result)
    except IndexError:
        return None

    # Check column data against expected values
    if result != expected:
        raise check50.Mismatch(
            "\n".join([str(entry) for entry in list(expected)]),
            "\n".join([str(entry) for entry in list(result)]),
        )
