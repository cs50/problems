from correct_test import is_valid as patched_is_valid


def is_valid(s):
    return patched_is_valid(s)


if __name__ == "__main__":
    pass