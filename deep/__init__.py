import check50


@check50.check()
def exists():
    """deep.py exists"""
    check50.exists("deep.py")


@check50.check(exists)
def test_42():
    """input of 42 yields output of Yes"""
    input = "42"
    output = "Yes"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty_two():
    """input of forty-two yields output of Yes"""
    input = "forty-two"
    output = "Yes"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty_two_space():
    """input of forty two yields output of Yes"""
    input = "forty two"
    output = "Yes"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_forty_two_malformed():
    """input of FoRty TwO yields output of Yes"""
    input = "FoRty TwO"
    output = "Yes"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_42_spaces():
    """input of 42, with spaces on either side, yields output of Yes"""
    input = " 42  "
    output = "Yes"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_50():
    """input of 50 yields output of No"""
    input = "50"
    output = "No"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_fifty():
    """input of fifty yields output of No"""
    input = "fifty"
    output = "No"
    check50.run("python3 deep.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(answer):
    """match case-insensitively with only whitespace on either side"""
    return rf'(?i)^\s*{answer}\s*$'