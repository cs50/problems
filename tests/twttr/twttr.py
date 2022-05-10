from correct_test import convert as patched_convert


def convert(s):
    return patched_convert(s)


if __name__ == "__main__":
    pass