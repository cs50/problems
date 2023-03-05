import os
import re
import check50
import check50.py

BRACKET2 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
]
BRACKET4 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
    {"team": "France", "rating": 1166},
    {"team": "Argentina", "rating": 1254},
]
BRACKET8 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
    {"team": "France", "rating": 1166},
    {"team": "Argentina", "rating": 1254},
    {"team": "Brazil", "rating": 1384},
    {"team": "Mexico", "rating": 1008},
    {"team": "Belgium", "rating": 1346},
    {"team": "Japan", "rating": 528},
]
BRACKET16 = [
    {"team": "Uruguay", "rating": 976},
    {"team": "Portugal", "rating": 1306},
    {"team": "France", "rating": 1166},
    {"team": "Argentina", "rating": 1254},
    {"team": "Brazil", "rating": 1384},
    {"team": "Mexico", "rating": 1008},
    {"team": "Belgium", "rating": 1346},
    {"team": "Japan", "rating": 528},
    {"team": "Spain", "rating": 1162},
    {"team": "Russia", "rating": 493},
    {"team": "Croatia", "rating": 975},
    {"team": "Denmark", "rating": 1054},
    {"team": "Sweden", "rating": 889},
    {"team": "Switzerland", "rating": 1179},
    {"team": "Colombia", "rating": 989},
    {"team": "England", "rating": 1040},
]
QUESTIONS = [
    "Which predictions, if any, proved incorrect as you increased the number of simulations?",
    'Suppose you\'re charged a fee for each second of compute time your program uses.\nAfter how many simulations would you call the predictions "good enough"?',
]
SIMULATION_RUNS = [
    "10",
    "100",
    "1000",
    "10000",
    "100000",
    "1000000",
]


@check50.check()
def exists():
    """tournament.py exists"""
    check50.exists("tournament.py", "answers.txt")
    check50.include("2018m.csv", "2019w.csv")


@check50.check(exists)
def imports():
    """tournament.py imports"""
    check50.py.import_("tournament.py")


@check50.check(imports)
def sim_tournament_2():
    """simulate_tournament handles a bracket of size 2"""
    check_tournament(BRACKET2)


@check50.check(imports)
def sim_tournament_4():
    """simulate_tournament handles a bracket of size 4"""
    check_tournament(BRACKET4)


@check50.check(imports)
def sim_tournament_8():
    """simulate_tournament handles a bracket of size 8"""
    check_tournament(BRACKET8)


@check50.check(imports)
def sim_tournament_16():
    """simulate_tournament handles a bracket of size 16"""
    check_tournament(BRACKET16)


@check50.check(imports)
def counts():
    """correctly keeps track of wins"""
    actual = check50.run("python3 tournament.py 2018m.csv").stdout()
    percents = re.findall("[0-9]*\.[0-9]", actual)
    percents = [float(x) for x in percents]
    if sum(percents) < 99 or sum(percents) > 101:
        raise check50.Failure("fails to keep track of wins")


@check50.check(imports)
def correct_teams1():
    """correctly reports team information for Men's World Cup"""
    actual = check50.run("python3 tournament.py 2018m.csv").stdout()
    expected = ["Belgium", "Brazil", "Portugal", "Spain"]
    not_expected = ["Germany"]
    for team in expected:
        if team not in actual:
            raise check50.Failure(f"did not find team {team}")
    for team in not_expected:
        if team in actual:
            raise check50.Failure(f"incorrectly found team {team}")


@check50.check(imports)
def correct_teams2():
    """correctly reports team information for Women's World Cup"""
    actual = check50.run("python3 tournament.py 2019w.csv").stdout()
    expected = ["Germany", "United States", "England"]
    not_expected = ["Belgium"]
    for team in expected:
        if team not in actual:
            raise check50.Failure(f"did not find team {team}")
    for team in not_expected:
        if team in actual:
            raise check50.Failure(f"incorrectly found team {team}")

    percents = re.findall("[0-9]*\.[0-9]", actual)
    percents = [float(x) for x in percents]
    if sum(percents) < 99 or sum(percents) > 101:
        raise check50.Failure("fails to keep track of wins")


@check50.check(imports)
def check_answers():
    """answers.txt is complete"""
    with open("answers.txt") as f:
        contents = f.read()

        # Check timings
        for runs in SIMULATION_RUNS:
            match = re.search(
                rf"(?i){re.escape(runs)} simulations:\s*(\d+m\d+\.\d\d\ds)(?<!0m0\.000s)",
                contents,
            )
            if not match:
                raise check50.Failure(
                    "answers.txt does not include timings for each number of simulation runs",
                    help="Did you put all of your answers in 0m0.000s format?",
                )

        # Check free response
        num_questions = len(QUESTIONS)
        for i, question in enumerate(QUESTIONS):

            # Search for question, with at least 3 words afterwards
            if i + 1 < num_questions:

                # Regex includes question being asked, response, and following question
                regex = (
                    rf"(?i){re.escape(question)}"
                    + r":\s*(\S+\s+){3,}"
                    + rf"{re.escape(QUESTIONS[i + 1])}"
                )
            else:

                # Last regex includes question being asked and response
                regex = rf"(?i){re.escape(question)}" + r":\s*(\S+\s+){3,}"

            match = re.search(regex, contents)
            if not match:
                raise check50.Failure(
                    "answers.txt does not include answers to free response questions",
                    help="Did you write a sufficient response to each question?",
                )


# Helpers


def check_round(*args):
    tournament = check50.py.import_("tournament.py")
    actual = tournament.simulate_round(args[0])

    for i in range(len(actual)):
        expected = [args[0][2 * i], args[0][2 * i + 1]]
        if not (actual[i] in expected):
            raise check50.Failure(
                "simulate_round fails to determine winners in a round"
            )


def check_tournament(*args):
    tournament = check50.py.import_("tournament.py")
    actual = tournament.simulate_tournament(args[0])
    teams = [x["team"] for x in args[0]]

    if not actual in teams:
        raise check50.Failure(
            "simulate_tournament fails to return the name of 1 winning team"
        )
