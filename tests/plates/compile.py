from py_compile import compile

FILES = ["alnum_test.py", "beginning_alpha_test.py", "correct_test.py", "length_test.py", "number_test.py", "zero_test.py"]

for file in FILES:
    compile(file, f"{file[:-3]}.pyc")