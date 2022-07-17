import random
import re

# Setting seed to have static "random" results
random.seed(0)

# Regex patterns to detect wanted tokens
FUNC_DEFINITION = r"^def\s+(\w+)\("
FUNC_CALL = r"^(\w+)\("
IF_STATEMENT = r'^(if\s+__name__\s*==\s*"__main__"\s*:)'
AFTER_IF_FUNC_CALL = r"^\s+(\w+)\("

# Results dictionary that stores lists of matched regex results
results = {
    FUNC_DEFINITION: [],
    FUNC_CALL: [],
    IF_STATEMENT: [],
    AFTER_IF_FUNC_CALL: [],
}

with open("figlet.py", "r") as file:
    for line in file:
        for key in results:
            # Skip AFTER_IF_FUNC_CALL until IF_STATEMENT found
            if not results[IF_STATEMENT] and key == AFTER_IF_FUNC_CALL:
                continue
            
            # Skip key if no result in line
            if not (result := re.search(key, line)):
                continue
            
            # Append result group to the correct results list
            results[key].append(result.groups()[0])

            # Only one result per line
            break


# If there was no IF_STATEMENT just import and let it run
if not results[IF_STATEMENT]:
    import figlet
# Call the main function if it appeared after the IF_STATEMENT
elif "main" in results[AFTER_IF_FUNC_CALL]:
    import figlet
    figlet.main()
# Exit with error 12 when there was an IF_STATEMENT, but no main function
else:
    import sys
    sys.exit(12)
