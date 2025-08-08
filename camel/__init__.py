import check50


@check50.check()
def exists():
    """camel.py exists"""
    check50.exists("camel.py")


def check_camel_output(input_text, expected_output):
    """Helper function to check camel.py output after the colon."""
    try:
        actual = check50.run("python3 camel.py").stdin(input_text, prompt=True).stdout()
        
        # Check if there's no stdout (program might have crashed)
        if not actual or actual.strip() == "":
            raise check50.Failure("Program produced no output (may have crashed)")
        
        actual = actual.split(":")[-1].strip()
        if actual != expected_output:
            raise check50.Mismatch(expected_output, actual)
            
    except check50.Failure:
        raise
    except Exception as e:
        raise check50.Failure(f"Program crashed or encountered an error: {str(e)}")


@check50.check(exists)
def test_name():
    """input of \"name\" yields output of \"name\""""
    check_camel_output("name", "name")


@check50.check(exists)
def test_firstName():
    """input of \"firstName\" yields output of \"first_name\""""
    check_camel_output("firstName", "first_name")


@check50.check(exists)
def test_preferredFirstName():
    """input of \"preferredFirstName\" yields output of \"preferred_first_name\""""
    check_camel_output("preferredFirstName", "preferred_first_name")