import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected

@pytest.mark.skip("TODO")
def test_set():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)
    hashtable.set("orange", 2)

    assert hashtable._buckets[0].value == 5
    assert hashtable._buckets[3].value == 3
    assert hashtable._buckets[2].value == 2

@pytest.mark.skip("TODO")
def test_get():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)
    hashtable.set("orange", 2)

    assert hashtable.get("apple") == 5
    assert hashtable.get("banana") == 3
    assert hashtable.get("orange") == 2

@pytest.mark.skip("TODO")
def test_has():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)
    hashtable.set("orange", 2)

    assert hashtable.has("apple") is True
    assert hashtable.has("banana") is True
    assert hashtable.has("watermelon") is False

@pytest.mark.skip("TODO")
def test_keys():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)
    hashtable.set("orange", 2)

    assert hashtable.keys() == ["apple", "banana", "orange"]

@pytest.mark.skip("TODO")
def test_non_existing_key():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)

    try:
        hashtable.get("grape")
    except KeyError:
        pass
    else:
        assert False, "Expected KeyError but no exception was raised."


