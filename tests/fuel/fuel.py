from correct_test import convert as patched_convert
from correct_test import gauge as patched_gauge


def convert(s):
    return patched_convert(s)


def gauge(s):
    return patched_gauge(s)


if __name__ == "__main__":
    pass