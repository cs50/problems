import check50
import check50.c
import re

@check50.check()
def exists():
    """cash.c exists"""
    check50.exists("cash.c")

    # Include additional unit testing file
    check50.include("testing.c")

@check50.check(exists)
def compiles():
    """cash.c compiles"""
    # Check if student code compiles
    check50.c.compile("cash.c", lcs50=True)
    
    # Rename main function to "distro_main"
    cash = re.sub("int\s+main", "int distro_main", open("cash.c").read())

    # Read testing file
    testing = open("testing.c").read()

    # Combine student code and testing file
    with open("cash_test.c", "w") as f:
        f.write(cash)
        f.write("\n")
        f.write(testing)

    check50.c.compile("cash_test.c", lcs50=True)

@check50.check(compiles)
def cents():
    """get_cents returns integer number of cents"""
    check50.run("./cash_test 0").stdin("100", prompt = True).stdout("100").exit()

@check50.check(compiles)
def negative():
    """get_cents rejects negative input"""
    check50.run("./cash_test 0").stdin("-10", prompt = True).reject()

@check50.check(compiles)
def test_reject_foo():
    """get_cents rejects a non-numeric input of "foo" """
    check50.run("./cash_test 0").stdin("foo", prompt = True).reject()

@check50.check(compiles)
def quarters0():
    """calculate_quarters returns 2 when input is 50"""
    check50.run("./cash_test 1").stdout("2")

@check50.check(compiles)
def quarters1():
    """calculate_quarters returns 1 when input is 42"""
    check50.run("./cash_test 2").stdout("1")

@check50.check(compiles)
def dimes0():
    """calculate_dimes returns 1 when input is 10"""
    check50.run("./cash_test 3").stdout("1")

@check50.check(compiles)
def dimes1():
    """calculate_dimes returns 1 when input is 15"""
    check50.run("./cash_test 4").stdout("1")

@check50.check(compiles)
def dimes2():
    """calculate_dimes returns 7 when input is 73"""
    check50.run("./cash_test 8").stdout("7")    
    
@check50.check(compiles)
def nickels0():
    """calculate_nickels returns 1 when input is 5"""
    check50.run("./cash_test 5").stdout("1")

@check50.check(compiles)
def nickels1():
    """calculate_nickels returns 5 when input is 28"""
    check50.run("./cash_test 6").stdout("5")

@check50.check(compiles)
def pennies():
    """calculate_pennies returns 4 when input is 4"""
    check50.run("./cash_test 7").stdout("4")
  

@check50.check(compiles)
def test41():
    """input of 41 cents yields output of 4 coins"""
    output = check50.run("./cash").stdin("41", prompt = True).stdout("4\n").exit()

@check50.check(compiles)
def test160():
    """input of 160 cents yields output of 7 coins"""
    check50.run("./cash").stdin("160", prompt = True).stdout("7\n").exit()

def coins(num):
    # regex that matches `num` not surrounded by any other numbers (so coins(2) won't match e.g. 123)
    return fr"(?<!\d){num}(?!\d)"
