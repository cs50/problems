import check50


@check50.check()
def exists():
    """scourgify.py exists"""
    check50.exists("scourgify.py")
    check50.include("before.csv")
    check50.include("after_correct.csv")
    check50.include("before_long.csv")
    check50.include("after_long_correct.csv")


@check50.check(exists)
def test_no_arguments():
    """scourgify.py exits given no command-line arguments"""
    exit = check50.run("python3 scourgify.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_too_few_arguments():
    """scourgify.py exits given too few command-line arguments"""
    exit = check50.run("python3 scourgify.py before.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_too_many_arguments():
    """scourgify.py exits given too many command-line arguments"""
    check50.run("python3 scourgify.py before.csv after.csv before_long.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_file():
    """scourgify.py exits given invalid input file"""
    exit = check50.run("python3 scourgify.py invalid_name.csv after.csv").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_create_file():
    """scourgify.py creates new CSV file"""
    check50.run("python3 scourgify.py before.csv after.csv").exit(0)
    check50.exists("after.csv")


@check50.check(test_create_file)
def test_clean_file():
    """scourgify.py cleans short CSV file"""
    check50.run("python3 scourgify.py before.csv after.csv").exit(0)
    check50.exists("after.csv")

    with open("after.csv", "r") as student_file, open("after_correct.csv") as check_file:
        compare_csv_files(student_file, check_file)


@check50.check(test_clean_file)
def test_clean_file_long():
    """scourgify.py cleans long CSV file"""
    check50.run("python3 scourgify.py before_long.csv after_long.csv").exit(0)
    check50.exists("after_long.csv")

    with open("after_long.csv", "r") as student_file, open("after_long_correct.csv") as check_file:
        compare_csv_files(student_file, check_file)


def compare_csv_files(student_file, check_file):
    """compares two CSV files, standardizing CRLF and CR on LF (linefeed)"""

    student_output = student_file.read().replace("\r\n", "\n").replace("\r", "\n")
    correct_output = check_file.read().replace("\r\n", "\n").replace("\r", "\n")
    
    if student_output == correct_output + correct_output:
        raise check50.Failure("scourgify.py does not produce CSV with specified format", help="Did you mistakenly open your file in append mode?")
    elif student_output != correct_output:
        raise check50.Failure("scourgify.py does not produce CSV with specified format")