@check50.check(exists)
def test_beginning_alpha_checks():
    """test_plates catches plates.py without beginning alphabetical checks"""
    test_implementation("beginning_alpha_test", code=1)


@check50.check(exists)
def test_length_checks():
    """test_plates catches plates.py without length checks"""
    test_implementation("length_test", code=1)


@check50.check(exists)
def test_number_placement_checks():
    """test_plates catches plates.py without checks for number placement"""
    test_implementation("number_test", code=1)


@check50.check(exists)
def test_zero_checks():
    """test_plates catches plates.py without checks for zero placement"""
    test_implementation("zero_test", code=1)


@check50.check(exists)
def test_alnum_checks():
    """test_plates catches plates.py without checks for alphanumeric characters"""
    test_implementation("alnum_test", code=1)