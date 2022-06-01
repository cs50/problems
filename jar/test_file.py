from jar import Jar
import pytest


def test_init():
    assert Jar().capacity == 12
    assert Jar(13).capacity == 13


def test_raises_value_error():
    with pytest.raises(ValueError):
        Jar(-1)


def test_empty_str():
    jar = Jar()
    assert str(jar) == ""


def test_full_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_too_full():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(11)
    assert jar.size == 0


def test_empty():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(13)
