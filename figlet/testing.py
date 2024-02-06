import random
import re

# Setting seed to have static "random" results
random.seed(0)

# Regex patterns to detect wanted tokens
# Unneeded patterns commented out
# FUNC_DEFINITION = r"^def\s+(\w+)\("
# FUNC_CALL = r"^(\w+)\("
IF_STATEMENT = r'^(if(?:\s+|\s*\(\s*)__name__\s*==\s*"__main__"(?:\s*|\s*\)\s*):)'
AFTER_IF_FUNC_CALL = r"^\s+(\w+)\s*\(\s*\)"

# Results dictionary that stores sets of matched regex results
results = {
    IF_STATEMENT: set(),
    AFTER_IF_FUNC_CALL: set(),
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
            
            # Append result group to the correct results set
            results[key].add(result.groups()[0])

            # Only one result per line
            break

# If there was no IF_STATEMENT just import and let it run
if not results[IF_STATEMENT]:
    import figlet
# Call the main function if it appeared after the IF_STATEMENT
elif "main" in results[AFTER_IF_FUNC_CALL]:
    import figlet
    figlet.main()
