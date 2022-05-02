import check50
from pexpect import EOF
from re import escape


@check50.check()
def exists():
    """adieu.py exists"""
    check50.exists("adieu.py")


@check50.check(exists)
def test_EOF():
    """input of EOF halts program"""
    input = "Liesl"

    # Run program
    program = check50.run("python3 adieu.py")
    
    # Send name and EOF
    program.stdin(input, prompt=False).stdin(EOF, prompt=False)
    
    # Program exits gracefully
    program.exit(0)


@check50.check(test_EOF)
def test_single_name():
    """input of \"Liesl\" yields \"Adieu, adieu, to Liesl\""""
    input = "Liesl"
    output = "Adieu, adieu, to Liesl"
    
    # Run program
    program = check50.run("python3 adieu.py")
    
    # Send name and EOF
    program.stdin(input, prompt=False).stdin(EOF, prompt=False)

    # Check for expected output
    program.stdout(regex(output), output, regex=True)

    # Program exits gracefully
    program.exit(0)


@check50.check(test_EOF)
def test_two_names():
    """input of \"Liesl\" and \"Friedrich\" yields \"Adieu, adieu, to Liesl and Friedrich\""""
    input = ["Liesl", "Friedrich"]
    output = "Adieu, adieu, to Liesl and Friedrich"
    multi_name_test(input, output)


@check50.check(test_EOF)
def test_three_names():
    """input of \"Liesl\", \"Friedrich\", and \"Louisa\" yields \"Adieu, adieu, to Liesl, Friedrich, and Louisa\""""
    input = ["Liesl", "Friedrich", "Louisa"]
    output = "Adieu, adieu, to Liesl, Friedrich, and Louisa"
    multi_name_test(input, output)


@check50.check(test_EOF)
def test_four_names():
    """input of \"Liesl\", \"Friedrich\", \"Louisa\", and \"Kurt\" yields \"Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt\""""
    input = ["Liesl", "Friedrich", "Louisa", "Kurt"]
    output = "Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt"
    multi_name_test(input, output)


@check50.check(test_EOF)
def test_five_names():
    """input of \"Liesl\", \"Friedrich\", \"Louisa\", \"Kurt\", and \"Brigitta\" yields \"Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta\""""
    input = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta"]
    output = "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta"
    multi_name_test(input, output)


@check50.check(test_EOF)
def test_six_names():
    """input of \"Liesl\", \"Friedrich\", \"Louisa\", \"Kurt\", \"Brigitta\", and \"Marta\" yields \"Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta\""""
    input = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta"]
    output = "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta"
    multi_name_test(input, output)


@check50.check(test_EOF)
def test_six_names():
    """input of \"Liesl\", \"Friedrich\", \"Louisa\", \"Kurt\", \"Brigitta\", \"Marta\", and \"Gretl\" yields \"Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl\""""
    input = ["Liesl", "Friedrich", "Louisa", "Kurt", "Brigitta", "Marta", "Gretl"]
    output = "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl"
    multi_name_test(input, output)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'


def multi_name_test(input, output):
    """test names in list create expected output"""

    # Run program and supply names in input via stdin
    program = check50.run("python3 adieu.py")
    for name in input:
        program.stdin(name, prompt=False)

    # EOF halts program, output is as expected
    program.stdin(EOF, prompt=False)
    program.stdout(regex(output), output, regex=True)

    # Program exits gracefully
    program.exit(0)