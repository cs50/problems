import check50
from re import escape

@check50.check()
def exists():
    """tasks.py exists"""
    check50.exists("tasks.py")
    check50.include("testing.py", "monday.txt")

@check50.check(exists)
def test_correct_input():
    """tasks.py correctly accepts two command-line inputs"""
    check50.run("python3 tasks.py").exit(code=1)

@check50.check(exists)
def test_simple_add():
    """tasks.py correctly handles simple add case"""
    output = "1. Attend Lecture\n2. Rip a Phonebook\n3. Eat"
    check50.run("python3 tasks.py monday.txt").stdin("add Eat", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_print_add():
    """tasks.py correctly prints added task"""
    output = "1. Attend Lecture\n2. Rip a Phonebook\n3. Call David"
    check50.run("python3 tasks.py monday.txt").stdin("add Call David", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_case_add():
    """tasks.py correctly handles case-sensitive add"""
    output = "1. Attend Lecture\n2. Rip a Phonebook\n3. Call David"
    check50.run("python3 tasks.py monday.txt").stdin("aDd Call David", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_print_remove():
    """tasks.py correctly prints list after removal"""
    output = "1. Rip a Phonebook"
    check50.run("python3 tasks.py monday.txt").stdin("remove Attend Lecture", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_case_remove():
    """tasks.py correctly handles case-sensitive remove"""
    output = "1. Rip a Phonebook"
    check50.run("python3 tasks.py monday.txt").stdin("rEMoVe Attend Lecture", prompt=True).stdout(regex(output), output).kill()

@check50.check(exists)
def test_invalid_remove():
    """tasks.py correctly exits when no match to remove"""
    check50.run("python3 tasks.py monday.txt").stdin("remove Feed the Cat", prompt=True).exit(code=1)

@check50.check(exists)
def test_just_command():
    """tasks.py correctly exits when no task is given"""
    check50.run("python3 tasks.py monday.txt").stdin("add", prompt=True).exit(code=1)

@check50.check(exists)
def test_invalid_command():
    """tasks.py correctly exits when invalid operation"""
    check50.run("python3 tasks.py monday.txt").stdin("edit Rip a Phonebook", prompt=True).exit(code=1)

def regex(text):
    """match case-sensitively with any characters on either side"""
    return rf"^.*{escape(text)}.*$"
