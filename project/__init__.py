import re
import check50


@check50.check()
def exists_readme():
    """README.md exists"""
    check50.exists("README.md")


@check50.check(exists_readme)
def final_readme():
    """final project details"""
    text = open("README.md").read().lower()
    if len(text) < 1500:
        raise check50.Failure(f"Description is not long enough.")

    urls = re.findall("https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+", text)
    if not urls:
        raise check50.Failure(f"Video URL is missing.")


@check50.check()
def exists_project():
    """project.py exists"""
    check50.exists("project.py")


@check50.check(exists_project)
def main_function():
    """main function exists"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py main_function").exit(0)


@check50.check(exists_project)
def custom_functions():
    """implemented at least 3 top-level functions other than main"""
    check50.include("custom_checks.py")
    check50.run("python3 custom_checks.py custom_functions").exit(0)


@check50.check(custom_functions)
def unit_test():
    """each function other than main accompanied with a unit test"""
    check50.include("custom_checks.py")
    code = check50.run("python3 custom_checks.py unit_test").exit()
    if (code == 2):
        raise check50.Failure("test_project.py not found")
    elif (code != 0):
        raise check50.Failure("failed to run unit tests")
