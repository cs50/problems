import os
import sys
import subprocess
from inspect import getmembers, isfunction

import project

# Attempt to import test_project, if it exists
try:
    import test_project
except:
    pass

match sys.argv[1]:

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

            # Ensure unit tests can be executed with pytest            
            subprocess.check_call(["pytest", "test_project.py"])
        
        # Inspect unit test individually
        else:
            for function in getmembers(project, isfunction):
                
                # Ensure each custom function other than main accompanied with a unit test
                if function[0] != "main":
                    assert f"test_{function[0]}.py" in files

                    # Ensure each unit test can be executed with pytest
                    subprocess.check_call(["pytest", f"test_{function[0]}.py"])
    
    case "custom_functions":
        assert len([func for func in getmembers(project, isfunction)]) - 1 >= 3
