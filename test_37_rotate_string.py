
import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_two_positions():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_full_length():
    assert module.rotate_string("abc", 3) == "abc"


def test_rotate_empty_string():
    assert module.rotate_string("", 2) == ""


def test_rotate_more_than_length():
    assert module.rotate_string("abcd", 6) == "cdab"
