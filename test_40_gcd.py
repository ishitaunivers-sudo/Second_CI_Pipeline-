
import importlib

module = importlib.import_module("40_gcd")


def test_gcd_normal():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime():
    assert module.gcd(7, 13) == 1


def test_gcd_zero():
    assert module.gcd(10, 0) == 10


def test_gcd_negative():
    assert module.gcd(-12, 18) == 6
