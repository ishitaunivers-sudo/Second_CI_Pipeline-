
import importlib

module = importlib.import_module("32_count_words")


def test_normal_sentence():
    assert module.count_words("Python is very easy") == 4


def test_extra_spaces():
    assert module.count_words("  Hello   World  ") == 2


def test_empty_sentence():
    assert module.count_words("") == 0
