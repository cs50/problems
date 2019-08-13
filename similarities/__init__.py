import os

import check50
import check50.py

@check50.check()
def exists():
    """helpers.py exists"""
    check50.exists("helpers.py")

@check50.check(exists)
def imports():
    """can import helpers.py """
    check50.py.import_("helpers.py")


@check50.check(imports)
def lines_none():
    """detects no lines in common"""
    a = "Line 1\nLine 2"
    b = "Line 3\nLine 4"
    check_strings("lines", set(), a, b)

@check50.check(imports)
def lines_one():
    """detects one line in common"""
    a = "Line 1\nLine 2\nLine 3\nLine 4"
    b = "Line 5\nLine 6\nLine 3\nLine 8"
    check_strings("lines", {"Line 3"}, a, b)

@check50.check(imports)
def lines_multiple():
    """detects multiple lines in common"""
    a = "Line 1\nLine 2\nLine 3\nLine 4"
    b = "Line 4\nLine 6\nLine 3\nLine 8"
    check_strings("lines", {"Line 3", "Line 4"}, a, b)

@check50.check(imports)
def lines_duplicates():
    """handles duplicate lines in common"""
    a = "Line 1\nLine 2\nLine 3\nLine 4"
    b = "Line 4\nLine 6\nLine 3\nLine 8\nLine 3"
    check_strings("lines", {"Line 3", "Line 4"}, a, b)

@check50.check(imports)
def sentences_none():
    """handles no sentences in common"""
    a = "This is a sentence. Here is another one."
    b = "This is a third sentence. A fourth. A fifth."
    check_strings("sentences", set(), a, b)

@check50.check(imports)
def sentences_one():
    """handles one sentence in common"""
    a = "This is a sentence. Here is another one."
    b = "This is a third sentence. Here is another one. A fifth."
    check_strings("sentences", {"Here is another one."}, a, b)

@check50.check(imports)
def sentences_multiple():
    """handles multiple sentences in common"""
    a = "This is a sentence. Here is another one."
    b = "This is a third sentence. Here is another one. This is a sentence."
    check_strings("sentences", {"Here is another one.", "This is a sentence."}, a, b)

@check50.check(imports)
def sentences_punctuation():
    """handles sentences with different punctuation"""
    a = "Is this a sentence? Here is another one!"
    b = "This is a third sentence. Here is another one. Is this a sentence?"
    check_strings("sentences", {"Is this a sentence?"}, a, b)

@check50.check(imports)
def sentences_mid_punctuation():
    """handles sentences with punctuation mid-sentence"""
    a = "One... two... three. Four. Five."
    b = "Four. One... two... three. Six."
    check_strings("sentences", {"One... two... three.", "Four."}, a, b)

@check50.check(imports)
def sentences_duplicates():
    """handles duplicate sentences in common"""
    a = "This is one. This is two. This is three. This is two. This is one."
    b = "This is three. This is two. This is four. This is five."
    check_strings("sentences", {"This is three.", "This is two."}, a, b)

@check50.check(imports)
def substrings_none():
    """handles no substrings in common"""
    a = "foo"
    b = "bar"
    check_strings("substrings", set(), a, b, 1)
    check_strings("substrings", set(), a, b, 2)
    check_strings("substrings", set(), a, b, 3)

@check50.check(imports)
def substrings_one():
    """handles one substring in common"""
    a = "foobar"
    b = "bar"
    check_strings("substrings", {"bar"}, a, b, 3)

@check50.check(imports)
def substrings_multiple():
    """handles multiple substrings in common"""
    a = "foobar"
    b = "barfoo"
    check_strings("substrings", {"fo", "oo", "ba", "ar"}, a, b, 2)
    check_strings("substrings", {"foo", "bar"}, a, b, 3)

@check50.check(imports)
def substrings_identical():
    """handles substrings when strings are identical"""
    a = "foobar"
    b = "foobar"
    check_strings("substrings", {"foo", "oob", "oba","bar"}, a, b, 3)
    check_strings("substrings", {"foob", "ooba", "obar"}, a, b, 4)
    check_strings("substrings", {"fooba", "oobar"}, a, b, 5)
    check_strings("substrings", {"foobar"}, a, b, 6)

@check50.check(imports)
def substrings_bounds():
    """handles substring length longer than string length"""
    a = "foobar"
    b = "foobar"
    check_strings("substrings", set(), a, b, 7)

@check50.check(imports)
def substrings_duplicates():
    """handles duplicate substrings in common"""
    a = "foobarbaz"
    b = "barbaz"
    check_strings("substrings", {"ba", "ar", "rb", "az"}, a, b, 2)

@check50.check(imports)
def substrings_nonalpha():
    """handles substrings containing nonalpha chars"""
    a = "foo bar baz"
    b = "foo barbaz"
    check_strings("substrings", {"foo b", "oo ba", "o bar"}, a, b, 5)

def check_strings(method, expected, *args):
    a, b = args[0], args[1]
    helpers = check50.py.import_("helpers.py")
    check50.log(f"running '{method}' on inputs {repr(a)} and {repr(b)}...")
    try:
        with open(os.devnull, "w") as f:
            actual = getattr(helpers, method)(*args)
    except Exception as e:
        raise check50.Failure(str(e))

    if len(actual) != len(expected):
        raise check50.Failure(f"expected {len(expected)} matches, not {len(actual)}")
    actual = set(actual)
    if actual != expected:
        raise check50.Mismatch(str(expected), str(actual))
