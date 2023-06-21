import pytest
from data_structures.linked_list import LinkedList, TargetError


# @pytest.mark.skip("TODO")
def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")
# LinkedList = apple
    linked_list.insert("banana")
# LinkedList = banana, apple
    linked_list.append("cucumber")
# LinkedList = banana, apple, cucumber
    assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"


# @pytest.mark.skip("TODO")
def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(ValueError):
        linked_list.insert_before("radish", "zucchinni")


# @pytest.mark.skip("TODO")
def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(ValueError):
        linked_list.insert_before("radish", "zucchinni")


# @pytest.mark.skip("TODO")
def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(ValueError):
        linked_list.insert_after("radish", "zucchinni")


# @pytest.mark.skip("TODO")
def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(ValueError):
        linked_list.insert_after("radish", "zucchinni")

# TypeError: expected exception must be a BaseException type, not TargetError
# Changing TargetError to ValueError causes tests to pass.
