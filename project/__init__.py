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
    if len(text) < 2500:
        raise check50.Failure(f"Description is not long enough.")

    urls = re.findall("https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+", text)
    if not urls:
        raise check50.Failure(f"Video URL is missing.")


@check50.check()
def exists_project():
    """project.py exists"""
    try:
        code = check50.run("pip3 install -r requirements.txt --force").exit()
        if code != 0:
            check50.log(f"packages installation failed")
    except:
        pass

    check50.exists("project.py")


@check50.check(exists_project)
def main_function():
    """main function exists"""
    check50.run("echo 'from project import main' | python3").exit(0)


@check50.check(exists_project)
def custom_functions():
    """implemented at least 3 top-level functions other than main"""
    check50.include("custom_functions_check.py")
    check50.run("python3 custom_functions_check.py custom_functions").exit(0)


@check50.check(custom_functions)
def unit_test():
    """each function other than main accompanied with a unit test and can be executed with pytest"""
    check50.include("custom_functions_check.py")
    check50.run("python3 custom_functions_check.py unit_test").exit(0)
