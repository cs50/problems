import os
import re
import sys
from inspect import getmembers, isfunction

# Ignore all import statements
def strip_imports(filename):
    buffer = []
    with open(filename) as file:
        for line in file.readlines():
            if re.match("^\s*(?:from|import)\s+(\w+(?:\s*,\s*\w+)*)", line) is not None:
                continue

            buffer.append(line)
    
    with open(f"stripped_{filename}", "w+") as file:
        file.write("".join(buffer))

strip_imports("project.py")
strip_imports("test_project.py")

import stripped_project as project
import stripped_test_project as test_project


match sys.argv[1]:

    case "main_function":
        assert "main" in [func[0] for func in getmembers(project, isfunction)]

    case "custom_functions":

        # Ensure there are at least 3 top-level functions other than main
        assert len([func for func in getmembers(project, isfunction)]) - 1 >= 3

    case "unit_test":
        files = os.listdir(".")

        # If all the unit tests reside in one single test file
        if "test_project.py" in files:

            # Get all unit tests from test_project.py
            unit_test_functions = [func[0] for func in getmembers(test_project, isfunction)]

            # Exclude unit test for main function
            try:
                unit_test_functions.remove("test_main")
            except:
                pass

            # Ensure each custom function other than main accompanied with a unit test
            for function in getmembers(project, isfunction):
                if function[0] != "main":
                    assert f"test_{function[0]}" in unit_test_functions

        else:
            sys.exit(2)
