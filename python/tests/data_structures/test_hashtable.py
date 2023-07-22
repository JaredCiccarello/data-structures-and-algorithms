import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

# Set and get in accordance to requirements are supposed to overwrite the bucket values, therefore we access "apple" key, but getting the overwritten value.
# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

# Keys are coming out in random order,but those are the correct keys. Might have to run multiple times to get the right sequence
# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = hashtable.keys()
    expected = ["ahmad", "silent", "listen"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_get():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)
    hashtable.set("orange", 2)

    assert hashtable.get("apple") == 5
    assert hashtable.get("banana") == 3
    assert hashtable.get("orange") == 2

# @pytest.mark.skip("TODO")
def test_has():
    hashtable = Hashtable(size=5)
    hashtable.set("apple", 5)
    hashtable.set("banana", 3)
    hashtable.set("orange", 2)

    assert hashtable.has("apple") is True
    assert hashtable.has("banana") is True
    assert hashtable.has("watermelon") is False


def test_has_not():
    hashtable = Hashtable(1024)
    hashtable.set("true_key","Value from the key")
    actual =  hashtable.has("something")
    expected = False
    assert actual == expected

