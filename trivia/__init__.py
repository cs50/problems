import check50


@check50.check()
def exists():
    """Trivia submitted"""
    check50.exists("index.html")
    check50.exists("styles.css")
