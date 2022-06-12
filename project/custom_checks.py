import sys
from inspect import getmembers, isfunction

match sys.argv[1]:

    case "main_function":
        with open("project.py") as file:

            # Look for main function definition and avoid importing any libraries
            assert "def main" in "".join(file.read().splitlines())

    case "custom_functions":
        with open("project.py") as file:
            counter = 0
            for line in file.readlines():
                if "def main" in line.strip():
                    continue
                elif "def" in line.strip():
                    counter += 1
            
            # Ensure there are at least 3 top-level functions other than main
            assert counter >= 3

    case "unit_test":
        with open("test_project.py") as file:
            counter = 0
            for line in file.readlines():
                if "def test_" in line:
                    counter += 1
            
            assert counter >= 3
