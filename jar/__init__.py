import check50
import re
import ast


@check50.check()
def exists():
    """jar.py exists"""
    check50.exists("jar.py")
    check50.exists("test_jar.py")
    check50.include("test_file.py")


@check50.check(exists)
def test_init():
    """Jar's constructor initializes a cookie jar with given capacity"""
    check50.run("pytest test_file.py -k 'test_init'").exit(0)


@check50.check(exists)
def test_init_value_error():
    """Jar's constructor raises ValueError when called with negative capacity"""
    check50.run("pytest test_file.py -k 'test_raises_value_error'").exit(0)


@check50.check(exists)
def test_empty_str():
    """Empty jar prints zero cookies"""
    check50.run("pytest test_file.py -k 'test_empty_str'").exit(0)


@check50.check(exists)
def test_full_str():
    """Jar prints total number of cookies deposited"""
    check50.run("pytest test_file.py -k 'test_full_str'").exit(0)


@check50.check(exists)
def test_too_full():
    """Jar's deposit method raises ValueError when deposited cookies exceed the jar's capacity"""
    check50.run("pytest test_file.py -k 'test_too_full'").exit(0)


@check50.check(exists)
def test_withdraw():
    """Jar's withdraw method removes cookies from the jar's size"""
    check50.run("pytest test_file.py -k 'test_withdraw'").exit(0)


@check50.check(exists)
def test_empty():
    """Jar's withdraw method raises ValueError when withdrawn cookies exceed jar's size"""
    check50.run("pytest test_file.py -k 'test_empty'").exit(0)


@check50.check(exists)
def test_student_file_passes():
    """Implementation of Jar passes all tests in test_jar.py"""
    check50.run("pytest test_jar.py").exit(0)


@check50.check(test_student_file_passes)
def test_number_functions():
    """test_jar.py contains at least four valid functions"""
    valid_test_out = check50.run("pytest test_file.py -k 'test_testfile'").stdout()
    valid_matches = re.search(r"(\d+) passed", valid_test_out)
    out = check50.run("pytest test_jar.py").stdout()
    matches = re.search(r"(\d+) passed", out)
    if not matches:
        raise check50.Failure("Could not parse output of pytest")

    try:
        functions = int(matches.group(1))
    except ValueError:
        raise check50.Failure("Could not parse output of pytest")

    if functions < 4 or not valid_matches:
        raise check50.Failure(
            "test_jar.py does not contain at least four valid functions"
        )


@check50.check(test_student_file_passes)
def test_named_functions():
    """test_jar.py defines test_init, test_str, test_deposit, and test_withdraw"""
    result = check50.run("pytest test_jar.py --collect-only -q").stdout()
    collected_tests = []
    for line in result.strip().split('\n'):
        if '::test_' in line:
            test_name = line.split('::')[1].strip()
            collected_tests.append(test_name)

    required_funcs = ["test_init", "test_str", "test_deposit", "test_withdraw"]
    missing_funcs = []
    for func in required_funcs:
        if func not in collected_tests:
            missing_funcs.append(func)

    if missing_funcs:
        raise check50.Failure(
            f"Function(s) not collected by pytest in test_jar.py: {', '.join(missing_funcs)}")


@check50.check(test_student_file_passes)
def test_valid_testing():
    """test_jar.py contains implemented functions"""
    with open("test_jar.py") as f:
        contents = f.read()

    try:
        tree = ast.parse(contents)
    except SyntaxError:
        raise check50.Failure("test_jar.py contains syntax errors")

    required_funcs = ["test_init", "test_str", "test_deposit", "test_withdraw"]
    implemented_funcs = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in required_funcs:
            has_test_content = False

            # Walk through all nodes in the function to find test-related code
            for child in ast.walk(node):
                # Check for assert statements
                if isinstance(child, ast.Assert):
                    has_test_content = True
                    break
                # Check for pytest.raises or with statements (for context managers)
                elif isinstance(child, ast.With):
                    has_test_content = True
                    break
                # Check for calls to pytest functions or assert methods
                elif isinstance(child, ast.Call):
                    if isinstance(child.func, ast.Attribute):
                        # Check for pytest.* or self.assert* calls
                        if (hasattr(child.func.value, 'id') and child.func.value.id == 'pytest') or \
                           child.func.attr.startswith('assert'):
                            has_test_content = True
                            break

            if has_test_content:
                implemented_funcs.append(node.name)

    missing_or_empty = set(required_funcs) - set(implemented_funcs)
    if missing_or_empty:
        raise check50.Failure(
            f"Missing or empty function(s) in test_jar.py: {', '.join(sorted(missing_or_empty))}")
