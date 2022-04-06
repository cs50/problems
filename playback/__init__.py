import check50


@check50.check()
def exists():
    """playback.py exists"""
    check50.exists("playback.py")

@check50.check(exists)
def testcs50():
    """input of \"This is CS50\" yields output of \"This...is...CS50\""""
    check50.run("python3 playback.py").stdin("This is CS50", prompt=False).stdout(r"This\.\.\.is\.\.\.CS50|This…is…CS50", "This...is...CS50").exit()

@check50.check(exists)
def testfunctions():
    """input of \"This is our week on functions\" yields output of \"This...is...our...week...on...functions\""""
    check50.run("python3 playback.py").stdin("This is our week on functions", prompt=False).stdout(r"This\.\.\.is\.\.\.our\.\.\.week\.\.\.on\.\.\.functions|This…is…our…week…on…functions", "This...is...our...week...on...functions").exit()

@check50.check(exists)
def testimplemented():
    """input of \"Let's implement a function called hello\" yields output of \"Let's...implement...a...function...called...hello\""""
    check50.run("python3 playback.py").stdin("Let's implement a function called hello", prompt=False).stdout(r"Let's\.\.\.implement\.\.\.a\.\.\.function\.\.\.called\.\.\.hello|Let's…implement…a…function…called…hello", "Let's...implement...a...function...called...hello").exit()