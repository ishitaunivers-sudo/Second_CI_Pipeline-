
import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating():
    assert module.first_non_repeating("swiss") == "w"


def test_all_repeated():
    assert module.first_non_repeating("aabb") is None


def test_single_character():
    assert module.first_non_repeating("x") == "x"
