from jar import Jar
import pytest
import inspect


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


def test_testfile():
    import test_jar as t

    num_tests = 0
    for member in inspect.getmembers(t):
        if inspect.isfunction(member[1]) and member[0].startswith("test"):
            source = inspect.getsource(member[1]).split("\n")[1:]
            for line in source:
                line = line.strip().replace("...", "").replace("pass", "")
                if line and not line.startswith("#"):
                    num_tests += 1
                    break

        if num_tests >= 4:
            break

    assert num_tests >= 4
