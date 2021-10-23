import re

import check50


@check50.check()
def exists():
    """log.sql and answers.txt exist"""
    check50.exists("log.sql", "answers.txt")

@check50.check(exists)
def log_file():
    """log file contains SELECT queries"""

    log = open("log.sql").read().lower()
    if "select" not in log:
        raise check50.Failure(f"missing SELECT queries in log.sql")

@check50.check(exists)
def solved():
    """mystery solved"""

    answers = open("answers.txt").read().lower()

    thief = "6272756365"
    city = "6e657720796f726b"
    accomplice = "726f62696e"

    for q in ["thief is", "escaped to", "accomplice is"]:
        if answers.count(q) > 1:
            raise check50.Failure("invalid answers.txt formatting")

    identify_thief = re.search(f"thief\s*is\s*:?\s*{bytes.fromhex(thief).decode('utf-8')}", answers)
    identify_city = re.search(f"escaped\s*to\s*:?\s*{bytes.fromhex(city).decode('utf-8')}", answers)
    identify_accomplice = re.search(f"accomplice\s*is\s*:?\s*{bytes.fromhex(accomplice).decode('utf-8')}", answers)
    if not identify_thief or not identify_city or not identify_accomplice:
        raise check50.Failure(f"answers.txt does not correctly solve mystery")
