"""Use PLACEHOLDER.pyc as implementation for testing student checks"""

import marshal

# Header bytes in .pyc files have changed with python versions
# https://peps.python.org/pep-0552/
HEADER_BYTES = 16

# Open test file for reading in binary format
with open("PLACEHOLDER.pyc", "rb") as test_file:

    # Move file pointer past .pyc file header
    test_file.seek(HEADER_BYTES)

    # De-marshal .pyc file for execution
    test_file_obj = marshal.load(test_file)

    # Run test file to gain access to function definitions
    exec(test_file_obj)

# With help from https://stackoverflow.com/questions/34709390/how-can-i-import-a-pyc-compiled-python-file-and-use-it