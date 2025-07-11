from cs50 import SQL

import check50
import sqlparse


@check50.check()
def exists():
    """Archivos SQL existen"""
    for i in range(1, 14):
        check50.exists(f"{i}.sql")
    check50.include("movies.db")


def run_query(filename):
    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///movies.db")
        result = db.execute(query)
        return result
    except Exception as e:
        raise check50.Failure(f"Error al ejecutar consulta: {str(e)}")


def check_single_col(actual, expected, ordered=False):
    if actual is None or actual == []:
        raise check50.Failure("La consulta no arrojó resultados")

    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {1}:
        raise check50.Failure("La consulta solo debe devolver una sola columna")

    result = [str(list(row.values())[0]) for row in actual]
    result = result if ordered else set(result)

    expected = [str(value) for value in expected]
    expected = expected if ordered else set(expected)

    if result != expected:
        raise check50.Mismatch("\n".join(expected), "\n".join(list(result)))


def check_single_cell(actual, expected):
    return check_single_col(actual, [expected], ordered=True)


def check_double_col(actual, expected, ordered=False):
    if actual is None or actual == []:
        raise check50.Failure("La consulta no arrojó resultados")

    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {2}:
        raise check50.Failure("La consulta debe devolver exactamente dos columnas")

    result = []
    for row in actual:
        values = list(row.values())
        result.append({str(values[0]).strip(), str(values[1]).strip()})
    result = result if ordered else set(result)

    cleaned_expected = [
        {str(list(e)[0]).strip(), str(list(e)[1]).strip()} if isinstance(e, set) else e
        for e in expected
    ]
    cleaned_expected = cleaned_expected if ordered else set(cleaned_expected)

    if result != cleaned_expected:
        raise check50.Mismatch(
            "\n".join([str(entry) for entry in list(cleaned_expected)]),
            "\n".join([str(entry) for entry in list(result)])
        )


@check50.check(exists)
def test1():
    """1.sql produce resultado correcto"""
    check_single_col(
        run_query("1.sql"),
        {"Deadpool & Wolverine", "Venom: The Last Dance", "Immaculate", "Kraven the Hunter"},
        ordered=False,
    )


@check50.check(exists)
def test2():
    """2.sql produce resultado correcto"""
    check_single_cell(run_query("2.sql"), "1996")


@check50.check(exists)
def test3():
    """3.sql produce resultado correcto"""
    check_single_col(
        run_query("3.sql"),
        [
            "Barbie",
            "Oppenheimer",
            "Tenet",
            "The Batman",
            "Avatar: The Way of Water",
            "Black Panther: Wakanda Forever",
            "Top Gun: Maverick",
            "Everything Everywhere All at Once",
            "Encanto",
            "No Time to Die",
            "Soul",
        ],
        ordered=True,
    )


@check50.check(exists)
def test4():
    """4.sql produce resultado correcto"""
    check_single_cell(run_query("4.sql"), "99")


@check50.check(exists)
def test5():
    """5.sql produce resultado correcto"""
    check_double_col(
        run_query("5.sql"),
        [
            {"The Lord of the Rings", "1978"},
            {"The Lord of the Rings: The Fellowship of the Ring", "2001"},
            {"The Lord of the Rings: The Two Towers", "2002"},
            {"The Lord of the Rings - The Appendices Part 1: From Book to Vision", "2002"},
            {"The Lord of the Rings: The Return of the King", "2003"},
            {"The Lord of the Rings Symphony", "2003"},
            {"The Hobbit: An Unexpected Journey", "2012"},
            {"The Hobbit: The Desolation of Smaug", "2013"},
            {"The Hobbit: The Battle of the Five Armies", "2014"},
            {"The Hobbit: The Swedolation of Smaug", "2014"},
            {"À la recherche du Hobbit", "2014"},
            {"Le Hobbit: Le Retour du Roi du Cantal", "2015"},
            {"Music of the Lord of the Rings", "2019"},
            {"Darla's Book Club: Discussing the Lord of the Rings", "2021"},
            {"The Lord of the Rings: The War of the Rohirrim", "2024"},
            {"The Lord of the Rings: The Hunt for Gollum", "2026"},
        ],
        ordered=True,
    )


@check50.check(exists)
def test6():
    """6.sql produce resultado correcto"""
    check_double_col(
        run_query("6.sql"),
        [
            {"A Story for Winter", "10.0"},
            {"El encanto de las ballenas", "9.6"},
            {"The Irish Wedding", "9.1"},
            {"The Last Resort", "9.0"},
            {"Before I Die", "8.9"},
            {"Boys", "8.8"},
            {"The Garden of Evil", "8.7"},
            {"A Spy Movie", "8.2"},
        ],
        ordered=True,
    )


@check50.check(exists)
def test7():
    """7.sql produce resultado correcto"""
    check_single_cell(run_query("7.sql"), "6.2382")


@check50.check(exists)
def test8():
    """8.sql produce resultado correcto"""
    check_single_col(
        run_query("8.sql"),
        [
            "Andy Rossi",
            "Paola Calvo",
            "Zachary James",
            "Sherif Nagib",
            "Vincenzo Della Corte",
            "Renee Chandler",
            "Tim Fehlbaum",
            "Max Landis",
        ],
        ordered=True,
    )


@check50.check(exists)
def test9():
    """9.sql produce resultado correcto"""
    check_single_col(
        run_query("9.sql"),
        {
            "Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth",
            "Scarlett Johansson", "Jeremy Renner", "Don Cheadle", "Paul Rudd",
            "Benedict Cumberbatch", "Chadwick Boseman"
        },
        ordered=False,
    )


@check50.check(exists)
def test10():
    """10.sql produce resultado correcto"""
    check_single_col(
        run_query("10.sql"),
        {"Marlon Brando", "Diane Keaton", "Ben Kingsley", "Morgan Freeman"},
        ordered=False,
    )


@check50.check(exists)
def test11():
    """11.sql produce resultado correcto"""
    check_double_col(
        run_query("11.sql"),
        [
            {"One Night: Joshua vs. Ruiz", "8.5"},
            {"Rocky", "8.1"},
            {"Body of Work", "7.9"},
            {"First Blood", "7.7"},
            {"Creed", "7.6"},
        ],
        ordered=True,
    )


@check50.check(exists)
def test12():
    """12.sql produce resultado correcto"""
    try:
        check_single_col(
            run_query("12.sql"),
            {
                "Edward Scissorhands", "Ed Wood", "Corpse Bride", "Sleepy Hollow",
                "Charlie and the Chocolate Factory", "Sweeney Todd: The Demon Barber of Fleet Street",
                "Alice in Wonderland", "Dark Shadows"
            },
            ordered=False,
        )
    except Exception as e:
        raise check50.Failure(f"Error al ejecutar 12.sql: {str(e)}")


@check50.check(exists)
def test13():
    """13.sql produce resultado correcto"""
    check_single_col(
        run_query("13.sql"),
        {
            "Don Scardino", "Barbara Stuart", "Carrie Fisher", "Jim Belushi",
            "Dan Aykroyd", "Sally Field", "Melanie Griffith"
        },
        ordered=False,
    )
