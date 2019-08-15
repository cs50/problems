import check50

@check50.check()
def ceasar():
    """spelled caesar correctly"""
    raise check50.Failure("Looks like you may have typed 'ceasar' when you meant 'caesar'. Try rerunning this command with 'cs50/problems/2019/x/caesar'!")
