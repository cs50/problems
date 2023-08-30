from cs50 import SQL

import check50
import sqlparse


@check50.check()
def sql_exists():
    """SQL files exists"""
    for i in range(1, 8):
        check50.exists(f"{i}.sql")
    check50.include("songs.db")


@check50.check()
def answers_exists():
    """answers.txt exists"""
    check50.exists("answers.txt")


@check50.check(sql_exists)
def test1():
    """1.sql produces correct result"""
    solution = {
        "God's Plan",
        "SAD!",
        "rockstar (feat. 21 Savage)",
        "Psycho (feat. Ty Dolla $ign)",
        "In My Feelings",
        "Better Now",
        "I Like It",
        "One Kiss (with Dua Lipa)",
        "IDGAF",
        "FRIENDS",
        "Havana",
        "Lucid Dreams",
        "Nice For What",
        "Girls Like You (feat. Cardi B)",
        "The Middle",
        "All The Stars (with SZA)",
        "no tears left to cry",
        "X",
        "Moonlight",
        "Look Alive (feat. Drake)",
        "These Days (feat. Jess Glynne, Macklemore & Dan Caplen)",
        "Te Bote - Remix",
        "Mine",
        "Youngblood",
        "New Rules",
        "Shape of You",
        "Love Lies (with Normani)",
        "Meant to Be (feat. Florida Georgia Line)",
        "Jocelyn Flores",
        "Perfect",
        "Taste (feat. Offset)",
        "Solo (feat. Demi Lovato)",
        "I Fall Apart",
        "Nevermind",
        "Echame La Culpa",
        "Eastside (with Halsey & Khalid)",
        "Never Be the Same",
        "Wolves",
        "changes",
        "In My Mind",
        "River (feat. Ed Sheeran)",
        "Dura",
        "SICKO MODE",
        "Thunder",
        "Me Niego",
        "Jackie Chan",
        "Finesse (Remix) [feat. Cardi B]",
        "Back To You - From 13 Reasons Why",
        "Let You Down",
        "Call Out My Name",
        "Ric Flair Drip (& Metro Boomin)",
        "Happier",
        "Too Good At Goodbyes",
        "Freaky Friday (feat. Chris Brown)",
        "Believer",
        "FEFE (feat. Nicki Minaj & Murda Beatz)",
        "Rise",
        "Body (feat. brando)",
        "XO TOUR Llif3",
        "Sin Pijama",
        "2002",
        "Nonstop",
        "Fuck Love (feat. Trippie Redd)",
        "In My Blood",
        "Silence",
        "God is a woman",
        "Dejala que vuelva (feat. Manuel Turizo)",
        "Flames",
        "What Lovers Do",
        "Taki Taki (with Selena Gomez, Ozuna & Cardi B)",
        "Let Me Go (with Alesso, Florida Georgia Line & watt)",
        "Feel It Still",
        "Pray For Me (with Kendrick Lamar)",
        "Walk It Talk It",
        "Him & I (with Halsey)",
        "Candy Paint",
        "Congratulations",
        "1, 2, 3 (feat. Jason Derulo & De La Ghetto)",
        "Criminal",
        "Plug Walk",
        "lovely (with Khalid)",
        "Stir Fry",
        "HUMBLE.",
        "Vaina Loca",
        "Perfect Duet (Ed Sheeran & Beyonc?)",
        "Corazon (feat. Nego do Borel)",
        "Young Dumb & Broke",
        "Siguelo Bailando",
        "Downtown",
        "Bella",
        "Promises (with Sam Smith)",
        "Yes Indeed",
        "I Like Me Better",
        "This Is Me",
        "Everybody Dies In Their Nightmares",
        "Rewrite The Stars",
        "I Miss You (feat. Julia Michaels)",
        "No Brainer",
        "Dusk Till Dawn - Radio Edit",
        "Be Alright",
    }
    check_single_col(run_query("1.sql"), solution, ordered=False)


@check50.check(sql_exists)
def test2():
    """2.sql produces correct result"""
    solution = [
        "changes",
        "SAD!",
        "God's Plan",
        "Feel It Still",
        "Criminal",
        "Lucid Dreams",
        "Him & I (with Halsey)",
        "Eastside (with Halsey & Khalid)",
        "River (feat. Ed Sheeran)",
        "In My Feelings",
        "Too Good At Goodbyes",
        "I Like Me Better",
        "These Days (feat. Jess Glynne, Macklemore & Dan Caplen)",
        "Nice For What",
        "Flames",
        "Vaina Loca",
        "Sin Pijama",
        "Bella",
        "Me Niego",
        "1, 2, 3 (feat. Jason Derulo & De La Ghetto)",
        "Plug Walk",
        "Perfect Duet (Ed Sheeran & Beyonc?)",
        "Dura",
        "Perfect",
        "FRIENDS",
        "Taki Taki (with Selena Gomez, Ozuna & Cardi B)",
        "Shape of You",
        "Echame La Culpa",
        "2002",
        "Te Bote - Remix",
        "All The Stars (with SZA)",
        "IDGAF",
        "Taste (feat. Offset)",
        "Siguelo Bailando",
        "Nevermind",
        "Ric Flair Drip (& Metro Boomin)",
        "Happier",
        "Pray For Me (with Kendrick Lamar)",
        "Back To You - From 13 Reasons Why",
        "Let Me Go (with Alesso, Florida Georgia Line & watt)",
        "Havana",
        "Solo (feat. Demi Lovato)",
        "I Miss You (feat. Julia Michaels)",
        "Finesse (Remix) [feat. Cardi B]",
        "Rise",
        "The Middle",
        "What Lovers Do",
        "lovely (with Khalid)",
        "New Rules",
        "Yes Indeed",
        "Youngblood",
        "Body (feat. brando)",
        "no tears left to cry",
        "Promises (with Sam Smith)",
        "Congratulations",
        "One Kiss (with Dua Lipa)",
        "Wolves",
        "Believer",
        "Girls Like You (feat. Cardi B)",
        "Rewrite The Stars",
        "In My Mind",
        "FEFE (feat. Nicki Minaj & Murda Beatz)",
        "Be Alright",
        "Jackie Chan",
        "Moonlight",
        "Never Be the Same",
        "Everybody Dies In Their Nightmares",
        "Fuck Love (feat. Trippie Redd)",
        "Freaky Friday (feat. Chris Brown)",
        "Jocelyn Flores",
        "Call Out My Name",
        "No Brainer",
        "I Like It",
        "Young Dumb & Broke",
        "Look Alive (feat. Drake)",
        "In My Blood",
        "Psycho (feat. Ty Dolla $ign)",
        "Silence",
        "Mine",
        "I Fall Apart",
        "Love Lies (with Normani)",
        "Better Now",
        "God is a woman",
        "Walk It Talk It",
        "Let You Down",
        "HUMBLE.",
        "Meant to Be (feat. Florida Georgia Line)",
        "Nonstop",
        "SICKO MODE",
        "XO TOUR Llif3",
        "rockstar (feat. 21 Savage)",
        "Downtown",
        "Thunder",
        "Dejala que vuelva (feat. Manuel Turizo)",
        "Candy Paint",
        "Dusk Till Dawn - Radio Edit",
        "X",
        "Stir Fry",
        "This Is Me",
        "Corazon (feat. Nego do Borel)",
    ]
    check_single_col(run_query("2.sql"), solution, ordered=True)


@check50.check(sql_exists)
def test3():
    """3.sql produces correct result"""
    check_single_col(
        run_query("3.sql"),
        [
            "Te Bote - Remix",
            "SICKO MODE",
            "Walk It Talk It",
            "Him & I (with Halsey)",
            "Perfect",
        ],
        ordered=True,
    )


@check50.check(sql_exists)
def test4():
    """4.sql produces correct result"""
    check_single_col(
        run_query("4.sql"),
        {
            "Dura",
            "Me Niego",
            "Feel It Still",
            "1, 2, 3 (feat. Jason Derulo & De La Ghetto)",
            "Criminal",
        },
        ordered=False,
    )


@check50.check(sql_exists)
def test5():
    """5.sql produces correct result"""
    check_single_cell(run_query("5.sql"), "0.65906", floating=True)


@check50.check(sql_exists)
def test6():
    """6.sql produces correct result"""
    check_single_col(
        run_query("6.sql"),
        {
            "rockstar (feat. 21 Savage)",
            "Psycho (feat. Ty Dolla $ign)",
            "Better Now",
            "I Fall Apart",
            "Candy Paint",
            "Congratulations",
        },
        ordered=False,
    )


@check50.check(sql_exists)
def test7():
    """7.sql produces correct result"""
    check_single_cell(run_query("7.sql"), "0.599", floating=True)


@check50.check(sql_exists)
def test8():
    """8.sql produces correct result"""
    check_single_col(
        run_query("8.sql"),
        {
            "rockstar (feat. 21 Savage)",
            "Psycho (feat. Ty Dolla $ign)",
            "Girls Like You (feat. Cardi B)",
            "Look Alive (feat. Drake)",
            "These Days (feat. Jess Glynne, Macklemore & Dan Caplen)",
            "Meant to Be (feat. Florida Georgia Line)",
            "Taste (feat. Offset)",
            "Solo (feat. Demi Lovato)",
            "River (feat. Ed Sheeran)",
            "Finesse (Remix) [feat. Cardi B]",
            "Freaky Friday (feat. Chris Brown)",
            "FEFE (feat. Nicki Minaj & Murda Beatz)",
            "Body (feat. brando)",
            "Fuck Love (feat. Trippie Redd)",
            "Dejala que vuelva (feat. Manuel Turizo)",
            "1, 2, 3 (feat. Jason Derulo & De La Ghetto)",
            "Corazon (feat. Nego do Borel)",
            "I Miss You (feat. Julia Michaels)",
        },
        ordered=False,
    )


@check50.check(answers_exists)
def answers():
    """answers.txt includes reflection"""
    with open("answers.txt", "r") as f:
        contents = f.read()

    if len(contents.split()) < 10:
        raise check50.Failure("answers.txt does not contain a sufficiently long reflection")


def run_query(filename):
    try:
        with open(filename) as f:
            query = f.read().strip()
            query = sqlparse.format(query, strip_comments=True).strip()
        db = SQL("sqlite:///songs.db")
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


def check_single_cell(actual, expected, floating=False):
    if floating:
        if len(actual) != 1 or len(actual[0]) != 1:
            raise check50.Failure(
                "Query should only return a single column and single cell"
            )
        if abs(float(list(actual[0].values())[0]) - float(expected)) > 0.01:
            raise check50.Mismatch("\n".join(expected), str(actual))
        return
    return check_single_col(actual, [expected], ordered=True)


def check_double_col(actual, expected, ordered=False):
    """
    Checks for queries that return just a single column, ensures correct results.
    """

    # Make sure query returned results
    if actual is None or actual == []:
        raise check50.Failure("Query did not return results")

    # Make sure there is only a single column
    row_counts = {len(list(row.values())) for row in actual}
    if row_counts != {2}:
        raise check50.Failure("Query should only return a single column")

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
