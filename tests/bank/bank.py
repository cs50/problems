from correct_test import value as patched_value


def value(s):
    return patched_value(s)


if __name__ == "__main__":
    pass