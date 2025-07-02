import check50
from re import escape

@check50.check()
def exists():
    """tasks.py exists"""
    check50.exists("tasks.py")
    check50.include("testing.py", "monday.txt")

@check50.check(exists)
def test_correct_input():
    """correctly accepts two command-line inputs"""
    check50.run("python3 tasks.py").exit(code=1)

@check50.check(exists)
def test_print_add():
    """correctly prints added task"""
    output = "1. Attend Lecture\n2. Rip a Phonebook\n3. Call David"
    check50.run("python3 tasks.py monday.txt").stdin("add Call David", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_case_add():
    """disregards the case of add"""
    output = "1. Attend Lecture\n2. Rip a Phonebook\n3. Call David"
    check50.run("python3 tasks.py monday.txt").stdin("aDd Call David", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_add_txt():
    """test"""
    check50.run("python3 testing.py get_level")

@check50.check(exists)
def test_print_remove():
    """correctly prints list after removal"""
    output = "1. Rip a Phonebook"
    check50.run("python3 tasks.py monday.txt").stdin("remove Attend Lecture", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_case_remove():
    """disregards the case of remove"""
    output = "1. Rip a Phonebook"
    check50.run("python3 tasks.py monday.txt").stdin("rEMoVe Attend Lecture", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_invalid_remove():
    """correctly exits when no match to remove"""
    check50.run("python3 tasks.py monday.txt").stdin("remove Feed the Cat", prompt=True).exit(code=1)

@check50.check(exists)
def test_just_command():
    """correctly exits when no description"""
    check50.run("python3 tasks.py monday.txt").stdin("add", prompt=True).exit(code=1)

@check50.check(exists)
def test_invalid_command():
    """correctly exits when invalid command"""
    check50.run("python3 tasks.py monday.txt").stdin("edit Rip a Phonebook", prompt=True).exit(code=1)

def regex(text):
    """match case-sensitively with any characters on either side"""
    return rf"^.*{escape(text)}.*$"