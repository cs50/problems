import check50


@check50.check()
def exists():
    """answers.md exists"""
    check50.exists("answers.md")


@check50.check(exists)
def check_length():
    """answers.md contains at least 250 characters"""
    text = open("answers.md").read().lower()
    if len(text) < 250:
        raise check50.Failure(f"answers.md is not long enough.")
